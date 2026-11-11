---
name: verify-flask-dnn-classifier
description: Verify the flask cats-vs-dogs classifier's source, route and frontend/backend contract; the trained model file is absent from the repo, so boot and prediction remain an honestly recorded boundary.
---
# Flask DNN classifier verification

## Launch
Flask app: predict.py (POST /predict, base64 image JSON in, {result:{dog,cat}} out). Page: static/index.html (file input, jQuery POST to hardcoded http://localhost:5000/predict).

## Doctor + Drive
`python3 .cursor/skills/verify-flask-dnn-classifier/verify.py` (stdlib only): parses predict.py (ast), asserts the /predict handler exists, checks the page form elements and the frontend/backend response-key contract (`response.result.*` matching jsonify's {result: ...}). FAILURES=0 exit 0.

## Evidence
Runner output. No server boot: impossible without the model.

## Known boundaries (blocking)
- VGG16_cats_and_dogs.h5 (trained model) is NOT in the repo and has no documented source; fetch_model() runs at import, so the app cannot boot and no prediction can be verified.
- requirements.txt unpinned (Flask/Keras/Pillow/numpy): the code uses keras.preprocessing.image, removed in Keras 3 - it needs TF/Keras 2.x pins to run.
- The page posts to hardcoded http://localhost:5000 and the Flask app defines no / route and no CORS, so the page must be opened separately against a locally running server.
- Repaired in this rollout: frontend read response.prediction.* while the backend returns {result: ...}; now response.result.*.
