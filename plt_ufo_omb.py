import numpy as np
import sys
import statistics
import math
import matplotlib.pyplot as plt
from netCDF4 import Dataset

#from datetime import datetime
#import matplotlib.colors as colors
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature

def plt_ufo_t(filename,OBSTYPE,VarName):

   thisobstype=OBSTYPE
   thisvarname=VarName
   gsihofXBc=thisvarname+'@GsiHofXBc'
   gsihofX  =thisvarname+'@GsiHofX'
   ufohofX  =thisvarname+'@hofx'
   f=Dataset(filename, mode='r')
   gsi_observer_withqc=f.variables[gsihofXBc][:]
   gsi_observer_noqc  =f.variables[gsihofX][:]
   ufo                =f.variables[ufohofX][:]
   geopotential_height=f.variables['geopotential_height@MetaData'][:]
   f.close()

   plt.rcParams.update({'font.size': 18})
#  plt.rcParams.update({'line.linewidth': 8})
#=========================
   fig = plt.figure(figsize=(8.0,7.5))
   ax=fig.add_subplot(111)

   plt.scatter(gsi_observer_withqc,ufo, color='blue',label=thisobstype, marker='o', s=3)

# Put a legend to the right of the current axis
#  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

   plt.xlabel('gsi')
   plt.ylabel('ufo')
   plt.title(thisobstype+':gsi and ufo hofx scatter')
   figname='ufo_'+thisobstype+'_stage1_scatter_'+subtask+'.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================

#=========================
#  diff=gsi_observer_noqc
   diff=gsi_observer_withqc
   diff=diff - ufo
   print(diff)

   rms=float(0)
   for x in diff:
      rms=rms+x*x
   rms=math.sqrt(rms/len(diff))
   print("rms=",rms)

#  diff=diff*1000.0

   print(diff.max(),diff.min())

   fig1 = plt.figure(figsize=(8.0,7.5))
   ax=fig1.add_subplot(111)
#  plt.hist(diff,bins=50,range=(-0.10,0.10))
   plt.hist(diff,bins=50,range=(-2.00,2.00))
#  plt.xlim([-0.15,0.15])
   plt.xlabel('(gsi-ufo)*1')
   plt.title(thisobstype+':gsi and ufo diff histogram')
   figname='ufo_'+thisobstype+'_stage1_hist_'+subtask+'.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================

#=========================
   fig2 = plt.figure(figsize=(8.0,7.5))
   ax=fig2.add_subplot(111)
   plt.scatter(diff,geopotential_height, color='b',label="rw", marker='o', s=3)
#  plt.xlim([-0.15,0.15])
   plt.xlabel('(gsi-ufo)*1')
   plt.ylabel('geop-height')
   plt.title(thisobstype+':gsi-ufo diff in vertical')
   figname='ufo_'+thisobstype+'_stage1_vdiff_scatter_'+subtask+'.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================


#=====================================================================
#=====================================================================
if __name__ == '__main__':

   print("start ploting")
   print("ploting gsi hofx v.s. ufo hofx")
   fileame=sys.argv[1]
   OBSTYPE=sys.argv[2]
   VarName=sys.argv[3]
   subtask=sys.argv[4]
   plt_ufo_t(fileame,OBSTYPE,VarName)
   print("ploting done")

