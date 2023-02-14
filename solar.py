import math

import matplotlib.pyplot as plt
import numpy as np
import unicodedata

# Great spiral that expands at 400km/s and rotates 360 degrees in 25 days

m = 10000

tlist = np.linspace(0, 2160000, num=m)
# Selects 10000 evenly-spaced points within the 25-day period

angle = []
for i in range(m):
    if len(angle) == 0:
        angle.append(0)
    angle.append(angle[i]+((360/m)*(np.pi/180)))
angle.pop()
# The angle expands at a constant rate, reaching 360 degrees at the end of the rotational period


def solar(t):
    return t * (400 / (1.496 * 10 ** 8))
# The solar wind propels outward at a rate of 400 km/s, the returned value is then converted from km to AU


slist = solar(tlist)
x = slist * np.cos(angle)
y = slist * np.sin(angle)
# Conversion from polar to cartesian for radial length and angle calculations


fig, ax = plt.subplots()
# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(x, y)
ax.set_title("Numerical Model of Solar Wind in one Solar Rotation (AU)", va='bottom')
ax.grid(True)

clist = []

for i in range(len(x)):
    temp = [x[i], y[i]]
    clist.append(temp)

def getAngle(xdist, ydist, rxdist, rydist):
    vector_a = float(np.sqrt(((xdist ** 2) + (ydist ** 2))))
    vector_b = float(np.sqrt(((rxdist ** 2) + (rydist ** 2))))
    dot_prod = float((xdist * rxdist) + (ydist * rydist))
    ratio = abs(dot_prod / (vector_a * vector_b))
    theta = math.acos(ratio) * (360 / (2 * np.pi))
    return float(theta)

theta_list = []
radial_length = []

for i in range(len(clist)):
    distance = np.sqrt((((clist[i])[0])**2) + (((clist[i])[1])**2))
    radial_length.append(distance)

    if i == len(clist)-1:
        theta_list.append(theta_list[-1])
        break

    x_initial = (clist[i])[0]
    x_final = (clist[i+1])[0]

    y_initial = (clist[i])[1]
    y_final = (clist[i + 1])[1]

    x_dist = (x_final - x_initial)
    y_dist = (y_final - y_initial)

    if x_initial == 0:
        r_slope = y_final / x_final
    else:
        r_slope = y_initial / x_initial

    ry = r_slope * x_final

    ry_dist = (ry - y_initial)

    the = getAngle(x_dist, y_dist, x_dist, ry_dist)

    theta_list.append(the)

ax.plot(radial_length, theta_list)
th = unicodedata.lookup("GREEK SMALL LETTER THETA")
plt.xlabel("Distance from the Center of the Sun [AU]")
plt.ylabel("Magnetic Field Angel [" + th + "]")
# def degree(r):
#     i = 0
#     while i < len(r):
#         r[i] = r[i] * 180/np.pi
#         i += 1
#     return r
#
#
# angle2 = degree(angle)
# th = unicodedata.lookup("GREEK SMALL LETTER THETA")
# plt.plot(slist, angle2)
# plt.xlabel("Distance from Solar Center [AU]")
# plt.ylabel("Angle of Magnetic Field [" + th + "]")
# plt.xlim(0, 6)
# plt.yticks([0, 60, 120, 180, 240, 300, 360])
# plt.ylim(0, 360)
# plt.grid(True)
# ax.set_rmax(1)
# use this to zoom in by setting the rmax to the needed AU value

# ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
# ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line

# ax.grid(True)

# ax.set_title("The Travel of Solar Wind in one Solar Rotation", va='bottom')

plt.show()
