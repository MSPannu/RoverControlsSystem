from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)  # Flask app name should be __name__
socketio = SocketIO(app)

# Store the latest command
latest_command = None

@app.route('/')
def index():
    return render_template('index.html')

# WebSocket route to receive commands
@socketio.on('command')
def handle_command(data):
    global latest_command
    latest_command = data
    print(f"Received command: {data}")
    
    # Broadcast the command to all connected clients
    emit('update', data, broadcast=True)

# Use __name__ == '__main__' to start the server
if __name__ == '__main__':
    socketio.run(app)
