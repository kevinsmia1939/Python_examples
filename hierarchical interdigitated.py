import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.rcParams['figure.dpi'] = 200
mpl.rcParams['xtick.labelsize'] = 6
mpl.rcParams['ytick.labelsize'] = 6
mpl.rcParams['axes.labelsize'] = 6
mpl.rcParams['axes.facecolor'] = 'black'

# Square hiearchical interdigitated flow field

block_height_num = 2 #number of fins = block_height_num - 1 
block_length_num = 1
unit_height1 = 2
fin_thinness = 0  # 0 for equal, >0 for thinner <0 for thicker

const = 2.63157894737

start_x = const
start_y = 5
fin_length = start_x + const
gap1 = fin_length + const
gap2 = const

# Calculate dimention
height = start_y*2+unit_height1*(block_height_num-1)*2
print(height,"height")
width = (gap2*4)*(block_length_num-1)+start_x+fin_length
print(width,"width")

a = np.arange(0,block_height_num*2,1)
x = []
for i in a:
    x.append(start_x)
    x.append(start_x)
    x.append(fin_length)
    x.append(fin_length)
y = []
for k in a:
    if k%2 == 0:
        y.append(k*unit_height1)
        y.append(k*unit_height1)
    else:
        y.append(k*unit_height1+fin_thinness)
        y.append(k*unit_height1+fin_thinness)
    
# print(y)
x = x[1:]   
y = y[:-3] #Cut unneeded points  
x = x[:len(y)]
x = x[1:] # Remove first point
y = y[1:]
x = np.array(x)
y = np.array(y)

flip_x = -np.flip(x)
flip_y = np.flip(y)

field_unit_x = np.append(x,flip_x+fin_length+gap1)
field_unit_y = np.append(y,flip_y)

full_x = np.array([])
full_y = np.array([])
for i in np.arange(0,block_length_num,1):
    # print(i)
    full_x = np.append(full_x,field_unit_x+i*gap2*4)
    full_y = np.append(full_y,field_unit_y)
    
# Add the tail to beginning
full_x = np.append(0,full_x)
full_y = np.append(0,full_y)

# To make the end at the opposite diagonal, we need to cut off last half part
full_x = full_x[:-(block_height_num*2*2-4)]
full_y = full_y[:-(block_height_num*2*2-4)]
# Add outlet hole
full_x = np.append(full_x,full_x[-1]+fin_length)
full_y = np.append(full_y,full_y[-1])
full_y = full_y + start_y
# The pattern does not fit in square when all channel is equal to 1.
# compress2square = (max(full_x)-2)/y[-1]

tot_x_length = max(full_x)-min(full_x)
tot_y_length = max(full_y)-min(full_y)+start_y*2

if tot_y_length != tot_x_length:
    print("NOT SQUARE")
    print(tot_y_length, "Height")
    print(tot_x_length, "Width")
else:
    print("GOOD SQUARE")
    print(tot_y_length, "Height")
    print(tot_x_length, "Width")

plt.plot(full_x,full_y,"-o",markersize=0.5,linewidth=2,color="blue")
# plt.xlim(0,max(full_x))
# plt.ylim(0,max(full_x))
plt.xlim(0,50)
plt.ylim(0,50)
plt.gca().set_aspect('equal')
# plt.facecolor('xkcd:salmon')
# ax.set_facecolor((1.0, 0.47, 0.42))
plt.show()

points = []
for i in np.arange(0,len(full_x),1):
    points.append((full_x[i],full_y[i], 0))
    
print(points)