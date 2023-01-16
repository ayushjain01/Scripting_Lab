import numpy as np
from PIL import Image, ImageFilter

inputImage = r"./input.jpg"
outputImage = r"./output.jpg"

print("Starting Image Histogram Equalization...")
#Open the image
img = Image.open(inputImage)

#Convert the image to grayscale
imgGray = img.convert(mode='L')

#Convert the image to a numpy array
imgArray = np.asarray(imgGray)

#Generating the normalized cumulative histogram 
hArray = np.bincount(imgArray.flatten(), minlength=256)
num_pixels = np.sum(hArray)
hArray = hArray/num_pixels
cArray = np.cumsum(hArray)

#Generate pixel mapping lookup table
transformMap = np.floor(255 * hArray).astype(np.uint8)

#Flatten image array into 1D list
imgList = list(imgArray.flatten())

#Transform pixel values to equalize
eqImgList = [transformMap[p] for p in imgList]

#Reshaping
eqImgArray = np.reshape(np.asarray(eqImgList), imgArray.shape)

print("Image Equalization Completed.")

#Converting NumPy array to Pillow Image and write to file
eqImg = Image.fromarray(eqImgArray, mode='L')

#Detecting Edges
print("Detecting Edges...")
image = imgGray.filter(ImageFilter.FIND_EDGES)

#Saving the Image Under the name
print("Saving Image")
image.save(outputImage)

