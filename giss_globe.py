#!/usr/bin/env python
# coding: utf-8

# In[2]:


from netCDF4 import Dataset

data=Dataset("june.nc")
#print(data)

lons=data.variables["lon"][:]

lats=data.variables["lat"][:]

temp_anomaly=data.variables["TEMPANOMALY"][:]
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
from matplotlib import colormaps
def temp_anomaly_plot(projection, projection_name):
    
    fig = plt.figure(figsize = (12, 6))
    
    #Add an axes to the current figure and make it the current axes.
    ax = plt.axes(projection = projection)
    
    #make the map global rather than having it zoom in to extent of the plotted data
    ax.set_global()
    
    ax.gridlines(linestyle = "--", color = "black")

    #Set contour levels, then draw the plot and a colorbar
    clevs = np.arange(-5, 6)
    cmap = "coolwarm"

    #Plot filled contours
    plt.contourf(lons, lats, 
                 temp_anomaly,
                 clevs,
                 transform = ccrs.PlateCarree(),
                 cmap = cmap,
                 extend = "both" #To add arrows on both ends of the colorbar
                )
    
    #Add coastlines after filling contours
    ax.coastlines(resolution = "110m", lw = 1)
    
    plt.title(f"June 2023 L-OTI (°C) vs 1951-1980 mean\n Projection: {projection_name}")
    
    cb = plt.colorbar(ax = ax,
                      orientation = "horizontal",
                      pad = 0.02,
                      aspect = 20,  #ratio of long to short dimension
                      shrink = 0.5, #Fraction by which to multiply the size of the colorbar
                      ticks = clevs #To get the ticks same as clevs -5 to 5 degree Celsius in colorbar
                     )

    cb.set_label("°C", size = 12, rotation = 0, labelpad = 15)
    cb.ax.tick_params(labelsize = 10)
    plt.savefig(f"anomaly_{projection_name}.jpeg",
               dpi = 300)
temp_anomaly_plot(projection=ccrs.Orthographic(60,25), projection_name="Orthographic")
    #plt.show()


# In[ ]:




