# -- coding: utf-8 --

from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5002, debug=True)
