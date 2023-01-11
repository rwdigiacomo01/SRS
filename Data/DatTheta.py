import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt(r'C:\Users\reece\Downloads\r_psp_hci_1s_orb1')

t = []
x = []
y = []
z = []

i = 0
while i < len(data):
    if(math.isnan((data[i])[1])) == False:
        t.append((data[i])[0])
        x.append((data[i])[1])
        y.append((data[i])[2])
        z.append((data[i])[3])

    i = i + 1000


def getAngle(xdist, ydist, rxdist, rydist):
    vector_a = float(np.sqrt(((xdist ** 2) + (ydist ** 2))))
    vector_b = float(np.sqrt(((rxdist ** 2) + (rydist ** 2))))
    dot_prod = float((xdist * rxdist) + (ydist * rydist))
    ratio = abs(dot_prod / (vector_a * vector_b))
    theta = math.acos(ratio) * (360 / (2 * np.pi))
    return float(theta)

radial = []
theta = []
i = 0

while i < len(t):
    distance = np.sqrt(((x[i]/ (1.496*10**8))**2) + (y[i]/ (1.496*10**8))**2)
    radial.append(distance)

    if i == len(t)-1:
        theta.append(theta[-1])
        break

    xdist = x[i+1] - x[i]
    ydist = y[i+1] - y[i]

    rslope = y[i]/x[i]

    ry = rslope * y[i+1]
    rydist = ry - y[i]

    theta.append(getAngle(xdist, ydist, xdist, rydist))

    i+=1

print(radial)
print(theta)

plt.figure(num=0, dpi=120)
plt.plot(radial, theta)
plt.grid(True)


#pi = unicodedata.lookup("GREEK SMALL LETTER PI")
# th = unicodedata.lookup("GREEK SMALL LETTER THETA")
#x_ticks = [0, pi + "/2", pi, "3" + pi + "/2", "2" + pi]
#plt.xlabel("Distance from center (0 -> 2" + pi + ")")
#plt.ylabel(th + " (degrees)")

plt.show()