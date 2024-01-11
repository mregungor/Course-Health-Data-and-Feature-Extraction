# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:28:37 2024

@author: berkekuruoglu
"""

import tensorflow

# VGG16 is a pre-trained CNN model. 
conv_base = tensorflow.keras.applications.VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(224, 224, 3)
                  )

# Showing the convolutional layers.
conv_base.summary()

# Deciding which layers are trained and frozen.
# Until 'block5_conv1' are frozen.
conv_base.trainable = True
set_trainable = False
for layer in conv_base.layers:
    if layer.name == 'block5_conv1':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False

# An empyty model is created.
model = tensorflow.keras.models.Sequential()

# VGG16 is added as convolutional layer.
model.add(conv_base)

# Layers are converted from matrices to a vector.
model.add(tensorflow.keras.layers.Flatten())

# Our neural layer is added.
model.add(tensorflow.keras.layers.Dense(256, activation='relu'))
model.add(tensorflow.keras.layers.Dense(4, activation='softmax'))

model.compile(loss='binary_crossentropy',
              optimizer=tensorflow.keras.optimizers.RMSprop(lr=1e-5),
              metrics=['acc'])

# Showing the created model.
model.summary()

# Defining the directories that data are in.
train_dir = ('C:\\Users\\msi\\Desktop\\tensorflow\\veriler\\train')
validation_dir = ('C:\\Users\\msi\\Desktop\\tensorflow\\veriler\\validation')
test_dir = ('C:\\Users\\msi\\Desktop\\tensorflow\\veriler\\test')

# We need to apply data augmentation methods to prevent overfitting.
train_datagen = tensorflow.keras.preprocessing.image.ImageDataGenerator(
      rescale=1./255, # piksel değerleri 0-255'den 0-1 arasına getiriliyor.
      rotation_range=40, # istenilen artırma işlemleri yapılabilir.
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest'
      )

train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(224, 224),
        batch_size=20,
        )

# To validate the training process, we do not need augmented images.
validation_datagen = tensorflow.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255
        )

validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(224, 224),
        batch_size=20,
        )

# Training the model.
history = model.fit_generator(
      train_generator,
      steps_per_epoch=100,
      epochs=50,
      validation_data=validation_generator,
      validation_steps=5)

# Saving the trained model to working directory.
model.save('trained_tf_model.h5')

# To test the trained model, we do not need augmented images.
test_datagen = tensorflow.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255
        )

test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(224, 224),
        batch_size=20,
        )
#0.28tra  // 0.25 val 

# Printing the test results.
test_loss, test_acc = model.evaluate_generator(test_generator, steps=50)
print('test acc:', test_acc)
#0.3179999887943268 test
