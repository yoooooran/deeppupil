import socket
import cv2

# 创建一个NumPy数组
mat = cv2.imread('static/images/pic1.jpg')  # 读取图像

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 4005))
s.listen(5)

# 建立连接
conn, addr = s.accept()

# 将NumPy数组转换为字节串并发送
conn.send(mat.tobytes())

# 关闭连接
conn.close()
s.close()
