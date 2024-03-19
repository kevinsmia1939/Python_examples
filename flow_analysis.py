import numpy as np
import pandas as pd
from pyexcel_ods import get_data
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
# from matplotlib.patches import Patch


mpl.rcParams['figure.dpi'] = 150
plt.rcParams['figure.figsize'] = (10, 6)
mpl.rcParams['font.family'] = 'sans'
mpl.rcParams['font.serif'] = 'Liberation San'
mpl.rcParams['axes.titlesize'] = 16
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14

raw_data_ls = ["5mlmin","10mlmin","20mlmin","40mlmin"]
raw_data_damp_ls = ["5mlmin_500mldamp","10mlmin_500mldamp","20mlmin_500mldamp","40mlmin_500mldamp"]
avg_vel_ls = []
flow_label = ["5 ml/min","10 ml/min","20 ml/min","40 ml/min","5 ml/min","10 ml/min","20 ml/min","40 ml/min"]
ln_color = ["blue","orange","limegreen","tomato"]

fig, ax1 = plt.subplots()

df_append = pd.DataFrame()
for i in raw_data_ls:
    ods_data = get_data(str("/home/kevin/Desktop/UAntwerp/PhD_thesis/Flow_profile_test/PTFE-methylene-blue/")+i+str(".ods"))
    first_sheet_name = list(ods_data.keys())[0]
    df = pd.DataFrame(ods_data[first_sheet_name],columns=ods_data[first_sheet_name][1])
    df = df.iloc[2:]
    velocity = np.gradient(df['x'],df['t']) #cm/s
    df['x'] = velocity
    new_header = [str(i)+'t', str(i)+'v']
    df.columns = new_header
    df_append = df_append.assign(**df) #dictionary unpacking or keyword argument unpacking.

vel_avg_ls = []
for i in np.arange(0,df_append.shape[1]/2):
    time = df_append[df_append.columns[int(i*2)]]
    vel = df_append[df_append.columns[int(i*2)+1]]
    ax1.plot(time,vel*0.017694*60,label=flow_label[int(i)],linewidth=2,color=ln_color[int(i)])
    vel = vel[~np.isnan(vel)]
    vel_avg = np.average(vel)
    vel_avg_ls.append(vel_avg)

flow_rate = np.array([5,10,20,40])
# area = flow_rate/vel_avg_ls/60 #cm2



df_append = pd.DataFrame()
for i in raw_data_damp_ls:
    ods_data = get_data(str("/home/kevin/Desktop/UAntwerp/PhD_thesis/Flow_profile_test/PTFE-methylene-blue/")+i+str(".ods"))
    first_sheet_name = list(ods_data.keys())[0]
    df = pd.DataFrame(ods_data[first_sheet_name],columns=ods_data[first_sheet_name][1])
    df = df.iloc[2:]
    velocity = np.gradient(df['x'],df['t']) #cm/s
    df['x'] = velocity
    new_header = [str(i)+'t', str(i)+'v']
    df.columns = new_header
    df_append = df_append.assign(**df) #dictionary unpacking or keyword argument unpacking.

vel_avg_damp_ls = []
area_ls = [0.03988591, 0.01971711, 0.02086847, 0.02191459]
for i in np.arange(0,df_append.shape[1]/2):
    time = df_append[df_append.columns[int(i*2)]]
    vel = df_append[df_append.columns[int(i*2)+1]]
    ax1.plot(time,vel*area_ls[int(i)]*60,label=flow_label[int(i)],linewidth=2,linestyle="--",color=ln_color[int(i)])
    vel = vel[~np.isnan(vel)]
    vel_avg_damp = np.average(vel)
    vel_avg_damp_ls.append(vel_avg_damp)

vel*0.017694*60

legend_elements = [Line2D([0], [0], color='None', linestyle="None", label="No damper"),
                   Line2D([0], [0], color='blue', linestyle="-", label="5 ml/min"),
                   Line2D([0], [0], color='orange', linestyle="-", label="10 ml/min"),
                   Line2D([0], [0], color='limegreen', linestyle="-", label="20 ml/min"),
                   Line2D([0], [0], color='tomato', linestyle="-", label="40 ml/min"),
                   Line2D([0], [0], color='None', linestyle="None", label="500 ml damper"),
                   Line2D([0], [0], color='blue', linestyle="--", label="5 ml/min"),
                   Line2D([0], [0], color='orange', linestyle="--", label="10 ml/min"),
                   Line2D([0], [0], color='limegreen', linestyle="--", label="20 ml/min"),
                   Line2D([0], [0], color='tomato', linestyle="--", label="40 ml/min"),
                   ]

area = flow_rate/vel_avg_damp_ls/60 #cm2
print(np.average(area))
ax1.set_xlim(0,1.2)
ax1.set_ylim(-30,90)

ax2 = ax1.twinx()
ax2.set_ylim(1,3)
ax2.set_ylabel("Superficial velocity in electrode  ")
ax1.set_ylabel("Flow rate / ml/min")
plt.xlabel("Time / s")
plt.legend(handles=legend_elements,ncol=2,frameon=False)    

# print(np.average(area)) #cm2
