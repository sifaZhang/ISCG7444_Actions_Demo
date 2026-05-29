import flask
import json
from flask import jsonify

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'API works!'

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
