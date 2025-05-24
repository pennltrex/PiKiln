from flask import Flask, render_template
from flask_socketio import SocketIO
import csv
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def emit_temperature():
    last_line = ""
    while True:
        with open('temperature_log.csv', 'r') as f:
            lines = f.readlines()
            if lines and lines[-1] != last_line:
                last_line = lines[-1]
                timestamp, temp = last_line.strip().split(',')
                socketio.emit('temperature_update', {'time': timestamp, 'temp': float(temp)})
        time.sleep(5)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    thread = threading.Thread(target=emit_temperature)
    thread.daemon = True
    thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)
