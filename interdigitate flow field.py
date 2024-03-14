import numpy as np
from scipy import signal
import matplotlib as mpl
from matplotlib import pyplot as plt
# mpl.rcParams['figure.dpi'] = 200
mpl.rcParams['xtick.labelsize'] = 6
mpl.rcParams['ytick.labelsize'] = 6
mpl.rcParams['axes.labelsize'] = 6
mpl.rcParams['axes.facecolor'] = 'blue'

t = np.linspace(0, 1, 300, endpoint=False)
x = signal.square(1 * np.pi * 5 * t)

plt.plot(t, x,'-o',color="black",linewidth=1,markersize=1.1)
#
# plt.ylim(-2, 2)
plt.gca().set_aspect('equal')
plt.show()