# testing geocoordinate validation
# points taken in the household are render in the 
# polygon result from 4 points taken at 4 extreme 
# corners (boundaries) of the community

# import all relevant packages
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

#change directory
os.chdir("D\NSR\Geos)

#read data set that contains households geocoordinate
community_pts = pd.read_csv("community_pts.csv")