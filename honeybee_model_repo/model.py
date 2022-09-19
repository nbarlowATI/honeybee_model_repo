import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Activation,Dropout,Conv2D, MaxPooling2D,BatchNormalization
from tensorflow.keras.optimizers import Adam, Adamax
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras import regularizers
from tensorflow.keras.models import Model
# pprevent annoying tensorflow warning
import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
import warnings
#pd.set_option('max_columns', None)
#pd.set_option('max_rows', 90)
warnings.simplefilter("ignore")


class efficientNetB3:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__),'bees_95.55.h5')
        self.model = tf.keras.models.load_model(model_path)
        self.model = None

    def predict(self, image: np.ndarray):
        return self.model.predict(image)
