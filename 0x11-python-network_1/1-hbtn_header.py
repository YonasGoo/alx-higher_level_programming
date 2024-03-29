#!/usr/bin/python3
# takes and sends url
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)

