#!/usr/bin/env python
# coding: utf-8

# # Notebook for the Alento (site nb2) data processing
# 
# - 🔨 Data acquisition: G. Cassiani
# - Notebook Author: B. Mary
# 
# ### Steps to reproduce
# - import all libraries
# - import raw merged data 
# - create resipy project 3d
# - import electrode geometry
# - create thetra mesh
# - invert
# - show results 

# In[15]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:22:55 2021

@author: ben
"""
# import resipy and other useful libraries
# -----------------------------------------------------------------------------
#get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv


# In[16]:


#!pip install resipy==3.3.2


# In[17]:


correct_topo = 1
per_rec = 10 #10


# In[18]:


sys.path.append((os.path.relpath('../src'))) # add here the relative path of the API folder
from resipy import Project


# In[19]:



# dir_simu = './background_time'
dir_simu = '.'

dir_simu = '../INV/November_2021_f1'

k = Project(dirname=dir_simu, typ='R3t')
k.setTitle('Salorno_site2')


# # Import RAW data
# ### Raw file: file120data.dat

# # Set reciprocal filter to 10%

# In[20]:


# create survey
# -----------------------------------------------------------------------------
k.createSurvey('../rawData/file120data.csv', ftype='Syscal') # read the survey file
k.filterRecip(index=-1, percent=per_rec)


# # Create boreholes geometry
# 
# ### raw file: coordinatepozzilaghetti.txt

# In[21]:


# create boreholes geometry
# -----------------------------------------------------------------------------
nb_elecs_bor = 24
elecs_spacing = 1
offset = 1
asc_bor = np.arange(-nb_elecs_bor*elecs_spacing-offset,0-offset)
des_bor = np.flip(asc_bor)
elecs_z = np.hstack([asc_bor,des_bor,des_bor,des_bor,des_bor])

elecs = []
label = []

# lat/long of the electrodes
# -----------------------------------------------------------------------------
pozzi_coords = pd.read_csv('../survey/coordinatepozzilaghetti.txt', header='infer')

# lat/long to absolute positions
# -----------------------------------------------------------------------------
pozzi_coords['x'] = pozzi_coords['x'] - min(pozzi_coords['x'])
pozzi_coords['y'] = pozzi_coords['y'] - min(pozzi_coords['y'])
pozzi_coords['z'] = pozzi_coords['z'] - max(pozzi_coords['z'])


i=1
for index, row in pozzi_coords.iterrows():
    for ne in range(len(asc_bor)):
        elecs.append([row[1],row[2],row[3]])
        # print([str(1),str((ne+1)*(index+1))])
        # label.append(' '.join([str(index+1),str(ne+1)]))
        # label.append(' '.join([str(1),str(i)]))
        label.append(' '.join([str(i)]))
        i +=1

# correct for altitude
# -----------------------------------------------------------------------------
for ze in enumerate(elecs_z):
    # print(ze)
    if correct_topo == 1:
        elecs[ze[0]][2] +=  ze[1]
    else:
        elecs[ze[0]][2] =  ze[1]

elecs = np.vstack(elecs)

if correct_topo == 1:
    max_elecs = pozzi_coords['z'] - 2
else:
    max_elecs= max(elecs[:,2])

# buried flag for upper surface electrode is False!
# -----------------------------------------------------------------------------
buried = []
for e in elecs:
    if (round(e[2],4) == round(max_elecs, 4)).any():
        buried.append(False)
    else:
        buried.append(True)
            

# electrode positions to dataframe
# -----------------------------------------------------------------------------
elecs_df = pd.DataFrame(elecs,columns=['x', 'y', 'z'])
elecs_df['label'] = label
elecs_df['buried'] = buried

elecs_df.to_csv('./elecs120data.csv', index=False)
elecs_df.head()


# # Create mesh (using gmsh)
# ## refine is set to 1

# In[11]:


k.setElec(elecs_df)
# k.createMesh(refine=1)
k.createMesh(refine=0,cl_factor=1,cl=1) #,fmd=1

k.showMesh()
             # cl_factor=8.00, 
             # cln_factor=100.00,


# In[13]:


# import raw data and reshape for resipy 
# -----------------------------------------------------------------------------
data = np.loadtxt('../rawData/file120data.dat')

data_df = pd.DataFrame(data[:,[0,1,2,3,8,9]], columns=['Spa.1','Spa.2','Spa.3','Spa.4','Vp' ,'In'])
data_df['Spa.1'] = data_df['Spa.1'].astype(int)
data_df['Spa.2'] =data_df['Spa.2'].astype(int)
data_df['Spa.3'] =data_df['Spa.3'].astype(int)
data_df['Spa.4'] = data_df['Spa.4'].astype(int)

data_df['dev'] = np.zeros(len(data_df['Spa.1']))
data_df.to_csv('./file120data.csv', index=False)

data_df.head()


# # Inversion

# In[14]:


# inversion
# -----------------------------------------------------------------------------
k.param['num_xy_poly'] = 0
k.param['z_min'] = -np.inf
k.param['z_max'] = np.inf

# k.param['z_min'] = max(elecs_df['z'])
# k.param['z_max'] = min(elecs_df['z'])
k.param['data_type'] = 1 # using log of resistitivy
k.err = False # if we want to use the error from the error models fitted before
k.param['a_wgt'] = 0.01
k.param['b_wgt'] = per_rec/100 #0.05
k.invert() # this will do the inversion
# k.saveData(MainPath)


# save project
# -----------------------------------------------------------------------------
k.saveProject('Salorno_2')

# # Results

# In[11]:


#pl = pv.Plotter()
#mesh = pv.read(k.dirname + '/f001_res.vtk')
#pl.add_mesh(mesh)
#pl.show()


# In[12]:


k.showResults(attr='Resistivity(log10)', 
              sens=True, 
              contour=True, 
              use_pyvista=True,
              color_map='jet',zlim=[-30,0],
              background_color='white')


# In[13]:


pl = pv.Plotter()
k.showResults(attr='Resistivity(ohm.m)',
              ax=pl, pvslices=([5,15,25],[15],[]), 
              pvgrid=True, 
              vmin=0, 
              vmax=300, 
              color_map='jet',zlim=[-30,0],
              background_color='white')


# In[14]:


pl = pv.Plotter()
k.showResults(attr='Resistivity(ohm.m)',
              ax=pl, pvthreshold=[0,75], pvgrid=True,zlim=[-30,0],
              background_color='white')


# In[15]:




# In[ ]:




