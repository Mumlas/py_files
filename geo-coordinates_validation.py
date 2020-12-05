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
household_pts = pd.read_csv("household_pts.csv")

#read the four points that form the community polygon
community_pts = pd.read_csv("community_pts.csv")

#Convert the points into lines and join the lines to form the polygon
