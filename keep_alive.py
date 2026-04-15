from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    # Теперь веб-сервер возвращает очень короткое сообщение - ТОЛЬКО "OK"
    # Никакого HTML, никаких лишних данных.
    return "OK"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
