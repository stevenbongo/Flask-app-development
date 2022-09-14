

from flask import Flask
app = Flask(__name__)

app.run(host='0.0.0.0', port=8005)

@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'
