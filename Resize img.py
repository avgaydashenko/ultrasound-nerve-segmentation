__author__ = 'alex'
from PIL import Image
import numpy as np
import os
from os import listdir
from scipy import spatial

for f in listdir('train_/'):
    img =Image.open('train/'+f)
    img.resize((145, 105), Image.ANTIALIAS)
    img.save("new_test/"+f, optimaze = True, quality = 95)