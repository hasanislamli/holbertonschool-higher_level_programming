#!/usr/bin/python3
"""Sends POST request with email and prints response body"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode("utf-8")
        print(body)
