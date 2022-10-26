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

# In[1]:


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

import ipywidgets


# In[2]:


#!pip install resipy==3.3.2


# In[3]:


correct_topo = 0
per_rec = 1e-99 #10


# In[4]:


sys.path.append((os.path.relpath('../src'))) # add here the relative path of the API folder
from resipy import Project


# In[5]:

regMode = 1
dir_simu = '../INV/timeLapse/TL12' + 'regMode' + str(regMode)

k = Project(dirname=dir_simu, typ='R3t')
k.setTitle('Salorno_site_TL12')


# # Import RAW data
# ### Raw file: file120data.dat

# # Set reciprocal filter to 10%

# In[6]:


print(os.getcwd())

import pandas

filenames = [
            '../rawData/file120data1.dat',
            '../rawData/file120data2.dat',
            ]


# In[ ]:


# import raw data and reshape for resipy 
# -----------------------------------------------------------------------------
#data = np.loadtxt('../rawData/file120data.dat')

#data_df = pd.DataFrame(data[:,[0,1,2,3,8,9]], columns=['Spa.1','Spa.2','Spa.3','Spa.4','Vp' ,'In'])
#data_df['Spa.1'] = data_df['Spa.1'].astype(int)
#data_df['Spa.2'] =data_df['Spa.2'].astype(int)
#data_df['Spa.3'] =data_df['Spa.3'].astype(int)
#data_df['Spa.4'] = data_df['Spa.4'].astype(int)

#data_df['dev'] = np.zeros(len(data_df['Spa.1']))
#data_df.to_csv('./file120data.csv', index=False)

#data_df.head()


# In[14]:


column_names = ['Spa.1','Spa.2','Spa.3','Spa.4','Vp','In']
idx = [0,1,2,3,8,9]
filenames_csv = []
for f in filenames:
    numpyfile = np.loadtxt(f, skiprows=1)
    df=pd.DataFrame(numpyfile[:,idx],columns=column_names)
    df['dev']=np.zeros(len(df['Spa.1']))
    df = df.astype({"Spa.1": int}) 
    df = df.astype({"Spa.2": int}) 
    df = df.astype({"Spa.3": int}) 
    df = df.astype({"Spa.4": int}) 
    filenames_csv.append(f + '.csv')
    df.to_csv(f + '.csv',sep=',',index=False)


# In[15]:


filenames_csv


# In[16]:


# create survey
# -----------------------------------------------------------------------------
print(os.getcwd())
k.createTimeLapseSurvey(filenames_csv,
                         ftype='Syscal')
k.filterRecip(index=-1, percent=per_rec)

k.fitErrorLin()
k.err = True
#k.filterAppResist(index=-1, vmin=0.0, vmax=1000.0)


# # Create boreholes geometry
# 
# ### raw file: coordinatepozzilaghetti.txt

# In[17]:


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

# In[18]:


k.setElec(elecs_df)
k.createMesh(refine=0,cl_factor=15,cl=1) #,fmd=1
#k.createMesh(typ="tetra", surface=None, fmd=None, cl=-1.00, cl_factor=10.00, cln_factor=10.00, refine=0)

# k.showMesh()
             # cl_factor=8.00, 
             # cln_factor=100.00,


# # Inversion

# k.param['z_min'] = max(elecs_df['z'])
# k.param['z_max'] = min(elecs_df['z'])
k.param['data_type'] = 1 # using log of resistitivy
k.err = False # if we want to use the error from the error models fitted before
k.param['a_wgt'] = 0.01
k.param['b_wgt'] = per_rec/100 #0.05


k.invert(parallel=False) # this will do the inversion
# k.saveData(MainPath)
print(k.param['reg_mode'])


# inversion
# -----------------------------------------------------------------------------
# inversion
# -----------------------------------------------------------------------------
if regMode==1:
    k.param['num_xy_poly'] = 0
    k.param['z_min'] = -np.inf
    k.param['z_max'] = np.inf

# k.param['z_min'] = max(elecs_df['z'])
# k.param['z_max'] = min(elecs_df['z'])
k.param['data_type'] = 1 # using log of resistitivy
k.err = False # if we want to use the error from the error models fitted before
k.param['a_wgt'] = 0.01
k.param['b_wgt'] = per_rec/100 #0.05

k.param['reg_mode'] = regMode


k.invert(parallel=False) # this will do the inversion
# k.saveData(MainPath)


# save project
# -----------------------------------------------------------------------------
k.saveProject('Salorno_TL12_' + 'filtRec' + str(per_rec) + '_estErr')

# reg_mode == 1 is refered to as ‘background constrained’ inversion where the subsequente survey are penalized from departure from the reference survey. 
# - reg_mode == 2 (default in ResIPy) is refered to as ‘difference inversion’ but, for 3D,

# k.param['reg_mode'] = 1

# # Results

# In[ ]:


#pl = pv.Plotter()
#mesh = pv.read(k.dirname + '/f001_res.vtk')
#pl.add_mesh(mesh)
#pl.show()
# https://hkex.gitlab.io/resipy/auto_examples/nb_3d-time-lapse.html


# In[ ]:


pl = k.showResults(attr='Resistivity(log10)', 
              sens=True, 
              contour=True, 
              use_pyvista=True,
              color_map='jet',zlim=[-30,0],
              background_color='white',
              )


# In[ ]:


pl = pv.Plotter(notebook=True)
k.showResults(attr='Resistivity(ohm.m)',
              ax=pl, pvslices=([5,15,25],[15],[]), 
              pvgrid=True, 
              vmin=0, 
              vmax=300, 
              color_map='jet',
              background_color='white',
              pvthreshold=None,
              xlim=[0,20],
              ylim=[0,20],
              clipping=True,
              )

# boundingbox=False,
# camerazoom=2
              
#%%

#pvmesh = pv.read(dir_simu + '/invdir/' + 'f001_res.vtk') # read in temporary file 

#pvmesh

#plotter = pv.Plotter()
#_ = plotter.add_mesh(pvmesh)
#plotter.camera.zoom(2.0)
#plotter.show()

# In[ ]:


pl = pv.Plotter(notebook=True)
k.showResults(attr='Resistivity(ohm.m)',
              ax=pl, pvthreshold=[0,95], pvgrid=True,zlim=[-30,0],
              background_color='white')

# In[ ]:

k.showResults(index=1, 
    attr='difference(percent)', 
    contour=False, vmin=0, vmax=100)





# In[ ]:




