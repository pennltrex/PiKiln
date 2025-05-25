from flask import Flask, render_template
from flask_socketio import SocketIO
from temperature_emitter import start_emitter
import csv
import settings

app = Flask(__name__)
socketio = SocketIO(app)

def read_csv_data():
    data = []
    try:
        with open(settings.CSV_FILE_NAME, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append({
                    "x": row["Timestamp"],  # x for Chart.js time axis
                    "y": float(row["Temperature (°C)"])
                })
    except FileNotFoundError:
        pass
    return data

@app.route('/')
def index():
    initial_data = read_csv_data()
    return render_template('index.html', initial_data=initial_data)

# Start the background temperature emitter
start_emitter(socketio)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
