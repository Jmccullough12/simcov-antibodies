#include <upcxx/upcxx.hpp>
#include <string>
#include <fstream>
#include <unistd.h>

std::string &left_trim(std::string &str) {
   auto it = std::find_if(str.begin(), str.end(), [](char ch) { return !std::isspace<char>(ch, std::locale()); });
   str.erase(str.begin(), it);
   return str;
}
std::string get_proc_pin() {
  std::ifstream f("/proc/self/status");
  std::string line;
  std::string prefix = "Cpus_allowed_list:";
  while (getline(f, line)) {
    if (line.substr(0, prefix.length()) == prefix) {
       line = line.substr(prefix.length(), line.length() - prefix.length());
       return left_trim(line);
       break;
    }
  }
  return "";
}

int main(int argc, char **argv) {
  upcxx::init();
  char hnbuf[64];
  gethostname(hnbuf, sizeof(hnbuf) - 1);
  auto pid = getpid();
  std::string pinnings = get_proc_pin();
  for(int i = 0; i < upcxx::rank_n(); i++) {
    if (i < upcxx::rank_me()) 
      upcxx::barrier();
    if (i == upcxx::rank_me())
      std::cout << "Hello from " << upcxx::rank_me() << " of " << upcxx::rank_n() << " on " << hnbuf << " pid " << pid << " bound to " << pinnings << std::endl;
    if (i >= upcxx::rank_me()) 
      upcxx::barrier();
  }
  upcxx::finalize(); 
  exit(0);
}
