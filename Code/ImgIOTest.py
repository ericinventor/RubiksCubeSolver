import numpy as numpy
from PIL import Image

img = Image.open("some_file_name.jpg")
arr = numpy.array(img)
print(arr.shape)
newImg = Image.fromarray(arr)
newImg.save("some_other_file_name.jpg")