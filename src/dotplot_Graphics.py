
import matplotlib.pyplot as plt


def figure_setup(xlable, ylable, xscale, yscale, head, num):
    fig = plt.figure(num)
    plt.ylabel(ylable)
    plt.xlabel(xlable)
    plt.ylim([yscale, 0])
    plt.xlim([0, xscale])
    plt.title(head)
    return fig


def dotplot2Graphics(dp, hdA, hdB, heading, filename):
    x = []
    y = []
    extension=filename.split(".")[-1]
    filename=".".join(filename.split(".")[:-1])
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i, j] == 1:
                x.append(i)
                y.append(j)
    figure_setup(hdA, hdB, len(dp), len(dp[0]), heading, 1)
    plt.scatter(y, x, color='#AC1B49', marker='*')

    plt.savefig(filename[:-4] + "1." + extension)
    figure_setup(hdA, hdB, len(dp), len(dp[0]), heading, 2)
    plt.imshow(dp, 'Blues')
    plt.savefig(filename[:-4] + "2." + extension)
    plt.show()
