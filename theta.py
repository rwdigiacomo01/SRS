import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

import unicodedata

radius = 2 * np.pi
tlist = np.linspace(0, (2 * np.pi), num=1000)

def x(t):
    return ((radius / (2 * np.pi)) * t) * np.cos(t)


def y(t):
    return ((radius / (2 * np.pi)) * t) * np.sin(t)

xlist = x(tlist)
ylist = y(tlist)
clist = []

for i in range(len(xlist)):
    temp = [xlist[i], ylist[i]]
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
        add = theta_list[-1]
        theta_list.append(add)
        break

    x_initial = (clist[i])[0]
    x_final = (clist[i+1])[0]

    y_initial = (clist[i])[1]
    y_final = (clist[i + 1])[1]

    x_dist = (x_final - x_initial)
    y_dist = (y_final - y_initial)

    if x_initial == 0:
        r_slope = (y_final)/(x_final)
    else:
        r_slope = y_initial / x_initial

    ry = r_slope * x_final

    ry_dist = (ry - y_initial)

    theta = getAngle(x_dist, y_dist, x_dist, ry_dist)

    theta_list.append(theta)

print(len(theta_list))
print(len(radial_length))
print(theta_list)

plt.figure(num=0, dpi=120)
plt.plot(radial_length, theta_list)
plt.grid(True)


pi = unicodedata.lookup("GREEK SMALL LETTER PI")
th = unicodedata.lookup("GREEK SMALL LETTER THETA")
x_ticks = [0, pi + "/2", pi, "3" + pi + "/2", "2" + pi]
plt.xlabel("Distance from center (0 -> 2" + pi + ")")
plt.ylabel(th + " (degrees)")

plt.show()
