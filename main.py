'''
项目运行入口
'''

import time
import requests
import ssl
from config import *


def get_index_html():
    url = "https://www.icourse163.org/"
    # ssl._create_default_https_context = ssl._create_unverified_context
    r = requests.get(url)
    print(r.status_code)
    print(r.apparent_encoding)
    print(r.text)


def main():
    get_index_html()


if __name__ == '__main__':
    main()