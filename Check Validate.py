__author__ = 'alex'
import numpy as np # importing numpy for work with matrices
import csv # importing csv to work with train_masks.csv
from PIL import Image # importing Image to work with *.tif
from os import listdir # importing listdir to work with bunch of files
from scipy.spatial import KDTree # importing KDTree for fast neigbor searching
from time import gmtime, strftime
import re

def dice_coefficient(x, y):
    if not(x.any() or y.any()):
        return 1
    return 2 * (x.astype(bool) * y.astype(bool)).sum() / (x.sum() + y.sum())

answers = {}
with open("train_masks.csv") as train_masks:
    reader = csv.reader(train_masks)
    for row in reader:
        # dictionary will contain answer for each file from directory "train"
        print(str(row[0]) + "_" + str(row[1]))
        answers[str(row[0]) + "_" + str(row[1]) + ".tif"] = row[2]
with open("sort_order_of_train.csv") as sort_order_of_train:
    num_of_line = -1
    for line in sort_order_of_train: # getting names of files from directory "train" in str
        num_of_line += 1
        if (num_of_line % 1001 == 0):
            file = "new_train/" + line[:-5] + '_mask.tif'
            image_array = np.array(Image.open(file))
            image_array = image_array.flatten()
            image_array = image_array.astype(int)
            found_answer += dice_coefficient(answers[line[:-5]], image_array)
print(found_answer)