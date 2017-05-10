# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:55:23 2016

@author: khatami
"""


import numpy as np
import pylab
import matplotlib.pyplot as plt
x1=np.arange(100)
y1=x1-100
err1=np.random.random(100)
err1*=20
err1-=10

params = {'axes.labelsize' : 30,
              'font.size' : 30,
              'legend.fontsize' : 30,
              'xtick.labelsize' : 26,
              'ytick.labelsize' : 26}
pylab.rcParams.update(params)        
ax=plt.subplot(2,2,1)
ax.scatter(x1,y1+err1,c='y')
ax=plt.subplot(2,2,2)
plt.subplots_adjust(hspace=0.4)
ax.plot(x1,y1+err1,c='b',marker='^',label='line1')
ax.plot(x1,2*y1+err1,c='r',label='line2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.xlim(-50,150)
plt.ylim(-50,50)
x2=np.linspace(-20,20,200)
err2=np.random.random(200)-0.5
ax=plt.subplot(2,2,3)
y2=np.cos(x2)
ax.plot(x2,y2,c='g')
ax=plt.subplot(2,2,4)
ax.plot(x2,y2+err2)
ax.scatter(x2,y2+err2,s=10)
ax.set_title("f(x)=cos(x)")
plt.xlabel('x')
plt.ylabel('cos(y)')

plt.show()
