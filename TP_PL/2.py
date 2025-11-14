import numpy as np
import matplotlib.pyplot as plt

# Define x1 and x2 range
x1 = np.linspace(0, 10)
x2 = np.linspace(0, 10, 400)
X, Y = np.meshgrid(x1, x2)

# Define the constraints
con2_1 = (6 - x1) / 2   # x1 + 2*x2 <= 6
con2_2 = 4 - x1         # x1 + x2 <= 4
con2_3 = np.ones_like(x1) * 3  # x1 <= 3

Z1=2*X+Y
# Plotting the constraints
plt.plot(x1, con2_1, label=r'$x_1 + 2x_2 \leq 6$')
plt.plot(x1, con2_2, label=r'$x_1 + x_2 \leq 4$')
plt.axvline(x=3, label=r'$x_1 \leq 3$', color='red')
plt.contourf(X,Y,Z1,levels=[- np.inf,0],colors='lightgrey')

# Filling the feasible region
plt.fill_between(x1, 0, np.minimum(np.minimum(con2_1, con2_2), con2_3), color='lightblue', alpha=0.5)
plt.fill_between(x1, 0, 10, where=(x1 > 3), color='white')

# Setting the plot limits
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
