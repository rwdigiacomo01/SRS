import numpy as np
import matplotlib.pyplot as plt
import math


def getAngle(xdist, ydist, rxdist, rydist):
    vector_a = float(np.sqrt(((xdist ** 2) + (ydist ** 2))))
    vector_b = float(np.sqrt(((rxdist ** 2) + (rydist ** 2))))
    dot_prod = float((xdist * rxdist) + (ydist * rydist))
    ratio = dot_prod / (vector_a * vector_b)
    theta = math.acos(ratio) * (360 / (2 * np.pi))

    return theta

