__author__ = 'alex'

import csv # importing csv to work with train_masks.csv

answers = []
with open("train_masks.csv") as train_masks:
    reader = csv.reader(train_masks)
    for row in reader:
        tup = (str(row[0]) + "_" + str(row[1]) + ".tif",len(row[2].split()))
        answers.append(tup)
    answers.sort(key=lambda tup: tup[1])
f = open('sort_order_of_train.csv', 'w+')
for tup in answers:
    f.write(str(tup[0])+'\n')
