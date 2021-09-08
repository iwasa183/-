# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,3,400)

def x(n):
	return 4/(n*np.pi)*np.sin(2*np.pi*n*t)


def f(n):
	fn = np.zeros(shape=(t.shape[0],))
	for i in range(1,n,2):
		fn += x(i)
	return fn

num=19
plt.title("FourierSeriesExpansion")
plt.plot(t, x(1), color=(1.0,0.0,0.0), linewidth=1.0, label="a1")
plt.plot(t, x(3), color=(0.0,1.0,0.0), linewidth=1.0, label="a3")
plt.plot(t, x(5), color=(0.0,0.0,1.0), linewidth=1.0, label="a5")
plt.plot(t, f(num), color=(1.0,0.0,1.0), linewidth=1.0, label="n="+str(num))
plt.legend()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.show()