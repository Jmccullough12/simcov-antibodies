avgList = []

for num in range(9):
    resultFile = 1
    file = "results_batch_test/" + "simcov" + str(resultFile) + ".stats"
    listy = []
    with open(file) as f1:
           file1 = f1.readlines()
           count = 0
           for line in file1:
               line = line.split('\t')
               if (count):
                   listy.append((line[0],line[8]))
               count += 1
    resultFile += 1

for range in range(33118):
    countTwo = 0
    sum = 0
    avg = 0
    for e in listy:
        if(int(e[0]) == range):
            sum += float(e[1])
            if (countTwo < 33120):
                countTwo+=1
    avg = sum / 33119
    output = str(range) + '\t' + str(avg)
    print(output)
    #result.append((range,avg))
