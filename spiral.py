import numpy as np
import matplotlib.pyplot as plt
import unicodedata

a = 1
theta = np.linspace(0, 2*np.pi, 1000)
r = a * theta

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(num=0, dpi=120)
plt.polar(theta, r)
plt.grid(True)

pi = unicodedata.lookup("GREEK SMALL LETTER PI")
th = unicodedata.lookup("GREEK SMALL LETTER THETA")

plt.title("Archimedean Spiral [r = a" + th + "]")


plt.show()

