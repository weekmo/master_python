import matplotlib.pyplot as plt
import numpy as np
x=np.arange(15).reshape(3,5)
y=np.ones((3,2))
z=np.arange(0,50,5)
a=np.arange(5)
b=np.random.random((1,10))
plt.plot([1,2,3,5],[2,3,5,6],'k')
plt.axis([0,10,0,10])
plt.ylabel('Time')
plt.xlabel('Data Size')
plt.show()