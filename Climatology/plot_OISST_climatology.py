"""
Code to make plot of the OISST 1993-2022.
"""
from lo_tools import Lfun, zfun
from lo_tools import plotting_functions as pfun
import pinfo
from importlib import reload
reload(pfun)
reload(pinfo)

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import sys
from cmocean import cm
import pandas as pd

Ldir = Lfun.Lstart()


# read obs climatology from OISST
in_dir0 = Ldir['LOo'] / 'climatology' / 'OISST2.1'
fn = in_dir0 / 'sst.season.mean_1993_2022.nc'
    
df = xr.open_dataset(fn)


season = ['Winter', 'Spring', 'Summer', 'Fall']
months = ['(JFM)','(AMJ)', '(JAS)','(OND)']


vn_list = ['temp']

# output directory
    
outdir0 = Ldir['LOo'] / 'plots'/ 'climatology'  
Lfun.make_dir(outdir0)
outname = 'plot_' + 'OISST' + '_' + '1993-2022' + '_' + vn_list[0] + '_' + 'seasonal' +'.png'
print(outname)
outfile = outdir0 / outname
in_dict = dict()
in_dict['fn_out'] = outfile

# PLOTTING

plt.close('all')

# Focus on whole domain
aa = [-130, -122, 42, 52]

# AR is the aspect ratio of the map: Vertical/Horizontal
AR = (aa[3] - aa[2]) / (np.sin(np.pi*aa[2]/180)*(aa[1] - aa[0]))

fs = 20
hgt = 20    
pfun.start_plot(fs=fs, figsize=(5,hgt)) # now change it to single plot

fig = plt.figure()

vn = vn_list[0]
for ii in np.arange(1,5): 
    ax = fig.add_subplot(4, len(vn_list), ii)
    if ii == 1:
        vnn = 'sst'
        ax.set_title('OISST 1993-2022\n', fontsize=1.2*fs)
    clm = df.isel(season = ii-1)     
    Lon = clm['lon'].values
    Lat = clm['lat'].values 
    cs = ax.pcolormesh(Lon, Lat, clm[vnn].values, vmin=pinfo.vlims_dict[vn][0], vmax=pinfo.vlims_dict[vn][1], cmap=pinfo.cmap_dict[vn], alpha=pinfo.fac_dict[vn])

    fig.colorbar(cs)    
    pfun.add_coast(ax)
    ax.axis(aa)
    pfun.dar(ax)

    ax.text(.97, .83, '%s\n %s' % (season[ii-1], months[ii-1]),
       horizontalalignment='right' , verticalalignment='bottom',
       transform=ax.transAxes, fontsize=fs,fontweight='bold',
       bbox=dict(facecolor='w', edgecolor='None',alpha=.0))   
    if ii == 1 or ii ==3:
        ax.set_ylabel('Latitude')
        # ax.set_yticklabels([]) 
    if ii == 2 or ii == 4:
        #ax.set_yticklabels([]) 
        ax.set_ylabel('Latitude')
        
    if ii == 4:
        ax.set_xlabel('Longitude')
    
plt.tight_layout()
    
if len(str(in_dict['fn_out'])) > 0:
    plt.savefig(in_dict['fn_out'])  
plt.show()
pfun.end_plot()

df.close()