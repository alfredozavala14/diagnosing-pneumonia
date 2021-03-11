![Header](images/doctor-with-xray.jpg)


# diagnosing-pneumonia

## Introduction

As the data analytics Ironhack bootcamp comes to an end, we are faced with the task of developing our final projects to work on some of the skills learned during the past eight weeks. One of these skills is training neural networks to classify images, which is the primary objective of this project. Through supervised learning, I will develop a deep learning model that takes chest X-rays and diagnoses Pneumonia.

As a starting point for this project, I have used a [kaggle dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) containing almost 6,000 X-Ray images (JPEG) divided into 2 categories (Pneumonia/Normal). This is a summary of the downloaded images:

[Dowloaded data]("images/train-cases-downloaded-from-kaggle.png")

## Work done

As the backbone of the project, I have trained three convolutional networks. To assess each one, I used accuracy as a validation metric to train the model, but then looked at precision and recall as well.
    - The first one was a simple convnet with the data dowloaded from Kaggle used directly (with minimal treatment to make it feedable to the network.
    - The second iteration included data augmentation techniques to create more "normal" images and also included dropout.
    - For the third try, seeing that the second iteration showed no improvement, I didn't use dropout so I could see if data augmentation alone made a better convnet.
    
These are the accuracy, loss, precision and recall results:

[cnn summary results]("images/cnn-results-summary.png")

Once I had a relatively robust CNN, I was able to develop a diagnosis function and then work on improving the customer experience:
    - I created an APP using Streamlit so that users could upload their personal info and x-rays
    - I used FPDF to automate the creation of diagnosis reports
    - I used smtplib to automate sending an email to each client with the results of the diagnosis

## Deliverables

The main deliverable is a working website (working on my local computer) with the ability to diagnose Pneumonia through an X-ray


## Next steps

As next steps, I would like to include the following:
- A whatsapp alternative to the email , with the user chosing the preferred option on the API
- A deployed API, through heroku or an alternative provider
- A better CNN, using the power of pre-trained models
- A connection with SQL so that I could keep a record of client submissions and results
- A more detailed report, including possible treatments for pneumonia in case of a positive diagnosis

## Libraries used

During the project, I have used the following libraries:
- [Keras](https://keras.io/api/)
- [Tensorflow](https://www.tensorflow.org/api_docs)
- [OpenCV](https://docs.opencv.org/master/)
- [h5py](https://docs.h5py.org/en/stable/)
- [Streamlit](https://docs.streamlit.io/en/stable/api.html)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [FPDF](https://pyfpdf.readthedocs.io/en/latest/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/doc/)
- [Sklearn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org/stable/contents.html)
- [Seaborn](https://seaborn.pydata.org/)
- [os](https://docs.python.org/3/library/os.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [regex](https://docs.python.org/3/library/re.html)
- [progressbar]()

## Links & Resources

```- [Name of link](url)
