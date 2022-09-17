import numpy as np
import matplotlib.pyplot as plt
import unicodedata
radius = 1
tlist = np.linspace(0, 20, num=1000)

def x(t):
    return (radius/(2*np.pi) * t) * np.cos(t)
def y(t):
    return (radius/(2*np.pi) *t) * np.sin(t)

xlist = x(tlist)
ylist = y(tlist)

plt.figure(num=0, dpi=120)
plt.plot(xlist,ylist)
plt.grid(True)

pi = unicodedata.lookup("GREEK SMALL LETTER PI")

plt.xlabel("((r/2"+pi+")*t)*cos(t)")
plt.ylabel("((r/2"+pi+")*t)*sin(t)")
plt.title("Archimedean Spiral")

plt.show()