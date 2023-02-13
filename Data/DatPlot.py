import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#data = np.loadtxt(r'C:\Users\reece\Downloads\r_psp_hci_1s_orb1')
#data2 = np.loadtxt(r'C:\Users\reece\Downloads\B_1s_orb1')
data2 = np.loadtxt(r'D:\B_rtn_orb1_nonan.dat')
data = np.loadtxt(r'D:\R_psp_hci_orb1_nonan.dat')

t = []
x = []
y = []
z = []

i = 0

while i < 4585001:
   t.append((data[i])[0])
   x.append((data[i])[1]/ (1.496*10**8))
   y.append((data[i])[2]/ (1.496*10**8))
   z.append((data[i])[3]/ (1.496*10**8))
   i+=500

print(x)
# i = 0
# #print(len(data))
# while i < len(data):
#     t.append((data[i])[0])
#     x.append((data[i])[1])
#     y.append((data[i])[2])
#     z.append((data[i])[3])
#     i+=1

# i = 0
# spot = 0
# while i < len(data):
#     if(str(x[i]) != "nan"):
#         spot = i
#         print(spot)
#         break
#     else:
#         i+=1
# Used to find where to begin count, where values are no longer NaN

ax = plt.axes(projection="3d")

ax.scatter(x, y, z)

ax.set_xlim(-.6, .6)
ax.set_ylim(-.6, .6)
ax.set_zlim(-.6, .6)

ax.set_title("")

plt.show()
