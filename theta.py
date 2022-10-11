import numpy as np
import matplotlib.pyplot as plt
import math

radius = 1
tlist = np.linspace(0, (2 * np.pi), num=1000)

def x(t):
    return (radius / (2 * np.pi) * t) * np.cos(t)


def y(t):
    return (radius / (2 * np.pi) * t) * np.sin(t)


xlist = x(tlist)
ylist = y(tlist)

def getAngle(xdist, ydist, rxdist, rydist):
    vector_a = float(np.sqrt(((xdist ** 2) + (ydist ** 2))))
    vector_b = float(np.sqrt(((rxdist ** 2) + (rydist ** 2))))
    dot_prod = float((xdist * rxdist) + (ydist * rydist))
    ratio = dot_prod / (vector_a * vector_b)
    theta = math.acos(ratio) * (360 / (2 * np.pi))

    return theta

for i in range(len(xlist)):
    magnitude = np.sqrt(((xlist[i+1] - xlist[i])**2) + ((ylist[i+1] - ylist[i])**2))
    rslope = ylist/xlist
    ry = rslope*xlist[i+1]
    rmagnitude = np.sqrt(((xlist[i + 1] - xlist[i]) ** 2) + ((ry - ylist[i]) ** 2))




