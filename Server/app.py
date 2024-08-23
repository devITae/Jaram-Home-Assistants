# -- coding: utf-8 --

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)

# POST로 컬러 코드와 온오프 여부를 받아 저장하고, GET으로 저장된 데이터를 반환
turn = 'on'
color = '#FFFFFF'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST', 'GET'])
def api():
    global turn, color
    if request.method == 'POST':
        data = request.get_json()
        turn = data['turn']
        color = data['color']
        return jsonify(data)
    else:
        return jsonify({'turn': turn, 'color': color})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)
