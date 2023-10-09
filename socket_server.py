from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from uagents import Agent

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
alice = Agent(name='alice', seed='42')

# Define a function to send messages to the client
# @alice.on_interval(period=5.0)
def send_message_to_client(message):
    print("we at send_message_to_client")
    socketio.emit('message', message)

# executor.submit(send_message_to_client(message="hiii"))

# Define a route for the client to connect to
@app.route('/')
def index():
    return render_template('index.html')

# Start the SocketIO server
if __name__ == '__main__':
    # Start a background task to send messages to the client every 10 seconds
    # socketio.start_background_task(send_message_to_client, 'Agent is working!')
    socketio.run(app, port=8080)
    send_message_to_client("please work")
