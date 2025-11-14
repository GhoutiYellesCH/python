import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-10,10)
y=np.linspace(-10,10)
X,Y=np.meshgrid(x,y)

Z1=-2*X-Y+8
plt.contourf(X,Y,Z1,levels=[- np.inf,0],colors=['lightblue'])
xa=np.linspace(0,1000,num=5)
xb=np.linspace(0,1000,num=5)
xb=8-2*xa
plt.plot(xa,xb)

plt.xlim(-10,10)
plt.ylim(-10,10)
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0,color='black',linewidth=0.5)
plt.show()