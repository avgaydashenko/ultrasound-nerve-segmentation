import scipy.misc
import glob, os
import numpy as np
from PIL import Image


retval = os.getcwd()
os.chdir(retval + "\\" + "train")
sum = np.zeros((420, 580))

size=0
for f in glob.glob("*_*_*.tif"):
    size += 1
    image_array = np.array(Image.open(f))
    sum += image_array
        
sum = (sum / size)
scipy.misc.imsave('answer.jpg', sum.astype(int))

