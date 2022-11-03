import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

data = np.loadtxt(r'C:\Users\reece\Downloads\B_1s_orb1')


t = []
x = []
y = []
z = []

i = 456839
print((data[456839])[2])
while i < 457839:
    t.append((data[i])[0])
    x.append((data[i])[1])
    y.append((data[i])[2])
    z.append((data[i])[3])
    i+=1

#i = 0

#while i < len(data):
   # t.append((data[i])[0])
   # x.append((data[i])[1])
   # y.append((data[i])[2])
   # z.append((data[i])[3])
   # i+=1

#i = 0
#spot = 0
#while i < len(data):
   # if(str(x[i]) != "nan"):
   #     spot = i
   #     print(spot)
   #     break
   # else:
   #     i+=1

ax = plt.axes(projection="3d")
ax.scatter(x, y, z)

plt.show()
