from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = 'nyaya'

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
     print("Recieved Message: " + message)
     if message != "User connected!":
          send(message, broadcast = True)

@app.route('/')
def index():
     
     return render_template('chatbox.html')
     

if __name__ == '__main__':
     socketio.run(app, host="localhost", debug=True)
