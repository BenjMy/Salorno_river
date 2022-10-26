#!/usr/bin/env python
# coding: utf-8

# ## Independant inversion from T2 to T6

# In[1]:


# -------- ResIPy log file -------

import warnings
warnings.filterwarnings('ignore')
from resipy import Project
import pyvista as pv

pv.set_jupyter_backend('panel')

dir_simu = '../INV/regMode1step' + str(i+2) + '/'
k = Project(dirname=dir_simu, typ='R3t')
k.loadProject(dir_simu + "Salorno_2_step" + str(i+2) + ".resipy")

# In[2]:


pl = pv.Plotter(notebook=True,shape=(2, 3))
name = 'Salorno_2_cl5_step_rec10'
for i in range(5):
    
    dir_simu = '../INV/regMode1step' + str(i+2) + '/'
    k = Project(dirname=dir_simu, typ='R3t')
    #k.loadProject(dir_simu + "Salorno_2_step" + str(i+2) + ".resipy")
    k.loadProject(dir_simu + name + str(i+2) + ".resipy")


    if i<3:
        pl.subplot(0, i)
    else:
        pl.subplot(1, i-3)
    pl.add_text("Time" + str(i), font_size=10)
    print(i)
    k.showResults(
                  index = 0,
                  attr='Resistivity(ohm.m)',
                  ax=pl, 
                  vmin=0, 
                  vmax=300, 
                  color_map='jet',zlim=[-30,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=False,
                    )
    pl.show_bounds(all_edges=True)
    
pl.show()


# In[3]:



for i in range(5):
    
    dir_simu = '../INV/regMode1step' + str(i+2) + '/'
    k = Project(dirname=dir_simu, typ='R3t')
    #k.loadProject(dir_simu + "Salorno_2_step" + str(i+2) + ".resipy")
    k.loadProject(dir_simu + name + str(i+2) + ".resipy")

    pl = pv.Plotter(notebook=True)

    k.showResults(
                  index = 0,
                  attr='Resistivity(ohm.m)',
                  ax=pl, pvslices=([5,15,25],[15],[]), 
                  vmin=0, 
                  vmax=300, 
                  color_map='jet',zlim=[-30,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=True,
                    )
    pl.show_bounds(all_edges=True)


# In[4]:


pl = pv.Plotter(notebook=True,shape=(2, 3))

for i in range(5):
    
    dir_simu = '../INV/regMode1step' + str(i+2) + '/'
    k = Project(dirname=dir_simu, typ='R3t')
    #k.loadProject(dir_simu + "Salorno_2_step" + str(i+2) + ".resipy")
    k.loadProject(dir_simu + name + str(i+2) + ".resipy")

    if i<3:
        pl.subplot(0, i)
    else:
        pl.subplot(1, i-3)
    k.showResults(
                  index = 0,
                  attr='Resistivity(ohm.m)',
                  ax=pl, pvslices=([5,15,25],[15],[]), 
                  vmin=0, 
                  vmax=300, 
                  color_map='jet',zlim=[-30,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=False,
                    )
    pl.show_bounds(all_edges=True)

pl.show()


# ## Time lapse between November 2021 and April 2022

# In[5]:


# -------- ResIPy log file -------

from resipy import Project
import pyvista as pv
dir_simu = '../INV/timeLapse/TL12regMode2/'
k = Project(dirname=dir_simu, typ='R3t')
#k.loadProject(dir_simu + "Salorno_TL12_reg2.resipy")
#k.loadProject(dir_simu + "Salorno_TL12_filtAppRes_estErr.resipy")
k.loadProject(dir_simu + "Salorno_TL12regMode2rec10finemeshparallelF.resipy")





# In[6]:


pl = pv.Plotter(notebook=True,shape=(1, 3))
pvslices=([5,15,25],[15],[])

pl.subplot(0, 0)
k.showResults(
              index = 0,
              attr='Resistivity(ohm.m)',
              ax=pl, 
              vmin=0, 
              vmax=300, 
              color_map='jet',zlim=[-30,0],
              background_color='white',pvslices=pvslices,
              pvgrid = True,
              pvshow=False,
                )
pl.show_bounds(all_edges=True)


pl.subplot(0, 1)
k.showResults(
              index = 1,
              attr='Resistivity(ohm.m)',
              ax=pl, 
              vmin=0, 
              vmax=300, 
              color_map='jet',zlim=[-30,0],
              background_color='white',pvslices=pvslices,
              pvgrid = True,
              pvshow=False,
                )
pl.show_bounds(all_edges=True)


pl.subplot(0, 2)
k.showResults(
              index = 1,
              attr='difference(percent)',
              ax=pl, pvslices=([5,15,25],[15],[]), 
              vmin=0, vmax=100,
              color_map='bwr',zlim=[-30,0],
              background_color='white',
              pvgrid = True,
              pvshow=False,
                )
pl.show_bounds(all_edges=True)

pl.show()


# In[7]:


pl = pv.Plotter(notebook=True)
pvslices=([5,15,25],[15],[])

k.showResults(
              index = 1,
              attr='difference(percent)',
              ax=pl, pvslices=([5,15,25],[15],[]), 
              vmin=0, vmax=100,
              color_map='bwr',zlim=[-30,0],
              background_color='white',
              pvgrid = True,
              pvshow=False,
                )
pl.show_bounds(all_edges=True)

pl.show()


# In[8]:


pl = pv.Plotter(notebook=True)

k.showResults(
              index = 1,
              attr='difference(percent)',
              ax=pl, pvcontour=[50, 100], 
              vmin=50, vmax=150,
              color_map='jet',zlim=[-31,0],
              background_color='white',
              pvgrid = True,
              pvshow=False,
                )
pl.show_bounds(all_edges=True)

pl.show()

pl = pv.Plotter(notebook=True)

k.showResults(
              index = 1,
              attr='difference(percent)',
              ax=pl, pvcontour=[100, 150], 
              vmin=50, vmax=150,
              color_map='jet',zlim=[-31,0],
              background_color='white',
              pvgrid = True,
              pvshow=False,
                )
pl.show_bounds(all_edges=True)

pl.show()


# ## Time lapse during tracer injection (background inv)

# In[9]:


# -------- ResIPy log file -------

from resipy import Project
import pyvista as pv
dir_simu = '../INV/timeLapse/TL2b3456regMode2/'
k_back = Project(dirname=dir_simu, typ='R3t')
#k.loadProject(dir_simu + "Salorno_TL2b3456regMode2.resipy")
#k_back.loadProject(dir_simu + "Salorno_TL2b3456regMode2trimRecfinemeshparallelTlinErr.resipy")
#k_back.loadProject(dir_simu + "Salorno_TL2b3456regMode2trimRecfinemeshparallelF.resipy")
k_back.loadProject(dir_simu + "Salorno_TL2b3456regMode2trimRecfinemeshparallelF_3.resipy")


# In[10]:


pl = pv.Plotter(notebook=True,shape=(2, 3))

for i in range(5):
    if i<3:
        pl.subplot(0, i)
    else:
        pl.subplot(1, i-3)
    pl.add_text("Time" + str(i), font_size=10)
    k_back.showResults(
                  index = 0,
                  attr='Resistivity(ohm.m)',
                  ax=pl, 
                  vmin=0, 
                  vmax=300, 
                  color_map='jet',zlim=[-30,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=False,
                    )
    pl.show_bounds(all_edges=True) 
pl.show()


# In[11]:


pl = pv.Plotter(notebook=True,shape=(2, 4))

for i in range(4):
    pvcontour=[0, 50]
    pl.subplot(0, i)
    k_back.showResults(
                  index = i,
                  attr='difference(percent)',
                  ax=pl, pvcontour=pvcontour, 
                  vmin=0, vmax=150,
                  color_map='bwr',zlim=[-31,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=False,
                    )
    pl.show_bounds(all_edges=True)
    
    
    pl.subplot(1, i)
    pvcontour=[50, 150]
    k_back.showResults(
                  index = i,
                  attr='difference(percent)',
                  ax=pl, pvcontour=pvcontour, 
                  vmin=0, vmax=150,
                  color_map='bwr',zlim=[-31,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=False,
                    )
    pl.show_bounds(all_edges=True)
    

pl.show()


# ## Time lapse during tracer injection (difference inv)

# In[12]:


# -------- ResIPy log file -------

from resipy import Project
import pyvista as pv
dir_simu = '../INV/timeLapse/TL2b3456regMode1/'
k_diff = Project(dirname=dir_simu, typ='R3t')
#k.loadProject(dir_simu + "Salorno_TL2b3456.resipy")
k_diff.loadProject(dir_simu + "Salorno_TL2b3456regMode1trimRecfinemeshparallelF.resipy")


# In[13]:


pl = pv.Plotter(notebook=True,shape=(2, 3))

for i in range(5):
    if i<3:
        pl.subplot(0, i)
    else:
        pl.subplot(1, i-3)
    k_diff.showResults(
                  index = 0,
                  attr='Resistivity(ohm.m)',
                  ax=pl, pvslices=([5,15,25],[15],[]), 
                  vmin=0, 
                  vmax=300, 
                  color_map='jet',zlim=[-30,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=False,
                    )
    pl.show_bounds(all_edges=True)

pl.show()


# In[14]:


pl = pv.Plotter(notebook=True,shape=(2, 2))
#pl.add_text("Diff\n", font_size=30)

for i in range(4):
    if i<2:
        pl.subplot(0, i)
    else:
        pl.subplot(1, i-2)
            
    k_diff.showResults(
                  index = i,
                  attr='difference(percent)',
                  ax=pl, pvslices=([5,15,25],[15],[]), 
                  vmin=0, vmax=10,
                  color_map='bwr',zlim=[-30,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=False,
                    )
    pl.show_bounds(all_edges=True)

pl.show()


# In[15]:


pl = pv.Plotter(notebook=True,shape=(2, 4))

for i in range(4):
    pvcontour=[0, 5]
    pl.subplot(0, i)
    k_diff.showResults(
                  index = i,
                  attr='difference(percent)',
                  ax=pl, pvcontour=pvcontour, 
                  vmin=0, vmax=150,
                  color_map='bwr',zlim=[-31,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=False,
                    )
    pl.show_bounds(all_edges=True)
    
    
    pl.subplot(1, i)
    pvcontour=[5, 10]
    k_diff.showResults(
                  index = i,
                  attr='difference(percent)',
                  ax=pl, pvcontour=pvcontour, 
                  vmin=0, vmax=150,
                  color_map='bwr',zlim=[-31,0],
                  background_color='white',
                  pvgrid = True,
                  pvshow=False,
                    )
    pl.show_bounds(all_edges=True)
    

pl.show()

