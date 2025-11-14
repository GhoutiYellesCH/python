import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, 400)
x2 = np.linspace(0, 10, 400)
X, Y = np.meshgrid(x1, x2)

con2_1 = (6 - x1) / 2 
con2_2 = 4 - x1
con2_3 = np.ones_like(x1) * 3

plt.plot(x1, con2_1, color='blue')
plt.plot(x1, con2_2, color='green')
plt.axvline(x=3, color='red')

Z_val = np.arange(0, 7.5, 1)
for z in Z_val:
    x2 = z - 2*x1
    plt.plot(x1, x2, color='lightgrey')

plt.fill_between(x1, 0, np.minimum(np.minimum(con2_1, con2_2), con2_3), color='lightblue', alpha=0.5)
plt.fill_between(x1, 0, 10, where=(x1 > 3), color='white', alpha=1.0, interpolate=True)

plt.xlim(0, 4)
plt.ylim(0, 4)
plt.grid(True)
plt.show()
