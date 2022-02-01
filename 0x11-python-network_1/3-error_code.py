#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
