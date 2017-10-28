# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 21:20:07 2017

@author: Swaroop.Padala
"""

import PIL.Image as Image
import os

#Run this script to resize images and save to the directory where the script is present

#Set the resize values
pixel_size_x = 227
pixel_size_y = 227

# WHICH FOLDER TO LOOK FOR
DEST_IMAGES_PREFIX = 'beans'

# PATH OF THE IMAGES THAT NEED TO BE RESIZED
source_images_path = "C:/Users/Swaroop.Padala/Desktop/HackerEarth_IndiaHacks_ML/a0409a00-8-dataset_dp/segregated_images/beans/"

# IF YOU WANT ORIGINAL NAME, SET THE VARIABLE resized_image_suffix = ''
resized_image_suffix = 'resized'

FILE_EXTENSION = 'PNG'
file_ext = '.png'

def resizeImage(infile, output_dir="", size=(pixel_size_x,pixel_size_y)):
     outfile = os.path.splitext(infile)[0]+resized_image_suffix
     extension = os.path.splitext(infile)[1]

     if ((extension > file_ext) - (extension < file_ext)):
        return

     if infile != outfile:
        try :
            im = Image.open(source_images_path+infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(output_dir+'/'+outfile+extension,FILE_EXTENSION)
        except IOError as e:
            print (e)

if __name__=="__main__":
    output_dir = DEST_IMAGES_PREFIX+"_resized_images_"+str(pixel_size_x)+'X'+str(pixel_size_y)    
    
    dir = os.getcwd()

    if not os.path.exists(os.path.join(dir,output_dir)):
        os.mkdir(output_dir)

    for file in os.listdir(source_images_path):
        resizeImage(file,output_dir)
