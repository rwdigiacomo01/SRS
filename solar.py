import matplotlib.pyplot as plt
import numpy as np

# Great spiral that expands at 400km/s and rotates 360 degrees in 25 days

m = 10000

tlist = np.linspace(0, 2160000, num=m)

angle = []
for i in range(m):
    if len(angle) == 0:
        angle.append(0)
    angle.append(angle[i]+((360/m)*(np.pi/180)))
#temp solution
# I kept getting 1 more value than I needed so I popped the last value
angle.pop()


def solar (t):
    return t * ((400)/(1.496*10**8))

slist = solar(tlist)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angle, slist)

#ax.set_rmax(1)
# use this to zoom in by setting the rmax to the needed AU value

# ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
# ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line

ax.grid(True)

ax.set_title("The Travel of Solar Wind in one Solar Rotation", va='bottom')
plt.show()