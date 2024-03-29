#!/usr/bin/python3
# sends request
import urllib.request
import urlib.parse
import urllib.error
import sys


import urlib.parseif __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            thisPage = response.read().decode('utf-8')
            print(thisPage)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
