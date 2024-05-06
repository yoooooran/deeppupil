from flask import Flask, request
from flask_cors import CORS
from functools import wraps

import requests

from service_registry import ServiceRegistry

app = Flask(__name__)


@app.route('/<service_name>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_request(service_name, path):
    # get all
    # get_data = request.args.to_dict()

    # post all
    # post_data = request.form

    headers = request.headers
    print(headers)

    # token = request.args.get('token')
    # print(token)
    # headers = {"Content-Type":"application/json"}
    # if token is None:
    #     print("No token")
    # else:
    #     print("Token found:" + str(token))
    #     headers["Authorization"] = token
    # print(headers)
    service_url = registry.discover_service(service_name)
    if service_url:
        url = f"http://{service_url}/{path}"
        response = requests.request(request.method, url, data=request.data, headers=headers)
        return response.text, response.status_code
    else:
        return "Service not found", 404


@app.route('/<service_name>', methods=['GET', 'POST'])
def proxy_request_main(service_name):
    print(service_name)
    service_url = registry.discover_service(service_name)
    if service_url:
        url = f"http://{service_url}"
        response = requests.request(request.method, url, data=request.data)

        return response.text, response.status_code
    else:
        return "Service not found", 404


CORS(app, resources=r'/*')
if __name__ == '__main__':
    registry = ServiceRegistry(host='localhost', port=2379)
    registry.register_service('service1', '127.0.0.1', 5000)
    registry.register_service('service2', '127.0.0.1', 5001)
    registry.register_service('backend', '127.0.0.1', 8000)

    app.run(port=8050)
