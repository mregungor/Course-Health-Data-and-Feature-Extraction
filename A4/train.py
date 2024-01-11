import tensorflow as tf
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('./'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df=pd.read_csv('processed-data.csv')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.linear_model import LinearRegression

# Eğitim için hedef belirleme
target = 'Difficulty-in-Breathing'
X = df.drop(target , axis= 1)
y= df[target]

#Ölçeklendirme işlemi
scaler = MinMaxScaler()

X = scaler.fit_transform(X)
y = scaler.fit_transform(y.values.reshape(-1 , 1))

#Eğitim ve test verilerinin ayarlanması
X_train , X_test , y_train , y_test = train_test_split(X, y , test_size = 0.2 , random_state = 42)

from sklearn.metrics import mean_absolute_error
y_mean = y_train.mean()
y_pred_baseline= [y_mean] * len(y_train)

#Sinir ağı oluşturma işlemi
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=18))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error', 'acc', tf.keras.metrics.F1Score(), tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])
model.summary()

#Modelin eğitilmesi , sonuçların değerlendirilmesi ve kaydedilmesi
history = model.fit(X_train , y_train , epochs=20 , validation_split=0.2)
loss, mae, acc, f1, precision, recall = model.evaluate(X_test, y_test, verbose=1)
model.save('model.keras')