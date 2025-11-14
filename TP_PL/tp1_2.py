import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, 400)
x2 = np.linspace(0, 10, 400)
X1,X2=np.meshgrid(x1,x2)

Z1=2*X1+X2
C1 = X1 + 2*X2 <= 6  # x1 + 2x2 <= 6
C2 = X1 + X2 <= 4     # x1 + x2 <= 4
C3 = X1 <= 3  

plt.contourf(X1,X2,Z1,levels=[- np.inf,0],colors=['lightgrey'])
plt.contourf(X1,X2,C1,levels=[- np.inf,0],colors=['lightblue'])
plt.contourf(X1,X2,C2,levels=[- np.inf,0],colors=['lightgreen'])
plt.contourf(X1,X2,C3,levels=[- np.inf,0],colors=['red'])



plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()