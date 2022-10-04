import numpy as np
import matplotlib.pyplot as plt
import math

tlist = np.linspace(1, 100, num=1000)
radius = 1

def x(t):
    return (radius / (2 * np.pi) * t) * np.cos(t)

def y(t):
    return (radius / (2 * np.pi) * t) * np.sin(t)

def getAngle(xdist, ydist, rxdist, rydist):
    vector_a = float(np.sqrt(((xdist ** 2) + (ydist ** 2))))
    vector_b = float(np.sqrt(((rxdist ** 2) + (rydist ** 2))))
    dot_prod = float((xdist * rxdist) + (ydist * rydist))
    ratio = dot_prod / (vector_a * vector_b)
    theta = math.acos(ratio) * (360 / (2 * np.pi))

    return theta

i = 0
ystr = 0
xstr = 0

while i <= 100:
    xcord = x(i)
    ycord = y(i)

    i = i+0.1
    xstr = xcord
    ystr = ycord
