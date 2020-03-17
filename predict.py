import base64
import io
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

def fetch_model():
    global model
    model = load_model('VGG16_cats_and_dogs.h5')
    print(" Model fetched")

def prepare_image(image, desired_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(desired_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

fetch_model()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded_img = message['image']
    decoded_img = base64.b64decode(encoded_img)
    image = Image.open(io.BytesIO(decoded_img))
    final_img = prepare_image(image, desired_size=(224, 224))    
    result = model.predict(final_img).tolist()

    response = {
        'result': {
            'dog': result[0][0],
            'cat': result[0][1]
        }
    }
    return jsonify(response)
