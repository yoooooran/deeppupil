import socket
import numpy as np

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
s.connect(('localhost', 4005))

# 接收数据并转换为NumPy数组
data = s.recv(1024)
mat = np.frombuffer(data, dtype=np.int32).reshape((2, 3))

# 打印接收到的数组
print(mat)

# 关闭连接
s.close()
