#!/usr/bin/env python3
"""Verify what's verifiable of flask_dnn_image_classifier without the missing model file."""
import ast, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
failures = []
def check(name, cond, detail=''):
    print(('PASS' if cond else 'FAIL'), name, detail)
    if not cond: failures.append(name)
src = open(os.path.join(ROOT, 'predict.py')).read()
tree = ast.parse(src)  # raises on syntax error
check('predict-syntax', True)
check('predict-route', any(isinstance(n, ast.FunctionDef) and n.name == 'predict' for n in ast.walk(tree)))
check('model-load-at-import', 'fetch_model()' in src, 'crashes without VGG16_cats_and_dogs.h5')
model = os.path.exists(os.path.join(ROOT, 'VGG16_cats_and_dogs.h5'))
print('INFO model-file-present:', model)
html = open(os.path.join(ROOT, 'static', 'index.html')).read()
check('page-has-form', 'img-select' in html and 'pred-btn' in html)
# frontend/backend contract: backend returns {result:{dog,cat}}
check('response-key-contract', 'response.result.dog' in html and 'response.result.cat' in html,
      'frontend must read response.result.* to match jsonify({result: ...})')
print('FAILURES=%d' % len(failures))
sys.exit(0 if not failures else 1)
