import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from calories import calorie_dict

model = tf.keras.models.load_model("food_model.h5")

classes = ["pizza", "steak"]

def predict_food(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)/255
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    index = np.argmax(prediction)
    food_name = classes[index]

    calories = calorie_dict.get(food_name, "Unknown")

    return food_name, calories