from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # This is the magic line. It gets the "Hostname" of the machine.
    # In Docker, the Hostname is the Container ID.
    container_id = socket.gethostname()
    return f"🚦 Hello! Request served by Container ID: {container_id}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)