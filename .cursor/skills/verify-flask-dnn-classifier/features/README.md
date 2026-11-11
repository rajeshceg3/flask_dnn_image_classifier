# Feature map: flask_dnn_image_classifier

Cats-vs-dogs VGG16 classifier demo.

- POST /predict (predict.py): JSON {image: base64} -> VGG16 .h5 model -> {result: {dog, cat}} probabilities. NOT runnable: model file absent.
- static/index.html: file picker previews image, posts base64 to /predict, prints both class probabilities. Fixed response-key contract mismatch.
