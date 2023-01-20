import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt(r'C:\Users\reece\Downloads\r_psp_hci_1s_orb1')
data2 = np.loadtxt(r'C:\Users\reece\Downloads\B_1s_orb1')
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
    if(math.isnan((data[i])[1])) == False:
        Bt.append((data[i])[0])
        r.append((data[i])[1])
        t.append((data[i])[2])
        n.append((data[i])[3])

    i = i + 1
i = 0
while i < len(data2):
    if(math.isnan((data2[i])[1])) == False:
        Rt.append((data2[i])[0])
        x.append((data2[i])[1])
        y.append((data2[i])[2])
        z.append((data2[i])[3])

    i = i + 1


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
while i < len(Rt):
    distance = np.sqrt(((x[i]/ (1.496*10**8))**2) + (y[i]/ (1.496*10**8))**2)
    radial.append([Rt[i], distance])
    i += 1
i = 0
while i < len(Bt):

    if i == len(Bt)-1:
        theta.append(theta[-1])
        break

    xdist = r[i+1] - r[i]
    ydist = t[i+1] - t[i]

    rslope = t[i]/r[i]

    ry = rslope * t[i+1]
    rydist = ry - t[i]

    theta.append([Bt[i], getAngle(xdist, ydist, xdist, rydist)])

    i+=1

angle = []
mag = []
tcount = 1538352000
i = 0
p = 0
bp = 0

while i < 1464:
    counter = 0
    btemp = []
    rtemp = []
    tcount += 3600
    while counter < 3600 and (tcount <= 1543622400):

        if bp < len(theta) and (theta[bp])[0] < tcount:
            btemp.append((theta[bp])[1])
            bp += 1
        if p < len(radial) and (radial[p])[0] < tcount:
            rtemp.append((radial[p])[1])
            p += 1
        counter += 1


    if (len(btemp) != 0) and (len(rtemp) != 0):
        h = 0
        number = 0
        while h < len(btemp):
            number += btemp[h];
            h+= 1
        angle.append(number / len(btemp))
        h = 0
        number = 0
        while h < len(rtemp):
            number += rtemp[h];
            h += 1
        mag.append(number / len(rtemp))
    # else:
    #     bavg.append(0)
    #     ravg.append(0)

    i += 1
print(mag)
print(angle)
plt.figure(num=0, dpi=120)
plt.plot(mag, angle)
plt.grid(True)


#pi = unicodedata.lookup("GREEK SMALL LETTER PI")
# th = unicodedata.lookup("GREEK SMALL LETTER THETA")
#x_ticks = [0, pi + "/2", pi, "3" + pi + "/2", "2" + pi]
#plt.xlabel("Distance from center (0 -> 2" + pi + ")")
#plt.ylabel(th + " (degrees)")

plt.show()