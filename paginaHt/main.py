from flask import Flask, render_template
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    server_ip = socket.gethostbyname(socket.gethostname())
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", server_ip=server_ip, server_time=server_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)