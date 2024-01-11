# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:28:37 2024

@author: berkekuruoglu
"""

from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os

# Eğitilmiş modeli yükleyin
model = load_model('trained_tf_model.h5')

# Test etmek istediğiniz klasörün yolunu belirtin
test_folder_path = 'C:\\Users\\msi\\Desktop\\test pic'  # Test klasörünün gerçek adını ve yolunu ekleyin

# Klasördeki her bir dosyayı gezin
for filename in os.listdir(test_folder_path):
    if filename.endswith(".jpg"):  # Sadece JPEG dosyalarını seçmek için
        # Görseli modelin beklentiye uygun şekilde yükleyin ve ön işleme yapın
        img_path = os.path.join(test_folder_path, filename)
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Model üzerinde sınıflandırma yapın
        predictions = model.predict(img_array)

# Sınıfların özel isimlerini belirtin (örnek olarak)
        class_names = ['Glioma', 'Meningioma', 'Notumor', 'Pituitary']
        # Sınıflandırma sonuçlarını ekrana yazdırın
        print(f"Görsel: {filename}")
        for i, score in enumerate(predictions[0]):
            print(f"{class_names[i]}: yakınlık değeri: {score:f}")
        print("\n")
        
        

    
