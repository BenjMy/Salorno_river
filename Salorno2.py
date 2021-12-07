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


sys.path.append((os.path.relpath('../src'))) # add here the relative path of the API folder
from resipy import Project
dir_simu = '.'
k = Project(dirname=dir_simu, typ='R3t')
k.setTitle('Salorno_site2')


# create survey
# -----------------------------------------------------------------------------
k.createSurvey('./file120data.csv', ftype='Syscal') # read the survey file
per_rec = 10 #10
k.filterRecip(index=-1, percent=per_rec)


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
pozzi_coords = pd.read_csv('./coordinatepozzilaghetti.txt', header='infer')

pozzi_coords['x'] = pozzi_coords['x'] - min(pozzi_coords['x'])
pozzi_coords['y'] = pozzi_coords['y'] - min(pozzi_coords['y'])
pozzi_coords['z'] = pozzi_coords['z'] - min(pozzi_coords['z'])

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
    # elecs[ze[0]][2] +=  ze[1]
    elecs[ze[0]][2] =  ze[1]

elecs = np.vstack(elecs)
max_elecs= max(elecs[:,2])

# buried flag for upper surface electrode is False!
# -----------------------------------------------------------------------------
buried = []
for e in elecs:
    if e[2] == max_elecs:
        buried.append(False)
    else:
        buried.append(True)
            
# plot electrode positions
# -----------------------------------------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(elecs[:,0], elecs[:,1], elecs[:,2], marker='o')

ax.set_xlabel('Lat (m)')
ax.set_ylabel('Long (m)')
ax.set_zlabel('Altitude z (m)')

plt.show()

# electrode positions to dataframe
# -----------------------------------------------------------------------------
elecs_df = pd.DataFrame(elecs,columns=['x', 'y', 'z'])
elecs_df['label'] = label
elecs_df['buried'] = buried

elecs_df.to_csv('./elecs120data.csv', index=False)

k.setElec(elecs_df)
k.createMesh()


# k.saveMesh('mesh_Salorno2.vtk')
# k.importMesh('./mesh_Salorno2.vtk')

k.showMesh()

             # cl_factor=8.00, 
             # cln_factor=100.00, 

#%%
# import raw data and reshape for resipy 
# -----------------------------------------------------------------------------
data = np.loadtxt('./file120data.dat')

data_df = pd.DataFrame(data[:,[0,1,2,3,8,9]], columns=['Spa.1','Spa.2','Spa.3','Spa.4','Vp' ,'In'])

# for spa in enumerate(['Spa.1','Spa.2','Spa.3','Spa.4']):
    
data_df['Spa.1'] = data_df['Spa.1'].astype(int)
data_df['Spa.2'] =data_df['Spa.2'].astype(int)
data_df['Spa.3'] =data_df['Spa.3'].astype(int)
data_df['Spa.4'] = data_df['Spa.4'].astype(int)

data_df['dev'] = np.zeros(len(data_df['Spa.1']))
data_df.to_csv('./file120data.csv', index=False)



# inversion
# -----------------------------------------------------------------------------

k.param['num_xy_poly'] = 0
k.param['z_min'] = max(elecs_df['z'])
k.param['z_max'] = min(elecs_df['z'])
k.param['data_type'] = 1 # using log of resistitivy
k.err = False # if we want to use the error from the error models fitted before
k.param['a_wgt'] = 0.01
k.param['b_wgt'] = per_rec/100 #0.05
k.invert() # this will do the inversion
# k.saveData(MainPath)

# mesh = pv.read(k.dirname + '/f001_res.vtk')
# mesh.array_names


# %%

# import pyvista as pv

k.showResults(attr='Resistivity(log10)', 
              sens=True, 
              contour=True, 
              use_pyvista=True,
              color_map='jet')
#,             xlim=[0,100],ylim=[-50,50],zlim=[-100,0])

k.showResults(attr='Sensitivity_map(log10)', 
              sens=True, 
              contour=True, 
              use_pyvista=True,pvshow=True) 

# background_color

pl = pv.Plotter()
k.showResults(attr='Resistivity(ohm.m)',
              ax=pl, pvslices=([5,15,25],[10,20],[]), 
              pvgrid=True, 
              vmin=0, 
              vmax=250, 
              color_map='plasma')

pl = pv.Plotter()
k.showResults(attr='Resistivity(ohm.m)',
              ax=pl, pvthreshold=[0,75], pvgrid=True)


# save project
# -----------------------------------------------------------------------------
k.saveProject('Salorno_2')

# %% Time lapse

# k_TL = Project(typ='R3t')
# k_TL.createTimeLapseSurvey([testdir + '1230.csv',
#                             testdir + '1231.csv',
#                             testdir + '1232.csv',
#                             testdir + '1233.csv',
#                             ],
#                               ftype='Syscal')

# k_TL.filterRecip(percent=5.000000)

# k_TL.importMesh(testdir + 'mesh3d.dat')
# k_TL.param["a_wgt"] = 0.010000
# k_TL.param["b_wgt"] = 0.05


# k_TL.invert()
# # by default `reg_mode == 2` (difference inversion)
# print(k_TL.param['reg_mode'])

# k_TL.showResults(index=1, pvslices=[[10,20,30,40],[0],[]], attr='difference(percent)',
#              color_map='bwr', vmin=-10, vmax=10)


# # %% 
# # background constrained - see d-d0+f(m0) in the log
# k_TLb = Project(typ='R3t')
# k_TLb.createTimeLapseSurvey([testdir + '1230.csv',
#                             testdir + '1231.csv',
#                             testdir + '1232.csv',
#                             testdir + '1233.csv',
#                             ],
#                               ftype='Syscal')
# k_TLb.importMesh(testdir + 'mesh3d.dat')

# k_TLb.filterRecip(percent=5.000000)
# k_TLb.param["a_wgt"] = 0.010000
# k_TLb.param["b_wgt"] = 0.05

# k_TLb.param['reg_mode'] = 1
# k_TLb.param['num_xy_poly'] = 0 # tells R3t to no crop the mesh
# k_TLb.param['zmin'] = -np.inf
# k_TLb.param['zmax'] = np.inf
# k.invert()

# k_TLb.showResults(index=1, pvslices=[[10,20,30,40],[0],[]], attr='difference(percent)',
#              color_map='bwr', vmin=-10, vmax=10)
