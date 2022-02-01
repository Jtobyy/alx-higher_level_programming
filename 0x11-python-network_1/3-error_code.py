#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

from urllib.error import HTTPError
import urllib.request
import sys


def main():
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
    except HTTPError as e:
        print(f'Error code: {e.code}')


if __name__ == "__main__":
    main()
