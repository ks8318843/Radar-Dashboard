from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from firebase_utils import get_radar_data
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# Real-time data fetching
@socketio.on('get_data')
def handle_get_data():
    while True:
        radar_data = get_radar_data()
        emit('update_data', radar_data)
        time.sleep(2)  # Update every 2 seconds

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
