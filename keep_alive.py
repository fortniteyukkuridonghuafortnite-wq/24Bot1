from flask import Flask from threading import Thread
app = Flask(__name__)
@app.route ('/')
def home ():
return
"Bot is running!"
def run ():
port=8080)
app.run(host="O.0.0.0",
def keep_alive ():
t = Thread(target=run)
t.start ()
