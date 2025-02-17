# -*- coding: utf-8 -*-

import os
import sys 
import fiona
import pandas as pd 
from geopandas import read_file

script_path = os.path.dirname(__file__)
sys.path.append(os.path.join(script_path,".."))

from movingpandas.trajectory import Trajectory


if __name__ == '__main__':       
    df = read_file(os.path.join(script_path,'demodata_geolife.gpkg'))
    df['t'] = pd.to_datetime(df['t'])
    df = df.set_index('t')       
    trajectories = []
    for key, values in df.groupby(['trajectory_id']):
        trajectories.append(Trajectory(key, values))        
        
    intersections = []            
    polygon_file = fiona.open(os.path.join(script_path,'demodata_grid.gpkg'), 'r')
    for feature in polygon_file:
        for traj in trajectories:
            for intersection in traj.intersection(feature):
                intersections.append(intersection)
        
    for intersection in intersections:
        print(intersection)
        
    polygon_file.close()
    
    