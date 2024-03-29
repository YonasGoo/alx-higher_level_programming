#!/usr/bin/python3
# takes and sends url
import urllib.request
import sys

def get_x_request_id(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.headers.get('X-Request-Id')
        return x_request_id

if __name__ == "__main__":
    url = sys.argv[1]
    print(get_x_request_id(url))
