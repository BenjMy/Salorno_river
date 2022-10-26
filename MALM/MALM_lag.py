#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:05:37 2022

@author: ben
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

MALM = pd.read_csv('./MALM_LAG_270622.csv',sep=',')

MALM['R'] = MALM['Vp  ']/MALM['In  ']
MALM_d = MALM['R'].iloc[np.arange(0,len(MALM['R']),2)]
MALM_r = MALM['R'].iloc[np.arange(1,len(MALM['R']),2)]

# plt.plot(MALM_d)
# plt.plot(MALM_r)
nx = int((len(MALM)/4)/2)
# plt.plot(MALM['R'])

ny = 4
x = np.linspace(0, 18*2, nx+1)
y = np.linspace(0, 3*4, ny)
len(x)


gridx, gridy = np.meshgrid(x, y)
gridx = gridx.flatten()
gridy = gridy.flatten()

len(gridy)
len(MALM_r)

# plt.scatter(gridx[:-1],gridy[:-1],c=MALM_d.iloc[:])
plt.scatter(gridx[:-1],gridy[:-1],c=MALM_r.iloc[:])
plt.xlabel('x // dike (m)')
plt.ylabel('y _| dike (m)')
cb = plt.colorbar()
cb.set_label('V/I')

plt.scatter(y=-3,x=18,c='r',marker='v',s=1e2,label='center B3')
plt.scatter(x=5,y=-0.5,c='g',marker='^',s=1e2,label='B1')
plt.scatter(x=30,y=-0.5,c='b',marker='^',s=1e2,label='B2')

plt.title('MALM laghetti 27/06/22')
plt.legend()
# h = plt.contourf(x, y, zs)

