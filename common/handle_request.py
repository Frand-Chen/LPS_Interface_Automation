# -*- coding=utf-8 -*-

"""
该模块用来处理 HTTP 请求
"""

import requests


class HandleRequest:
    """处理单个 HTTP 请求"""

    def send(self, url, method, data=None, json=None, params=None, headers=None):
        # 请求方法统一转换成大写进行判断
        method = method.upper()
        if method == "GET":
            return requests.get(url=url, params=params, headers=headers)
        elif method == "POST":
            return requests.post(url=url, data=data, json=json, headers=headers)
        elif method == "PATCH":
            return requests.patch(url=url, data=data, json=json, headers=headers)
        elif method == "DELETE":
            pass


class HandleSessionRequest:
    """处理使用 session 鉴权的接口"""

    def __init__(self):
        self.session = requests.session()

    def send(self):
        pass


handle_request = HandleRequest()
handle_session_request = HandleSessionRequest()

if __name__ == '__main__':
    url = "http://ec2-18-234-127-122.compute-1.amazonaws.com/vNext2/api/v2/session"
    params = {
        "propertyCode": "k00888"
    }
    headers = {
        "AKey": "8D1097CD-40DF-4BA2-8EFD-CCD896798B89",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        "Host": "ec2-18-234-127-122.compute-1.amazonaws.com",
        "Connection":"keep-alive"
    }

    res = handle_request.send(url=url, method="get", params=params, headers=headers)
    print(res.url)
    print(res.headers)
    print(res.content)
    print(res)

