import numpy as np
import matplotlib.pyplot as plt
import math

import unicodedata

data2 = np.loadtxt(r'C:\Users\reece\Downloads\R_psp_hci_orb1_nonan.dat')
data = np.loadtxt(r'C:\Users\reece\Downloads\B_rtn_orb1_nonan.dat')
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
    Bt.append((data[i])[0])
    r.append((data[i])[1])
    t.append((data[i])[2])
    n.append((data[i])[3])

    i = i + 1
i = 0
while i < len(data2):

    Rt.append((data2[i])[0])
    x.append((data2[i])[1] / (1.496*10**8))
    y.append((data2[i])[2] / (1.496*10**8))
    z.append((data2[i])[3] / (1.496*10**8))

    i = i + 1


def getMagnitude(x1, y1, z1):
    magnitude = np.sqrt((x1 ** 2) + (y1 ** 2) + (z1 ** 2))
    return magnitude
# Uses Distance formula to calculate distance from PSP to Sun


def getAngle(Br, magnitude):
    temp = (math.acos((Br / magnitude)) * (180 / np.pi))
    return temp
# Uses Dot Product to calculate the angle between the magnetic field and PSP through


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


def sort_by_distance(e):
    return e[0]


# Combine radial and theta into a single list via identical timestamps
# use combined_list.sort(key=sort_by_distance), automatically sorts ascending
# sort through list averaging into .01 AU chunks, check, add to avg / average out compiled then move onto next range
# graphically display using a histogram with relevant title

i = 0
combo = []

while i < len(radial):
    combo.append([(radial[i])[1], (theta[i])[1]])
    i += 1

combo.sort(key=sort_by_distance)
angle = []
mag = []

temp2 = []
range_val = 0.01
i = 0

while i < len(combo):

    if (combo[i])[0] < range_val:
        temp2.append((combo[i])[1])
        i += 1

    if i >= len(combo):
        break

    if (combo[i])[0] >= range_val and len(temp2) != 0:
        avg = 0
        b = 0
        while b < len(temp2):
            avg = avg + temp2[b]
            b += 1
        mag.append(range_val)
        angle.append(avg/len(temp2))
        temp2 = []
        range_val += 0.01

    elif (combo[i])[0] >= range_val and len(temp2) == 0:
        range_val += 0.01


print(mag)
print(angle)
# Adjust t-count and i in the greater while loop since there are no longer any gaps in data


# The code below averages the angle based on time
# tcount = 1538352000
# i = 0
# p = 0
# bp = 0
#
# while i < 1464:
#     counter = 0
#     angletemp = []
#     magtemp = []
#     tcount += 36000
#     while counter < 36000 and (tcount <= 1543622400):
#
#         if bp < len(theta) and (theta[bp])[0] < tcount:
#             angletemp.append((theta[bp])[1])
#             bp += 1
#         if p < len(radial) and (radial[p])[0] < tcount:
#             magtemp.append((radial[p])[1])
#             p += 1
#         counter += 1
#
#     if (len(angletemp) != 0) and (len(magtemp) != 0):
#
#         h = 0
#         number = 0
#         while h < len(angletemp):
#             number += angletemp[h]
#             h += 1
#         angle.append(number / len(angletemp))
#
#         h = 0
#         number = 0
#         while h < len(magtemp):
#             number += magtemp[h]
#             h += 1
#         mag.append(number / len(magtemp))
#     # else:
#     #     bavg.append(0)
#     #     ravg.append(0)
#
#     i += 1


# Graphically displays via scatter plot
plt.figure(num=0, dpi=120)
plt.scatter(mag, angle)
plt.grid(True)
plt.ylim(0, 180)
th = unicodedata.lookup("GREEK SMALL LETTER THETA")
plt.title("Angle of the Sun's Magnetic Field Within the Inner Heliosphere")
plt.xlabel("Distance from the Center of the Sun [AU]")
plt.ylabel("Magnetic Field Angel [" + th + "]")
pi = unicodedata.lookup("GREEK SMALL LETTER PI")

# x_ticks = [0, pi + "/2", pi, "3" + pi + "/2", "2" + pi]
# plt.xlabel("Distance from center (0 -> 2" + pi + ")")
# plt.ylabel(th + " (degrees)")

plt.show()
