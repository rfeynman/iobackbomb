'''
Created on Apr 15, 2017

@author: wange
'''



from scipy.constants import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
from numpy import genfromtxt
import time
from traitlets.traitlets import add_article

def mapplot(data,deg,apt,off,rad):
    rcathode=0.013
    e0_p=938.27e6
    data_ind=e0_p*((1-np.array(data['Bz'])**2)**(-0.5)-1)>(350000*0.99)
    data_r=data[data_ind]
    z=(np.array(data_r['x'])**2+np.array(data_r['y'])**2)**(0.5)
    lenz=len(z)
    shieldlz=int(lenz*0.9)
    r90p=np.sort(z)[shieldlz]
    
    
    x=np.array([data['x']])
    y=np.array([data['y']])
    bz=np.array([data['Bz']])
    tem=np.append(x.T,y.T,axis=1)
    newarray=np.append(tem,bz.T,axis=1)
    
    fig,ax=plt.subplots()
    plt.figure(1)
    plt.scatter(x,y,c=e0_p*((1-bz**2)**(-0.5)-1),edgecolors='none',marker='.',alpha=0.4,cmap=plt.cm.RdYlGn) 
    plt.xlabel('x[m]')
    plt.ylabel('y[m]')
    plt.text(-0.014,0.0135,str(deg)+'deg_'+str(apt)+'apt_'+str(off)+'off_'+str(rad)+'rad')
    plt.text(0.001,0.0135,'r_damage(90%)='+'%.2f mm' % (r90p*1000))

    cb=plt.colorbar()
    cb.set_label('Proton energy [eV]')
    cir=plt.Circle((0,0),rcathode,color='b',fill=False)
    cir_90p=plt.Circle((0,0),r90p,color='r',ls='dashed',fill=False)
    ax.set_xlim((-0.015,0.015))
    ax.set_ylim((-0.015,0.015))
    ax.add_artist(cir)
    ax.add_artist(cir_90p)  
    plt.savefig('../'+str(deg)+'deg_'+str(apt)+'apt_'+str(off)+'off_'+str(rad)+'rad_'+'map.png')
    
    plt.figure(2,figsize=(10,10))
    plt.subplot(211)
    plt.hist(x[0], bins=20,facecolor='g',normed=True)
    plt.xlim(-0.015,0.015)
    plt.xlabel('x[m]')
    plt.ylabel('#')
    plt.text(-0.013,350,str(deg)+'deg_'+str(apt)+'apt_'+str(off)+'off_'+str(rad)+'rad')
    plt.subplot(212)
    plt.hist(y[0], bins=12,facecolor='g',normed=True)
    plt.xlim(-0.015,0.015)
    plt.xlabel('y[m]')
    plt.ylabel('#')
    plt.savefig('../'+str(deg)+'deg_'+str(apt)+'apt_'+str(off)+'off_'+str(rad)+'rad_'+'his.png')

    plt.show()
    
    return(0)

def main():
    ionsmap= genfromtxt('../ions_22deg_18apt_6off_4.3r_scttgap_results.txt',delimiter='',dtype=None,names=True)
    mapplot(ionsmap,22,18,6,4.3)   
    ionsmap= genfromtxt('../ions_22deg_18apt_6off_4r_scttgap_results.txt',delimiter='',dtype=None,names=True)
    mapplot(ionsmap,22,18,6,4)
    ionsmap= genfromtxt('../ions_22deg_18apt_6off_3r_scttgap_results.txt',delimiter='',dtype=None,names=True)
    mapplot(ionsmap,22,18,6,3)
    ionsmap= genfromtxt('../ions_22deg_18apt_6off_2r_scttgap_results.txt',delimiter='',dtype=None,names=True)
    mapplot(ionsmap,22,18,6,2)
    ionsmap= genfromtxt('../ions_22deg_18apt_6off_1r_scttgap_results.txt',delimiter='',dtype=None,names=True)
    mapplot(ionsmap,22,18,6,1)
    ionsmap= genfromtxt('../ions_22deg_18apt_4off_4.3r_scttgap_results.txt',delimiter='',dtype=None,names=True)
    mapplot(ionsmap,22,18,4,4.3)
    ionsmap= genfromtxt('../ions_22deg_18apt_2off_4.3r_scttgap_results.txt',delimiter='',dtype=None,names=True)
    mapplot(ionsmap,22,18,2,4.3)
    ionsmap= genfromtxt('../ions_22deg_18apt_0off_4.3r_scttgap_results.txt',delimiter='',dtype=None,names=True)
    mapplot(ionsmap,22,18,0,4.3)
    
if __name__ == '__main__':
    main()