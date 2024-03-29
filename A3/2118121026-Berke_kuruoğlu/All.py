# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wxHdbx1qe9mtJorHCaU0YhCscWs6nRCj
"""

from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os



model = load_model('trained_tf_model.h5')

# Define the classes
class_names = ['Glioma', 'Meningioma', 'Notumor', 'Pituitary']

# Specify the path of the test folder
test_folder_path = '/content/drive/MyDrive/test pic/a'  # Replace with the actual path

# Iterate over each file in the folder
for filename in os.listdir(test_folder_path):
    if filename.endswith(".jpg"):  # Select only JPEG files
        # Load and preprocess the image for model input
        img_path = os.path.join(test_folder_path, filename)
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Make predictions using the model
        predictions = model.predict(img_array)

        # Set thresholds for 'Notumor' and 'Tumor' classes
        notumor_threshold = 0.5
        tumor_threshold = 0.5

        # Print classification results
        print(f"Image: {filename}")

        if predictions[0][class_names.index('Notumor')] > notumor_threshold:
            print("Classification: Notumor\n")
        elif any(p > tumor_threshold for p in predictions[0][:-1]):  # Check for 'Glioma', 'Meningioma', 'Pituitary'
            print("Classification: Tumor\n")
        else:
            print("Uncertain Class\n")

import matplotlib.pyplot as plt

# Belirli yoğunluğa sahip piksellerin tespiti
image_path = "/content/drive/MyDrive/test pic/a/1 (2).jpeg"

# Görüntüyü oku
img = cv2.imread(image_path)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

yoğunluk_eşik = 150

# Belirli yoğunluğa sahip piksellerin tespiti
mask = (gray_image >= yoğunluk_eşik)

colored_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# maske yardımı ile boyama
colored_image[mask] = [255, 0, 0]  # Kırmızı renk: [R, G, B]

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(gray_image, cmap='gray')
plt.title('Orijinal Gri Tonlamalı Görüntü')

plt.subplot(122)
plt.imshow(colored_image)
plt.title(f'{yoğunluk_eşik} Yoğunluğa Sahip Bölgeler Kırmızıya Boyandı')

plt.show()

from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import cv2
import os
from google.colab.patches import cv2_imshow

# Load the segmentation model (replace 'trained_tf_model.h5' with the actual file path)
segmentation_model = load_model('trained_tf_model.h5')

# Specify the path of the image folder
image_folder_path = '/content/drive/MyDrive/test pic/a'

# Iterate over each file in the folder
for filename in os.listdir(image_folder_path):
    if filename.endswith(".jpg"):  # Select only JPEG files
        # Load and preprocess the image for model input
        img_path = os.path.join(image_folder_path, filename)
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Make predictions with the segmentation model
        segmentation_mask = segmentation_model.predict(img_array)


        # Resize the binary mask to match the dimensions of the original image
        original_img = cv2.imread(img_path)
        binary_mask_resized = cv2.resize(segmentation_mask, (original_img.shape[1], original_img.shape[0]))

        # Overlay the mask on the original image
        overlay_img = original_img.copy()
        overlay_img[binary_mask_resized > 0.5] = [0, 255, 0]  # Highlight tumor region in green

        # Display the result
        cv2_imshow(original_img)

        cv2_imshow( overlay_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()