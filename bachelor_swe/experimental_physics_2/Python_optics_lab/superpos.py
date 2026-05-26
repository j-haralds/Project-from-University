from turtle import Vec2D
from numpy import *
import matplotlib.pyplot as plt


# LaTeX font
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'



fig, axs = plt.subplots(3, 1)


t = linspace(0,5*pi,500)
v1 =sin(t)
v2 = v1
plt.figure(1)
for i in range(0,3):
    axs[i].set_xticks([])
    axs[i].set_yticks([])
    axs[i].set_ylim([-3,3])
axs[0].plot(t,v1,linewidth=2,color='tab:blue')
axs[1].plot(t,v2,linewidth=2,color='tab:blue')
axs[2].plot(t,v1+v2,linewidth=2,color='tab:blue')

plt.figure(2)
fig, axs = plt.subplots(3, 1)
v2 = -v1
for i in range(0,3):
    axs[i].set_xticks([])
    axs[i].set_yticks([])
    axs[i].set_ylim([-3,3])

axs[0].plot(t,v1,linewidth=2,color='tab:blue')
axs[1].plot(t,v2,linewidth=2,color='tab:blue')
axs[2].plot(t,v1+v2,linewidth=2,color='tab:blue')

plt.show()

