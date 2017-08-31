from getData import *
from scipy import io

#Change all image into 500*500
#number of cluster = 120
#dimenstion of Superpixel = 80*80


#data structure of DataColor and DataGrey
#first dimention: Color or Grey
#second dimention: which pitures
#third dimention: which layers
#forth dimention: which superpixels

#data structure of maxCluster
#number of maxCluster in layer:1,2,3

path="Images"
maxCluster, DataColorSet, DataGreySet = getDataSet(path)
data={'Color':DataColorSet, 'Grey':DataGreySet, 'maxClustLayer':maxCluster}
io.savemat('Data.mat',data)


