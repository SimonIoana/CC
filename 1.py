import json
from flask import Flask, jsonify, request, make_response
from flask import abort

app = Flask(__name__)
notes = [
{
   'id': 'today',
   'content': 'today is content',
   'date': 'date'
},
{
   'id': 'yesterday',
   'content' : 'yesterday is content',
   'date' : 'date'
}
]
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/GET/notes', methods=['GET'])
def get_notes():
    return jsonify({'notes': notes})

@app.route('/GET/notes/<string:note_id>', methods=['GET'])
def get_note(note_id):
    note = [note for note in notes if note['id'] == note_id]
    if len(note) == 0:
        abort(404)
    return jsonify({'note': note[0]})

@app.route('/GET/notes?limit=3', methods=['GET'])
def get_note_limit():
    lim = 0
    con = 0
    if 'limit' in request.args:
        lim = 1
        limit = int(request.args['limit'])
    if 'content' in request.args:
        con = 1
        content = request.args['content']
    l = []
    for item in notess:
        if con == 1 and not (item['content'].startswith(content)):
            continue
        l.append(item)
        if lim == 1:
            limit -= 1
            if limit == 0:
                break
    if len(l) == 0:
        return make_response('content is empty', status=204)
    else:
        return make_response(json.dumps(l), status=200)

@app.route('/POST/notes', methods=['GET','POST'])
def create_note():
    note = {
        'id': 'tomorrow',
        'content': 'tomorrow is content',
        'date': 'date'
           }
    notes.append(note)
    return jsonify({'note': note}), 201

@app.route('/DELETE/notes/<string:note_id>', methods=['GET', 'POST', 'DELETE'])
def delete_notes(note_id):
    note = [note for note in notes if note['id'] == note_id]
    if len(note) == 0:
        abort(404)
    notes.remove(note[0])
    return jsonify({'result': notes})

notess=[
{
   'id': 'today',
   'content': 'today is content',
   'date': 'date',
   'photos': [
       {
        'id': 'cat.jpg',
		'uploadDate': 'date',
		'content': 'content'
	   }
             ]
}
]

@app.route('/GET/notess/today/photos', methods=['GET'])
def afisareImg():
    with open("cat.jpg", "r+") as f:
        data = f.read()
    return data


if __name__ == '__main__':
        app.run(debug=True)