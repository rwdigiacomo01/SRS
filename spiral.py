import numpy as np
import matplotlib.pyplot as plt
import unicodedata

radius = 2*np.pi
tlist = np.linspace(0, (2 * np.pi), num=1000)


def x(t):
    return (radius / (2 * np.pi) * t) * np.cos(t)


def y(t):
    return (radius / (2 * np.pi) * t) * np.sin(t)

xlist = x(tlist)
ylist = y(tlist)

# This commented out section adds an Archimedean Spiral in the other direction
# Creating a Parker Spiral
# def c(t):
#    return (-1*radius/(2*np.pi) * t) * np.cos(t)
# def v(t):
#    return (-1*radius/(2*np.pi) *t) * np.sin(t)

# clist = c(tlist)
# vlist = v(tlist)

plt.figure(num=0, dpi=120)
plt.plot(xlist, ylist)
# plt.plot(clist, vlist)
plt.grid(True)

pi = unicodedata.lookup("GREEK SMALL LETTER PI")

plt.xlabel("((r/2" + pi + ")*t)*cos(t)")
plt.ylabel("((r/2" + pi + ")*t)*sin(t)")
plt.title("Archimedean Spiral")
plt.xlim(-2*np.pi, 2*np.pi)
plt.ylim(-2*np.pi, 2*np.pi)

plt.show()

