import etcd3


class ServiceRegistry:
    def __init__(self, host, port):
        self.client = etcd3.client(host=host, port=port)

    def register_service(self, name, host, port):
        key = f"/services/{name}"
        value = f"{host}:{port}"
        self.client.put(key, value)

    def discover_service(self, name):
        key = f"/services/{name}"
        response = self.client.get(key)
        strHaiCoder = str(response[0], 'utf-8')
        return strHaiCoder
        # if response.count > 0:
        #     return response.kvs[0].value
        # else:
        #     return None
