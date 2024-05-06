from flask import Flask, make_response
import cv2

app = Flask(__name__)


@app.route('/image')
def get_image():
    # 使用OpenCV处理图像
    image = cv2.imread('static/images/pic1.jpg')  # 读取图像
    # ... 进行一些处理 ...

    # 将图像转换为JPEG格式的字节流
    _, buffer = cv2.imencode('.jpg', image)
    jpeg_image = buffer.tobytes()

    # 设置响应头，并返回图像数据
    response = make_response(jpeg_image)
    response.headers['Content-Type'] = 'image/jpeg'
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4051)
