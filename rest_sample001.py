#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json


def execute(args):

    headers = {
        "Accept": "application/json",
        "Content-type": "application/json"
    }

    payload_obj = {
        'per_page': '1',
        'page': '4'
    }

    proxies = get_proxy()

    r = requests.get(
        'https://qiita.com/api/v2/users/qiita/items',
        headers=headers,
        params=payload_obj,
        proxies=proxies,
        verify=False
    )
    print(r.url)
    print(r.json())


def get_proxy():
    proxy = 'http://127.0.0.1:8888'
    return {
        "http": proxy, "https": proxy
    }


if __name__ == "__main__":
    execute(sys.argv)
