import numpy as np
import pylab
import matplotlib.pyplot as plt


def read_file(data_file):
    f = open(data_file,'r')
    data_list=[]
    for line in f:
        #print(line.split())
        data_list.append([x for x in line.split(',')])
    data = np.zeros(shape=(len(data_list),5))
    gender=[]
    for k,v in enumerate(data_list):
        data[k,:] = np.array([v[0],v[2],v[3],v[4],v[5]])
        gender.append(v[1])
    data=data.astype(int)
    gender=np.asarray(gender)

def myPlot(data,gender):
    params = {'axes.labelsize' : 15,
              'font.size' : 15,
              'legend.fontsize' : 15,
              'xtick.labelsize' : 13,
              'ytick.labelsize' : 13}
    pylab.rcParams.update(params)
    ax=plt.subplot(2,2,1)
    ax.scatter(data[gender[:] == 'M', 1],data[gender[:] == 'M',2],c='r')
    ax=plt.subplot(2,2,2)
    ax.scatter(data[gender[:] == 'F', 1],data[gender[:] == 'F',2],c='b')


print(read_file("info_linux.csv"))
