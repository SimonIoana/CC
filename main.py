import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import request

@app.route('/create', methods=['POST'])
def create_notes():
    try:
        _json = request.json
        _userId = _json['userId']
        _noteTitle = _json['noteTitle']
        _noteDescription = _json['noteDescription']

        sqlQuery = "INSERT INTO notes(userId, noteTitle, noteDescription) VALUES(%s, %s, %s)"
        data = (_userId,  _noteTitle, _noteDescription)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        conn.commit()
        res = jsonify({
            "userId":_userId,
            "noteTitle":_noteTitle,
            "noteDescription":_noteDescription
        })
        res.status_code = 200
        return res
    except Exception as e:
        print(e)


@app.route('/notes')
def notes():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM notes")
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200
        return res
    except Exception as e:
        print(e)

@app.route('/updatenotes/', methods=['PUT'])
def update_notes():
    try:
        _json = request.json
        _userId = _json['userId']
        _notesId = _json['notesId']
        _noteTitle = _json['noteTitle']
        _noteDescription = _json['noteDescription']

        sql = "UPDATE notes SET userId=%s, noteTitle=%s, noteDescription=%s WHERE notesId=%s"
        data = (_userId, _noteTitle, _noteDescription, _notesId)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        res = jsonify({
            "userId":_userId,
            "noteTitle":_noteTitle,
            "noteDescription":_noteDescription,
            "notesId":_notesId
        })
        res.status_code = 200
        return res
    except Exception as e:
        print(e)


@app.route('/notes/<int:notesId>')
def notes_id(notesId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM notes WHERE notesId=%s", notesId)
        row = cursor.fetchone()
        res = jsonify(row)
        res.status_code = 20
        return res
    except Exception as e:
        print(e)

@app.route('/notes_user/<string:userId>')
def notes_user(userId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM notes WHERE userId=%s", userId)
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200
        return res
    except Exception as e:
        print(e)

@app.route('/delete/<int:notesId>', methods=['DELETE'])
def delete_notes(notesId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE notesId=%s", (notesId))
        conn.commit()
        res = jsonify('Notes deleted successfully.')
        res.status_code = 200
        return res
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run()