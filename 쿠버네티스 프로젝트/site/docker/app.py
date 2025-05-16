from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, 3rd web site!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
