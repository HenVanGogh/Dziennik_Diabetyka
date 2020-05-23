#!/usr/bin/python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib import style

style.use("bmh")
x = [5,8,10]
y = [12,16,6]

plt.plot(x, y, 'g', label="line", linewidth=5)

plt.title("Wykres")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.legend()
plt.grid(True, color='k')
plt.show()
