import h5py
import cv2
from keras.models import load_model
import numpy as np

def diagnose(img_path=None, img_file=None):
    '''
    Given an image path or file for an x-ray, uses a trained convnet to
    predict a diagnosis for Pneumonia

    Takes: image path or file
    Returns: negative ('0' or 'normal') or positive ('1' or 'pneumonia')
    '''

    # loading the image
    if img_path:
        img = cv2.imread(img_path)
    elif type(img_file) is np.ndarray:
        img = img_file
    else:
        return "No image path of image file was given"

    # loading the model
    model = load_model("notebooks/my_model_it3.h5")

    # convert from images with 3 channels to greyscale 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img[..., np.newaxis]

    # reshape image to size used to train the model
    img = cv2.resize(img, (250,250))

    # normalize the img array for better model performance
    img = img.astype(np.float32)/255

    # reshape so model understands image is greyscale and has
    # 4 dims (required by trined model)
    img = img[..., np.newaxis]
    img = img.reshape((1,) + img.shape)
    
    # predict
    diagnosis_pred = (model.predict(img) > 0.5).astype("int32")

    # convert diagnosis to str result
    if diagnosis_pred[0][0] == 0:
        result = "negative"
    elif diagnosis_pred[0][0] == 1:
        result = "positive"
    
    # return first element in the array
    return result