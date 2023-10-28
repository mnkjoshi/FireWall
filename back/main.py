import firebase_admin
from flask import Flask, request, jsonify
from firebase_admin import auth, credentials, db
from firebase_connection import firebase_connection

# Initialize the Flask app
app = Flask(__name__)

fc = firebase_connection()
@app.route('/')
def base():
    return ''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

@app.route('/getdata', methods=['GET'])
def getdata():
    dataToDo = fc.get_data()
    if dataToDo:
        return dataToDo
    else:
        return ''

@app.route('/newData', methods=['GET'])
def newData():
    dataToDo = fc.get_new_data()
    return dataToDo

if __name__ == '__main__':
    app.run(debug=True)
