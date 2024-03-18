import FreeCAD as App
import Part
import numpy as np
import Sketcher

doc = App.activeDocument()
# Create a new sketch in the XY plane
sketch = doc.addObject('Sketcher::SketchObject', 'Flow Field')
doc.recompute()

block_height_num = 2 #number of fins = block_height_num - 1 
block_length_num = 1
unit_height1 = 3.333333333333333
unit_height2 = 3.333333333333333

const = 2.6315789477

start_x = const
start_y = 5
fin_length = start_x + const
gap1 = fin_length + const
gap2 = const

a = np.arange(0,block_height_num*2,1)
x = []

for i in a:
    x.append(start_x)
    x.append(start_x)
    x.append(fin_length)
    x.append(fin_length)
y = []
for k in a:
    y.append(k*unit_height1)
    y.append(k*unit_height2)
    
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

#Create vector point
points = []
for i in np.arange(0,len(full_x),1):
    points.append(App.Vector(full_x[i],full_y[i], 0))

print(points)
# Add the points to the sketch
for i, point in enumerate(points):
    sketch.addGeometry(Part.LineSegment(points[i - 1], point), False)
    
# No need to add constraint to do additive pipe
# for i in range(1, len(points)):
#     constraint = sketch.addConstraint(Sketcher.Constraint("Coincident", i-1, 2, i, 1))
# doc.recompute()

# for i in range(1, len(points)-1):
#     fillet = sketch.fillet(i,2,0.2,True,True)
# doc.recompute()

# Save the document
# doc.saveAs("path/to/save/interdigitated.FCStd")
