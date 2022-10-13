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
    print(vector_a)
    vector_b = float(np.sqrt(((rxdist ** 2) + (rydist ** 2))))
    print(vector_b)
    dot_prod = float((xdist * rxdist) + (ydist * rydist))
    print(dot_prod)
    ratio = min(1, dot_prod / (vector_a * vector_b))
    print(ratio)
    theta = math.acos(ratio) * (360 / (2 * np.pi))

    return float(theta)
print(tlist[0])
print (xlist[0])
print (ylist[0])
for i in range(len(xlist)-1):
    magnitude = np.sqrt(((xlist[i+1] - xlist[i])**2) + ((ylist[i+1] - ylist[i])**2))
    rslope = float(ylist[i]/xlist[i])
    if xlist[i] == 0:
        print(rslope)
    ry = rslope*xlist[i+1]
    rmagnitude = np.sqrt(((xlist[i + 1] - xlist[i]) ** 2) + ((ry - ylist[i]) ** 2))

    xdist = xlist[i+1] - xlist[i]
    ydist = ylist[i+1] - ylist[i]
    rxdist = xdist
    rydist = ry - ylist[i]
    # print("The Angle between the Archimedean vector ("+ str(magnitude)+") and the Radial vector ("+str(rmagnitude)+") is: "+ str(getAngle(xdist, ydist, rxdist, rydist)) + " degrees.")





