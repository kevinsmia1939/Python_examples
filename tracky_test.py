import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience
import pims
import trackpy as tp

mpl.rc('figure',  figsize=(10, 5))
mpl.rc('image', cmap='gray')

frames = pims.as_grey(pims.open('30_rpm/*.jpg'))

plt.imshow(frames[0]) #show first frame

tp.quiet()
f = tp.batch(frames[:300], diameter=11, minmass=20, invert=True) #algorithm looks for bright features; since the features in this set of images are dark, we set invert=True

t = tp.link(f, 5, memory=3)
t1 = tp.filter_stubs(t, 25)

# tp.mass_size(t1.groupby('particle').mean())

t2 = t1[((t1['mass'] > 50) & (t1['size'] < 2.6) & (t1['ecc'] < 0.3))] #low mass, or that are especially large or non-circular (eccentric)

# plt.figure()
tp.annotate(t2[t2['frame'] == 0], frames[0]);

# plt.figure()
# tp.plot_traj(t2);

d = tp.compute_drift(t2)

d.plot(y='y')
plt.show()

# print(move_y)

# tp.annotate(f, frames[0])

frame_time = d.index.tolist() #Get velocity by differentiate in y direction pixel/index
move_y = d['y']
diff_y = np.gradient(move_y,frame_time) 
plt.plot(frame_time,diff_y)
plt.show()
