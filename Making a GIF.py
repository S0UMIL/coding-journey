import imageio
import imageio.v3 as iio
filenames = ['raghav-1.jpg', 'raghav-2.jpg'] # these are the file names writing them down in a list
images = [] # creating a variable for the images to go into
for filename in filenames:#filename is a temporary variable that holds each item from filenames as the loop iterates.
    images.append(iio.imread(filename)) #.imread is used to load an image based on file path so now the variable we created for image will be activated
iio.imwrite('raghav.gif',images, duration = 500 ,loop = 0) #used to turn images into gif
