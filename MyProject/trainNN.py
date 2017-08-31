from scipy import io
import cv2

#Change all image into 500*500
#number of cluster = 120
#dimenstion of Superpixel = 80*80

#data structure of DataColor
#first dimention: Color or Grey
#second dimention: which pitures
#third dimention: which layers
#forth dimention: which superpixels

#data structure of maxCluster
#number of maxCluster in layer:1,2,3


dataSet = io.loadmat('ProduceDataSet/Data.mat')
DataColorSet = dataSet['Color']
DataGreySet = dataSet['Grey']
maxCluster = dataSet['maxClustLayer']
print(maxCluster)

cv2.imwrite("img1.jpg",DataColorSet[2][0][40])
cv2.imwrite("img2.jpg",DataColorSet[2][0][41])
cv2.imwrite("img3.jpg",DataColorSet[2][0][42])
cv2.imwrite("img4.jpg",DataColorSet[2][0][43])
cv2.imwrite("img5.jpg",DataColorSet[2][1][20])
cv2.imwrite("img6.jpg",DataColorSet[2][1][21])
cv2.imwrite("img7.jpg",DataColorSet[2][2][10])
cv2.imwrite("img8.jpg",DataColorSet[2][2][11])

cv2.imwrite("greyimg1.jpg",DataGreySet[2][0][40])
cv2.imwrite("greyimg2.jpg",DataGreySet[2][0][41])
cv2.imwrite("greyimg3.jpg",DataGreySet[2][0][42])
cv2.imwrite("greyimg4.jpg",DataGreySet[2][0][43])
cv2.imwrite("greyimg5.jpg",DataGreySet[2][1][20])
cv2.imwrite("greyimg6.jpg",DataGreySet[2][1][21])
cv2.imwrite("greyimg7.jpg",DataGreySet[2][2][10])
cv2.imwrite("greyimg8.jpg",DataGreySet[2][2][11])



