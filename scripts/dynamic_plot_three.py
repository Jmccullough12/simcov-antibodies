#1/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np





#plot_subplot(options.compare_file, ax_virus, [8], 'avg virions per cell', lw=4, alpha=0.3, clear=False,
#             log_scale=options.log_scale, scale=options.virus_scale)


def makePlot(xs, ys1, ys2, ys3, label1, label2, label3):
    fig = plt.figure()
    ax = plt.axes()
    #ax.legend(loc='upper left')
    ax.set_ylabel('Virion Count')
    ax.set_xlabel('Time (days)')
    ax.set_ylim(0.5, 10 * np.max(ys1))
    ax.set_yscale('log')

    plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x/1440), ',')))
    colors = ['blue', 'red', 'orange']
    plt.locator_params(axis='x',nbins=25)
    #ax.xaxis.set_ticks(np.linspace(0,len(xs),1))

    ax.plot(xs,ys1, label="Not Vaccinated",color=colors[0])
    ax.plot(xs,ys2, label="Vaccinated",color=colors[1])
    #ax.plot(xs,ys3, label="Scale = 0.10",color=colors[2])

    ax.legend(loc='lower left')
    ax.set_title("Vaccinated vs. Not Vaccinated")

    plt.savefig('vaccinated.png')


def getYs(name, steps):
    file = "averaged_results/" + name + ".stats"
    ys = np.zeros(int(steps))
    with open(file, 'r') as f:
           file1 = f.readlines()
           for i in range(int(steps)):
               line = file1[i].split('\t')
               ys[i] = float(line[1])

    return ys

def main():
    name1 = sys.argv[1]
    name2 = sys.argv[2]
    name3 = sys.argv[3]
    steps = sys.argv[4]

    ys1 = getYs(name1, steps)
    ys2 = getYs(name2, steps)
    ys3 = getYs(name3, steps)

    xs = np.zeros(int(steps), dtype=int)
    for i in range(int(steps)):
        xs[i] = int(i)

    print(ys1)
    print(ys2)
    print(ys3)

    makePlot(xs,ys1,ys2,ys3,name1,name2,name3)
if __name__=="__main__":
    main()
