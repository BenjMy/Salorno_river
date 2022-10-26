#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:47:18 2022

@author: ben
"""
from dataclasses import dataclass
import pandas as pd
from resipy import Project
from pathlib import Path
import os
import pyvista as pv
import numpy as np
import argparse

#%%


def get_cmd():
    parse = argparse.ArgumentParser()
    process_param = parse.add_argument_group('process_param')
    process_param.add_argument(
        '-Location', type=str, help='Field location', default='Laghetti', required=False) #Laghetti; Salorno
    process_param.add_argument(
        '-TestName', type=str, help='Test name', default='LAGHETTI3', required=False) #LAGHETTI1; SALORNO1
    process_param.add_argument(
        '-run_indiv', type=int, help='Run ind. ERT', default=0, required=False)
    process_param.add_argument(
        '-recErr', type=int, help='Rec. error', default=5, required=False)
    process_param.add_argument(
        '-reprocess', type=int, help='reprocess', default=0, required=False)
    process_param.add_argument(
        '-TLreg', type=int, help='TimeLapse reg mode', default=1, required=False)
    args = parse.parse_args()
    return(args)



#%%

def filter_log(log,field,test_name,typeERT=True):
    log = log[log['Location']==field]
    log = log[log['TestName']==test_name]
    
    if typeERT:
       log = log[log['Type']=='ERT']
    return log

    
def load_files(
                logfile='../Log_Laghetti_Salorno_river_updated.csv',
                field='Laghetti',
                test_name='LAGHETTI1',                
            ):
    
    log = pd.read_csv(logfile)
    log_filtered = filter_log(log,field,test_name)
     
    return log_filtered

def prepare_data(filenames):
    
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
        
    return df

def _run_ERT(log_ERT,filenames=[],invpath='../inversionERT/',
            per_rec=5):
    
    location = log_ERT['Location'].unique()[0]

    for i, f in enumerate(filenames):
        
        p = Path(invpath + location + '/' + f.split('/')[-1])       
        if p.is_dir() is False:
           p.mkdir(parents=True)
                   
        k = Project(p, typ="R3t")
        if location == 'Laghetti':
            k.createSurvey(f + '.csv', ftype="Syscal")
        else:
            k.createSurvey(f, ftype="ProtocolDC")
            
        # k.createSurvey(f + '.csv', ftype="protocolDC")
        k.filterRecip(percent=per_rec)
        k.importElec('../elecs/elecsXYZ_' + location + '.csv')
        k.importMesh('../mesh/mesh3d_' + location + '.dat')
        
        k.param['a_wgt'] = 0.1
        k.param['b_wgt'] = per_rec/100 #0.05
        
        k.param['z_min'] = max(k.elec['z'])
        k.param['z_max'] = min(k.elec['z'])
        
        k.invert(parallel=False) # this will do the inversion

        # save project
        k.saveProject(str(p) + '_rec' + str(per_rec))
        plot_InvertedModel(k,p, index=i)
            

def getR3out(imaging_path, files, typ='R3t'):
    """Reat the .out file and parse its content.
    
    Returns
    -------
    Dataframe with the dataset name, and the RMS decrease for each iteration.
    """
    
    DF_RMS = []
    for i, file_survey in enumerate(files):
        fname = os.path.join(imaging_path, 'inversionERT') + '/' + file_survey + '/invdir/' + typ + '.out'
        
        with open(fname, 'r') as f:
            lines = f.readlines()
        name = ''
        idataset = 0
        iiter = 0
        resRMS = np.nan
        phaseRMS = np.nan
        read = np.nan
        rejected = np.nan
        irow = 0
        df = pd.DataFrame(columns=['name', 'dataset', 'iteration', 'resRMS',
                                   'phaseRMS', 'read', 'rejected', 'success'])
        for x in lines:
            success = 'N/A'
            line = x.split()
            if len(line) > 1:
                if line[0] == 'Iteration':
                    iiter += 1
                elif ('measurements' in x) & ('read:' in x):
                    print(line)
                    read = int(line[5])
                    # rejected = int(line[5])
                elif line[0] == 'Final':
                    resRMS = float(line[3])
                    df.loc[irow, :] = [name, idataset, iiter, resRMS, phaseRMS,
                                       read, rejected, success]
                    irow += 1
                elif line[0] == 'FATAL:':
                    resRMS = np.nan
                elif line[0] == 'Processing':
                    iiter = 0
                    idataset += 1
                    name = file_survey
        df = df.apply(pd.to_numeric, errors='ignore').reset_index(drop=True)
        DF_RMS.append(df)

    DF_RMS = pd.concat(DF_RMS)
        
    return DF_RMS


def run_ERT(log_ERT,filenames=[],invpath='../inversionERT/',
            per_rec=5, reprocess=0):
    
    location = log_ERT['Location'].unique()[0]
    
    if reprocess==1:
        _run_ERT(log_ERT,filenames,invpath,
                    per_rec=5)
    else:
        for i, f in enumerate(filenames):
            p_backup = Path(invpath + location + '/' + f + '_rec' + str(per_rec)  + ".resipy")
            if p_backup.is_file() is False:
                print('revert and process')
                _run_ERT(log_ERT,f,invpath,
                            per_rec)
            else:
                k = Project(p_backup, typ='R3t')
                k.loadProject(os.path.join(f + '_rec' + str(per_rec)  + ".resipy"))
    
    df_rms = []
    for i, f in enumerate(filenames):
        p = Path(invpath + location + '/' + f.split('/')[-1])  
        df_rms.append(getR3out(p,
                               f,
                               )
                    )
    df_rms
    
        

def plot_InvertedModel(k,p,index=0):
    
        pl = pv.Plotter(off_screen=True,notebook=False,                 
                        lighting='three lights',
                        )
        k.showResults(attr='Resistivity(ohm.m)',
                      ax=pl, pvslices=([5,15,25],[15],[]), 
                      pvgrid=True, 
                      vmin=0, 
                      vmax=300, 
                      color_map='jet',
                      zlim=[-30,0],
                      background_color='white'
                      )
        pl.screenshot(str(p) + 'T'+ str(index) + '.png')
        # pl.show(screenshot=str(p) + 'T'+ str(index) + '.png')
        # pl.show()
        # pl.save_graphic(str(p) + 'T'+ str(index) + '.svg')


def plot_TL(k,p):

    for index in range(1,len(k.surveys)):
        
        plot_InvertedModel(k,p,index=index)
        
        pl = pv.Plotter(off_screen=True, notebook=False,
                        lighting='three lights',
                        )
        pv.set_plot_theme('document')

        k.showResults(index=index, pvslices=([],[],[-7.5]), 
                      pvgrid=True, attr='difference(percent)', 
                      contour=False, vmin=-25, vmax=0,ax=pl,
                     )
        # pl.view_xy()
        pl.show(screenshot=str(p) + '_diff' + str(index) + '.png')
        # pl.show()
        # pl.save_graphic(str(p) + '_diff' + str(index) + '.svg')

def _run_ERT_TL(log_ERT,filenames=[],invpath='../inversionERT_TL/',
               per_rec=5,TL_reg=1):
    
    TestName = log_ERT['TestName'].unique()[0]
    location = log_ERT['Location'].unique()[0]

    filenames_csv = []
    for f in filenames:
        filenames_csv.append(f + '.csv')
        
    p = Path(invpath + TestName + '_TL_reg' + str(TL_reg))       
    if p.is_dir() is False:
        p.mkdir(parents=True)
        
    k = Project(p, typ="R3t")
    if location == 'Laghetti':
        k.createTimeLapseSurvey(filenames_csv, ftype="Syscal")
    else:
        k.createTimeLapseSurvey(filenames, ftype="ProtocolDC")

    k.filterRecip(index=-1, percent=per_rec)
    k.importElec('../elecs/elecsXYZ_' + location + '.csv')
    k.importMesh('../mesh/mesh3d_' + location + '.dat')
    
    k.param['a_wgt'] =  0.1
    k.param['b_wgt'] = per_rec/100 #0.05
    # k.param['b_wgt'] = 0.2#per_rec/100 #0.05

    k.param['reg_mode'] = TL_reg
    
    if TL_reg==1:
        k.param['num_xy_poly'] = 0 # tells R3t to no crop the mesh
        k.param['zmin'] = -np.inf
        k.param['zmax'] = np.inf

    k.invert(parallel=False) # this will do the inversion      


    # save project
    k.saveProject(str(p) + '_rec' + str(per_rec))

    plot_TL(k,p)
    
def load_mesh_vtk(k,path,filenames):
    meshpv = []
    for ki in range(len(k.surveys)):
        k.surveys[ki]
        k.dirname
        meshpv.append(pv.read(path + '/' + filenames[ki].split('/')[-1] + '.vtk'))
        
    return meshpv
        
def plot_TL_pv(meshpv,k,clim=[-10,10],path=''):
    
    zlim = k.zlim
    zlim[0] = k.elec['z'].min() #- k.fmd
        
    xlim = [min(k.elec['x']), max(k.elec['x'])]
    ylim = [min(k.elec['y']), max(k.elec['y'])] 
    
        
    for ki in range(1,len(k.surveys)):
        print(ki)
       
        pv.set_plot_theme("document")
        
        mesh = meshpv[ki].clip_box((xlim[0],xlim[1],ylim[0],ylim[1],zlim[0],zlim[1]),invert=False),
        
        plotter = pv.Plotter(notebook=False ,
                         window_size=([2048, 1036]),
                         off_screen=False,
                         lighting='three lights'
                        )
        plotter.add_bounding_box()

        pvslices = [[15],[],[-7.5]]

        att = 'difference(percent)'

        sargs = dict(height=0.05, 
                     width=0.25,
                     vertical=False, 
                     position_x=0.5, 
                     position_y=0.05,
                     title_font_size=25,
                     label_font_size=25,
                     title=att
                     )
        # plotter.add_mesh(mesh[0],
        #                 scalars = att,
        #                 cmap='jet',
        #                 clim=clim,
        #                 opacity=0.75,
        #                 scalar_bar_args=sargs
        #                 )
                      
        for i, ss in enumerate(pvslices): # X, Y then Z slice
            normal = np.zeros(3)
            normal[i] = 1
            for s in ss:
                origin = np.zeros(3)
                origin[i] = s
                mesh_slice = mesh[0].slice(normal=normal, origin=origin)
                plotter.add_mesh(mesh_slice,
                                scalars = att,
                                cmap='jet',
                                clim=clim,
                                # opacity=0.75,
                                scalar_bar_args=sargs
                                )
        labels = dict(zlabel='Z (m)', xlabel='X (m)', ylabel='Y (m)',
                  )
            
        plotter.show_grid()

        plotter.show(screenshot=path + 'T'+ str(ki) + 'diff.png')
        plotter.close()
        
        plotter = pv.Plotter(notebook=False ,
                         window_size=([2048, 1036]),
                         off_screen=False,
                         lighting='three lights'
                        )
        mesh[0].set_active_scalars(att)
        threshed = mesh[0].threshold(value=-15,invert=True)
        largest = threshed.connectivity(largest=True)

        plotter.add_mesh(largest,
                        scalars = att,
                        cmap='jet',
                        clim=clim,
                        scalar_bar_args=sargs
                        ) 
        plotter.add_bounding_box()
        plotter.show(screenshot=path + 'T'+ str(ki) + 'threshold_diff.png')

            
    
def run_ERT_TL(log_ERT,filenames=[],invpath='../inversionERT_TL/',
               per_rec=5,TL_reg=1,
               reprocess=0):
    
    location = log_ERT['Location'].unique()[0]
    TestName = log_ERT['TestName'].unique()[0]
    p = Path(invpath + TestName + '_TL_reg' + str(TL_reg))       

    if reprocess==1:
        _run_ERT_TL(log_ERT,filenames,invpath,
                    per_rec=5)
    else:
            p_backup = Path(str(p) + '_rec' + str(per_rec) + ".resipy")
            if p_backup.is_file() is False:
                print('revert and process')
                _run_ERT_TL(log_ERT,filenames,invpath,
                            per_rec)
            else:
                k = Project(str(p) + 'backup/' , typ='R3t')
                k.loadProject(p_backup)
                
                path2mesh = (
                             str(p) + 'backup/invdir/' 
                             + str(p).split('/')[-1] 
                             + '_rec' + str(per_rec)
                            )
                pvmesh = load_mesh_vtk(k, 
                                       path2mesh,
                                       filenames,
                                       )
                
                # plot_TL(k,p)
                plot_TL_pv(pvmesh,k,clim=[-10,10],path=str(p_backup))

                # k.surveys
            

    pass

#%%
if __name__ == '__main__':
    
    args = get_cmd()   

    
    log_ERT = load_files(field=args.Location,test_name=args.TestName)
    filenames = ('../rawData/' + log_ERT['Location'] + '/' + log_ERT['Rawfile']).to_list()  
    # filenames[0]
    
    if log_ERT['Location'].unique() == 'Laghetti':
        _ = prepare_data(filenames)
        ftype = 'Syscal'
    
    if args.run_indiv==1:
        run_ERT(log_ERT,filenames,reprocess=args.reprocess)
    else:
        run_ERT_TL(log_ERT,filenames,invpath='../inversionERT_TL/',
               per_rec=args.recErr,TL_reg=args.TLreg)