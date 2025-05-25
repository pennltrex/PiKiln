
import time
from threading import Thread
from flask_socketio import SocketIO

socketio = None  # Will be initialized in app.py

def emit_temperature():
    file_position = 0

    while True:
        try:
            with open('temperature_log.csv', 'r') as f:
                f.seek(file_position)
                new_lines = f.readlines()
                file_position = f.tell()

                for line in new_lines:
                    try:
                        timestamp, temp = line.strip().split(',')
                        socketio.emit('temperature_update', {
                            'time': timestamp,
                            'temp': float(temp)
                        })
                        print(f"Emitting: {timestamp}, {temp}")
                    except ValueError:
                        continue
        except FileNotFoundError:
            pass  # Wait until the file is created

        time.sleep(5)

def start_emitter(sio):
    global socketio
    socketio = sio
    thread = Thread(target=emit_temperature)
    thread.daemon = True
    thread.start()
