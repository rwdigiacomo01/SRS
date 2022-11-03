import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")

x_data = np.random.randint(0, 50, (500,))
y_data = np.random.randint(0, 50, (500,))
z_data = np.random.randint(0, 50, (500,))

ax.scatter(x_data, y_data, z_data)

plt.show()