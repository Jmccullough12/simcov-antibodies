import sys
import numpy as np

def generateAverage(name, steps):
    #listy = []

    #for i in range(int(steps)):
        #listy.append(0.0)
    listy = np.zeros(int(steps))

    for num in range(10):
        resultFile = num + 1
        file = "results_" + name + "_batch/simcov" + str(resultFile) + ".stats"

        with open(file, 'r') as f:
               file1 = f.readlines()
               for i in range(int(steps)):
                   if (i == 0):
                       continue
                   line = file1[i].split('\t')
                   listy[i-1] = listy[i-1] + float(line[8])

        #resultFile += 1
    #result = [] # if we want to plot
    for i in range(len(listy)):

        listy[i] = listy[i] / 10

    return listy


def saveAverage(name, xs, ys):
    xs2 = xs.astype(int)
    #result = np.column_stack((xs2,ys))
    #print(result)

    file = "averaged_results/" + name + ".stats"
    result = []
    with open(file, 'w') as f:
        for i in range(len(xs)):
            content = str(xs2[i]) + "\t" + str(ys[i]) + "\n"
            f.write(content)


def main():
    name = sys.argv[1]
    steps = sys.argv[2]
    virs = generateAverage(name, steps)
    #print(virs)
    timesteps = np.zeros(int(steps), dtype=int)
    for i in range(int(steps)):
        timesteps[i] = int(i)

    timesteps = timesteps.astype(int)
    saveAverage(name, timesteps, virs)


if __name__=="__main__":
    main()
