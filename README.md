# SLICdataFeature
First, change directory to MyProject/ProduceDataSet.

Second, run $: python3 run.py #to produce the MAT file and the data structure of MAT file was describe in run.py.

Third, change directory to MyProject.

Forth, run $: python3 trainNN.py #to produce the image feature in each layer.


img1-4: the feature in layer one with cluster number 1,2,3,4.

img5: the feature in layer two with combining img1 and img2.

img6: the feature in layer two with combining img3 and img4.

img7: the feature in layer three with combining img5 and img6.

greyimg: the greyscale version of img.




Next Progess, Train a stronger MAT file with more images.

PS: Do you have any website can downloads a ton of images? (smt like 1000images, no need click with one by one).

After the MAT file form, I will try to build the CNN with the algorithm you told me Tuesday.(I am learning now).
