from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def main():
    return "OK"

def run():
  
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    server = Thread(target=run)
    server.start()
