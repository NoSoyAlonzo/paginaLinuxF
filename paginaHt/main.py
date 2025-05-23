from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # IP del cliente, considerando si viene desde un proxy inverso
    client_ip = request.headers.get('X-Real-IP', request.remote_addr)
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", client_ip=client_ip, server_time=server_time)
