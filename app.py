from flask import Flask, render_template
from flask_socketio import SocketIO
from temperature_emitter import start_emitter

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# Start the background temperature emitter
start_emitter(socketio)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
