# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:46:21 2017

@author: Swaroop.Padala
"""

#from multiprocessing import Pool
import os, sys
import csv
from shutil import copyfile

def main():
    # Creating directories for all the classes or categories the images need to be segregated into
    directories = ["beans","cake","candy","cereal","chips","chocolate","coffee","corn","fish","flour","honey","jam","juice","milk","nuts","oil","pasta","rice","soda","spices","sugar","tea","tomatosauce","vinegar","water"]
    root = "C:/Users/Swaroop.Padala/Desktop/HackerEarth_IndiaHacks_ML/a0409a00-8-dataset_dp/"    
    path1 = "train_img/"   
    #path2 = ""  
    count = 0
    for directory in directories:
        if not os.path.exists(root +"\\segregated_images\\" +directory):
            os.makedirs(root+"\\segregated_images\\"+ directory)
        
    train_images_listing = os.listdir(root + path1)   
    
    #Specify the csv file
    reader = csv.reader(open(root + 'train.csv', 'r'))
    d = {}
    for row in reader:
       k, v = row
       d[k+".png"] = v
    
    for image in train_images_listing:
        copyfile(root + path1 + image, root +"\\segregated_images\\" + d[image]+"\\" + image) 
        count += 1
        print (count)
        
if __name__ == "__main__":
    main()
