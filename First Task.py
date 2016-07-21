
# coding: utf-8

# In[3]:

import numpy as np # importing numpy for work with matrices
import csv # importing csv to work with train_masks.csv
from PIL import Image # importing Image to work with *.tif
from os import listdir # importing listdir to work with bunch of files
from scipy.spatial import KDTree # importing KDTree for fast neigbor searching
from time import gmtime, strftime

print("imports")


# In[2]:

answers = {}
with open("train_masks.csv") as train_masks:
    reader = csv.reader(train_masks)
    for row in reader:
        # dictionary will contain answer for each file from directory "train"
        answers[str(row[0]) + "_" + str(row[1]) + ".tif"] = row[2]
        
print("answers")


# In[4]:

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


# In[5]:

train = []
train_filenames = []
with open("sort_order_of_train.csv") as train_masks:
    num_of_line = -1
    for line in train_masks: # getting names of files from directory "train" in str
        num_of_line += 1
        if (num_of_line % 100 == 0):
            file = "new_train/" + line[:-1]
            train_filenames.append(file)
            image_array = np.array(Image.open(file))
            image_array = image_array.flatten()
            image_array = image_array.astype(int)
            train.append(list(image_array))

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("train")
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

test = []
test_filenames = []

with open("sort_order_of_train.csv") as train_masks:
    num_of_line = -1
    for line in train_masks: # getting names of files from directory "train" in str
        num_of_line += 1
        if (num_of_line % 1001 == 0):
            file = "new_train/" + line[:-1]
            image_array = np.array(Image.open(file))
            image_array = image_array.flatten()
            image_array = image_array.astype(int)
            test.append(list(image_array))
            test_filenames.append(file)

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("test")


# In[12]:

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


# In[13]:

tree = KDTree(train, leafsize=200)
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("tree")


# In[19]:

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


# In[20]:

indeces = tree.query(test, p=1)[1]
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("indeces")


# In[22]:

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


# In[23]:

result = []
for i in np.arange(len(test_filenames)):
    row = [int(test_filenames[i][:-4]), answers[train_filenames[indeces[i]]]]
    result.append(row)
result.sort()

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("result")


# In[24]:

with open("submission.csv", "w") as submission:
    writer = csv.writer(submission)
    writer.writerow(['img', 'pixels'])
    writer.writerows(result)
    
print("done")


# In[ ]:



