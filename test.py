import numpy as np
import matplotlib.pyplot as plt


r = np.arange(0, 1, 0.01)
theta = 2 * np.pi * r

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rmax(1)
ax.set_rticks([0.5, 1])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

# angle = input("What angle does the radial line exit the origin from: ")

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()