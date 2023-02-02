import numpy as np
import matplotlib.pyplot as plt
import math

data2 = np.loadtxt(r'C:\Users\reece\Downloads\r_psp_hci_1s_orb1')
data = np.loadtxt(r'C:\Users\reece\Downloads\B_1s_orb1')
# data = np.loadtxt(r'E:\Copy of B_1s_orb1')
# data2 = np.loadtxt(r'E:\Copy of r_psp_hci_1s_orb1')

Bt = []
r = []
t = []
n = []

Rt = []
x = []
y = []
z = []

i = 0
while i < len(data):
    if not (math.isnan((data[i])[1])):
        Bt.append((data[i])[0])
        r.append((data[i])[1])
        t.append((data[i])[2])
        n.append((data[i])[3])

    i = i + 1
i = 0
while i < len(data2):
    if not (math.isnan((data2[i])[1])):
        Rt.append((data2[i])[0])
        x.append((data2[i])[1])
        y.append((data2[i])[2])
        z.append((data2[i])[3])

    i = i + 1


def getMagnitude(x1, y1, z1):
    magnitude = np.sqrt((x1 ** 2) + (y1 ** 2) + (z1 ** 2))
    return magnitude


def getAngle(Br, magnitude):
    temp = (math.acos((Br / magnitude)) * (180 / np.pi))

    return temp


radial = []
theta = []
i = 0
while i < len(Rt):
    radial.append([Rt[i], getMagnitude(x[i], y[i], z[i])])
    i += 1
i = 0
while i < len(Bt):

    if i == len(Bt) - 1:
        theta.append(theta[-1])
        break

    theta.append([Bt[i], getAngle(r[i], getMagnitude(r[i], t[i], n[i]))])

    i += 1

angle = []
mag = []
tcount = 1538352000
i = 0
p = 0
bp = 0

while i < 1464:
    counter = 0
    angletemp = []
    magtemp = []
    tcount += 36000
    while counter < 36000 and (tcount <= 1543622400):

        if bp < len(theta) and (theta[bp])[0] < tcount:
            angletemp.append((theta[bp])[1])
            bp += 1
        if p < len(radial) and (radial[p])[0] < tcount:
            magtemp.append((radial[p])[1])
            p += 1
        counter += 1

    if (len(angletemp) != 0) and (len(magtemp) != 0):

        h = 0
        number = 0
        while h < len(angletemp):
            number += angletemp[h]
            h += 1
        angle.append(number / len(angletemp))

        h = 0
        number = 0
        while h < len(magtemp):
            number += magtemp[h]
            h += 1
        mag.append(number / len(magtemp))
    # else:
    #     bavg.append(0)
    #     ravg.append(0)

    i += 1
print(len(mag))
print(mag)
print(angle)
print(len(angle))
plt.figure(num=0, dpi=120)
plt.scatter(mag, angle)
plt.grid(True)

# pi = unicodedata.lookup("GREEK SMALL LETTER PI")
# th = unicodedata.lookup("GREEK SMALL LETTER THETA")
# x_ticks = [0, pi + "/2", pi, "3" + pi + "/2", "2" + pi]
# plt.xlabel("Distance from center (0 -> 2" + pi + ")")
# plt.ylabel(th + " (degrees)")

plt.show()
