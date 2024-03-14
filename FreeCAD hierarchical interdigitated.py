import FreeCAD as App
import Part
import numpy as np
import Sketcher

doc = App.activeDocument()
# Create a new sketch in the XY plane
sketch = doc.addObject('Sketcher::SketchObject', 'Flow Field')
doc.recompute()

block_height_num = 39 #number of fins = block_height_num - 1 
block_length_num = 2
unit_height = 5
a = np.arange(0,block_height_num*2,1)
x = []

start_x = 5
start_y = 10
fin_length = start_x + 10
gap1 = fin_length + 10
gap2 = 10

for i in a:
    x.append(start_x)
    x.append(start_x)
    x.append(fin_length)
    x.append(fin_length)
y = []
for k in a:
    y.append(k*unit_height)
    y.append(k*unit_height)
    
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
