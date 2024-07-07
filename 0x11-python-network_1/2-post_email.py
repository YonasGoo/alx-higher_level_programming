#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val).encode('ascii')
    handler = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(handler) as response:
        thisPage = response.read().decode('utf-8')
        print(thisPage)
