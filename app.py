from flask import Flask, request
app = Flask(__name__)
import json
data_file = 'data.json' 

LIST_SIZE = 100
SECRET_TOKEN = '3r4564q349nm88'

def data_obj():
    with open(data_file, 'r') as f:
        return json.loads(f.read())

def write_obj(o):
    with open(data_file, 'w') as f:
        f.write(json.dumps(o))

@app.route('/getScores')
def getScores():
    obj = data_obj()
    response = app.response_class(
        response=json.dumps(obj),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/viewScores')
def viewScores():
    obj = data_obj()
    return '<html><head></head><body>' + \
        ''.join(['<div><b>{}</b>: {}</div>'.format(d['name'], d['score']) for d in obj]) + \
        '</body></html>'

@app.route('/submit', methods=['POST'])
def submitScore():
    name = request.form.get('name')
    score = request.form.get('score')
    token = request.form.get('token')
    if not name or not score or not token or token != SECRET_TOKEN:
        return 'Error'
    obj = data_obj()
    obj.append({'name': name, 'score': score})
    obj = sorted(obj, key=lambda d: d['score'], reverse=True)[:LIST_SIZE]
    write_obj(obj)
    return '{}: {}'.format(name, score)
