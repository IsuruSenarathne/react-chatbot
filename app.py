from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return jsonify("hello")
        
    if request.method == 'POST':
        res = json.loads(request.data.decode())
        res = dict(res)['data']['text']
        if 'hi' in str(res).lower():
            return jsonify('hello')
        else:
            return jsonify('Hi isuru, how can i help you with')

if __name__ == '__main__':
    app.run(debug=True)
    
"""
FLASK_DEBUG=1
set FALSK_APP=app.py
flask run
"""