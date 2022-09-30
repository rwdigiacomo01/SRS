import numpy as np
import matplotlib.pyplot as plt
import math

x1 = float(input("Record x coordinate of initial vector point: "))
y1 = float(input("Record y coordinate of initial vector point: "))
x2 = float(input("Record x coordinate of second vector point: "))
y2 = float(input("Record y coordinate of second vector point: "))
x3 = float(input("Record x coordinate of radial vector point: "))
y3 = float(input("Record y coordinate of radial vector point: "))

l = float(np.sqrt(( ((x2-x1)**2) + ((y2-y1)**2) )))
print(l)
r = float(np.sqrt(( ((x3-x1)**2) + ((y3-y1)**2) )))
print(r)
d = float((x2*x3) + (y2*y3))
print(d)
p = (d)/(l*r)
print(p)
theta = math.acos(p) * (360/(2*np.pi))

print(theta)