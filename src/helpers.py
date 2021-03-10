import cv2
import os
import numpy as np
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
from progressbar import ProgressBar
import re

def load_images(path = "../data/chest_xray/chest_xray/", size = (250,250)):
    '''
    Given a directory path and output size, returns the images in a numpy array format
    
    Takes: directory path and output image size
    Returns: array with images in directory converted to greyscale and numpy array format
    '''
    # check if defined size is correct
    if (len(size) != 2) or (type(size) != tuple):
        return "Size should be a tuple with length 2."
    else:
    
        # labels for images, NORMAL will be 0 and PNEUMONIA will be 1
        labels = ['NORMAL', 'PNEUMONIA']

        # lists to insert the data and the labels
        img_list = []
        label_list = []

        # iterate through directories and load each of the two sets of images (normal and pneumonia)
        for l in labels:
            
            pbar = ProgressBar()
            for file in pbar(os.listdir(path + l)):
                
                # check extension to make sure we just load images, ignore the rest
                if file.split(".")[-1].lower() in {"jpeg", "jpg", "png"}:

                    # load images
                    img = cv2.imread(os.path.join(path + l, file))

                    # convert from images with 3 channels to greyscale
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    # reshape image to a common size so all inputs are equal
                    img = cv2.resize(img, size)

                    # normalize the img array for better model performance
                    img = img.astype(np.float32)/255

                    # create list with labels, NORMAL will be 0 and PNEUMONIA will be 1
                    label = labels.index(l)

                    # save image and label in corresponding list
                    img_list.append(img)
                    label_list.append(label)
        
        img_arr = np.array(img_list)
        label_arr = np.array(label_list)

        # include an additional dimension = 1 so model understands image is greyscale
        img_arr = img_arr[..., np.newaxis]
        
        #vectorizing the data to make it ready for the model
        return img_arr, label_arr


def shuffle_arrays(arr_1, arr_2):
    '''
    Given two numpy arrays with the same dimension, shuffles them maintaining the same relative order
    
    Takes: two numpy arrays
    Returns: two shuffled numpy arrays
    '''
    
    # check if the arrays have the same dimension 
    if arr_1.shape[0] != arr_2.shape[0]:
        return f"Arrays should have the same dimension, but have dimension {arr_1.shape[0]} and {arr_2.shape[0]} instead", "see error in index 1"
    else:
        # create a 1D array that with as many elements as the dimension of the input arrays
        s = np.arange(arr_1.shape[0])
        
        # shuffle the array to serve as index for input arrays
        np.random.shuffle(s)
        
        # adjust input arrays
        arr_1 = arr_1[s]
        arr_2 = arr_2[s]
        
    return arr_1, arr_2

def load_augment_images(path = "../data/chest_xray/chest_xray/", size = (250,250), augment_label=None, n_augments_per_img=2):
    '''
    Given a directory path, output size, label to augment and number of augmented images to generate per original
    image, returns the images in a numpy array format
    
    Takes: directory path, output image size, label to augment and number of augmented images to generate per original
    Returns: array with images in directory plus augmented images, converted to greyscale and numpy array format
    '''
    # check if defined size is correct
    if (len(size) != 2) or (type(size) != tuple):
        return "Size should be a tuple with length 2."
    else:
    
        # labels for images, NORMAL will be 0 and PNEUMONIA will be 1
        labels = ['NORMAL', 'PNEUMONIA']

        # lists to insert the data and the labels
        img_list = []
        label_list = []

        # iterate through directories and load each of the two sets of images (normal and pneumonia)
        for l in labels:
            
            pbar = ProgressBar()
            for file in pbar(os.listdir(path + l)):
                
                # check extension to make sure we just load images, ignore the rest
                if file.split(".")[-1].lower() in {"jpeg", "jpg", "png"}:

                    # load images
                    img = cv2.imread(os.path.join(path + l, file))

                    # convert from images with 3 channels to greyscale
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    # reshape image to a common size so all inputs are equal
                    img = cv2.resize(img, size)

                    # normalize the img array for better model performance
                    img = img.astype(np.float32)/255

                    # create list with labels, NORMAL will be 0 and PNEUMONIA will be 1
                    label = labels.index(l)

                    # include an additional dimension = 1 so model understands image is greyscale
                    img = img[..., np.newaxis]
                    
                    # save image and label in corresponding list
                    img_list.append(img)
                    label_list.append(label)
                    
                    # check if img label is defined to be agumented, and if so, generate image
                    if augment_label != None and augment_label not in labels:
                        return f"Unexpected augment label. Should be {labels[0]} or {labels[1]}"
                    elif augment_label == l:
                        train_datagen = ImageDataGenerator(
                            rotation_range=30,
                            zoom_range=0.1,
                            horizontal_flip=True,
                            brightness_range=(0.7, 1.5))
                        # reshape required for data augmentation
                        img = img.reshape((1,) + img.shape)
                        i = 0
                        for batch in train_datagen.flow(x = img, batch_size=1):
                            aug_img = batch[0]
                            img_list.append(aug_img)
                            label_list.append(label)
                            i += 1
                            if i % n_augments_per_img == 0:
                                break
                            
        #vectorizing the data to make it ready for the model
        img_arr = np.array(img_list)
        label_arr = np.array(label_list)
        
        return img_arr, label_arr

def check_email(email):
    '''
    Given a string, checks if it has a valid email format or not.

    Takes: string
    Returns: True or False 
    '''
    
    # defining email format
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    # check if string follows regex pattern
    if(re.search(regex,email)):  
        return True      
    else:  
        return False

