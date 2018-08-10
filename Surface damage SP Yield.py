#This code shows SP yield on cathode surface on a 3d Surface plot


from mpl_toolkits.mplot3d import Axes3D
from scipy.constants import *
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
from numpy import genfromtxt
from traitlets.traitlets import add_article

import time
start_time = time.time()


from pylab import figure

#data= genfromtxt('SPUTTER_10tab_5.txt',delimiter='',dtype=None, names=True)
data= genfromtxt('ions_22deg_18apt_0.6off_4.3r_scttgap_result.txt',delimiter='',dtype=None, names=True)

e0_p=938.27e6

fig = plt.figure()
ax = fig.gca(projection='3d')

xx=np.array(data['x'])
yy=np.array(data['y'])
bz=np.array(data['Bz'])

Ez = e0_p*((1-bz**2)**(-0.5)-1)
Ezk = Ez/1000        # ion Energy in KeV

print("len Ezk:", len(Ezk))

SY = np.arange(0, 24003 , 1 )   # SP. Yield, will be edited later

#print("SY:", SY)

#-------This part mimic SP. Yield with respect to ion Energy[KeV] --------
for i in range(24003):
    if 0.2<Ezk[i]<=1.5:
        SY[i]=13*(Ezk[i]-0.2)
    elif 1.5<Ezk[i]<=351:
        SY[i]=1+18*math.exp(-0.05*Ezk[i])
    else:
        SY[i]=0

#---- this variable converstion is not necessary--------
x= xx
y= yy
t = SY

#---- Creating Mesh Size-------
#-- one of the problem of matplotlib is it cant handle 3d plot efficiently----
mesh = 0.001        # finer mesh crash my PC

# -- Gird pints are created wth mesh value----
X = np.arange(-0.015, 0.015+mesh , mesh )
Y = np.arange(-0.015, 0.015+mesh, mesh)

#--- This XX, and YY is used later  for loop calculation
XX=X
YY=Y

print("number of XX points:", len(XX))
print("number of YY points:", len(YY))

#---- we used X,Y for grid, and XX, YY are left for loop calculation
X, Y = np.meshgrid(X, Y)

#---this is funny, but i didnt find any good way right now
R= (X**2 + Y**2)*0

print("##-- Code is Running, Please be Patient--##")

#--- this part will compare every point of grid, then it will
#-   find if any ion is in the grid or not, if ion is located
#-   in the grid, then SP. Yield corresponding to that ion-
#-   energy is added on the grid point.
#----- For more than one ion in a grid point, their SP. Yield
#-     is added simply
# ---- Not sure, this part is 100 percent correct, Please check
for i in range(len(XX)):
    for j in range(len(YY)):
        for k in range(24003):
            if abs(XX[i]-x[k])<(mesh/2) and abs(YY[j]-y[k])<(mesh/2):
                R[i,j]= R[i,j] + t[k]
            else:
                R[i,j]= R[i,j]


Z = R

# it printes total elapsed time in seconds
print("--- %s seconds ---" % (time.time() - start_time))

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=1, antialiased=True)
## more color map info, https://matplotlib.org/examples/color/colormaps_reference.html

cbar = plt.colorbar(surf)
cbar.set_label('Total Suuttering Yield on a Grid')

#fig.savefig('metoo.png')   # save the figure to file
#plt.close(fig)
plt.show()


