# deeppupil

#### 介绍
超级简陋的Python微服务解决方案

#### 项目结构   

- api_gateway.py  # API网关
- service_registry.py  # 服务注册与发现
- service_1.py  # 测试服务1
- service_2.py  # 测试服务2
- pic.py  # 本地图片读取/修改
- pic_mat.py  # socket服务
- pic_mat_receive.py  # socket接收
- video.py  #本地视频读取


#### 准备工作

Python >= 3.11.0 (最低3.9+版本)

#### 安装教程

安装依赖环境

    pip install -r requirements.txt

安装etcd(附docker安装方式)
    
    docker pull bitnami/etcd
    
    docker run -it --name etcd-server \
    -p 2379:2379 -p 2380:2380 \
    --env ALLOW_NONE_AUTHENTICATION=yes \
    -d bitnami/etcd

#### 使用说明

1.  启动etcd
2.  python service_1.py
3.  python service_2.py
4.  python api_gateway.py

