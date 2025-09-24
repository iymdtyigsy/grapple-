from flask import Flask, render_template
from flask_socketio import SocketIO
import serial, time, threading

# Adjust COM port for your Nano (Windows: COM3, Linux: /dev/ttyUSB0)
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # wait for Arduino reset

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('command')
def handle_command(cmd):
    print(f"Sending to Arduino: {cmd}")
    arduino.write((cmd + '\n').encode('utf-8'))

    # Read Arduino reply
    response = arduino.readline().decode('utf-8').strip()
    if response:
        socketio.emit('status', response)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
