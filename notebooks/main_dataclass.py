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

@dataclass
class ERT:
    filenames: str|list
    filepath: str
    reg_type: int = 1
    recip: int = 5 # reciprocal filter threshold value

    
    # def run_ERT(path: str, filename: str, recip: str):
    def run_ERT(self, invpath:str = './inversionERT/'):
        k = Project(invpath + self.filename, typ="R3t")
        k.createSurvey(self.filepath, ftype="Syscal")
        k.filterRecip(percent=self.recip)
        
        return k
        
    
    
def filter_log(log,field,test_name):
    log = log[log['Location']==field]
    log = log[log['Test name']==test_name]
    return log

    
def load_files(
                logfile='../Log_Laghetti_Salorno_river_updated.csv',
                field='Laghetti',
                test_name='LAGHETTI1',                
            ):
    
    log = pd.read_csv(logfile)
    log_filtered = filter_log(log,field,test_name)
     
    return log_filtered




    pass

def run_ERT_TL():
    
    pass


if __name__ == '__main__':
    
    
    log_ERT = load_files()
    
    filename = log_ERT['Rawfile'].iloc[0] + '.csv'
    path = str(Path('../rawData/') / log_ERT['Location'].iloc[0])
    processERT =  ERT(path+filename)
    processERT.run_ERT()
    
    # /home/ben/Documents/GitHub/BenjMy/Salorno_Laghetti_river/rawData/Laghetti/April/
    
    # run_ERT()
    
    # run_ERT_TL()