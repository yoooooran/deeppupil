from flask import Flask, send_file

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello from video!"


@app.route('/video', methods=['GET'])
def send_image():
    return send_file('static/video/test.mp4')


if __name__ == '__main__':
    app.run(port=4009)
