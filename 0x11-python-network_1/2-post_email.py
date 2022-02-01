#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


def main():
    """
    Takes in a URL and an email, sends a POST
    request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    url = sys.argv[1]
    email = sys.argv[2]
    req = urllib.request.Request(url)
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print(f'{html.decode("utf-8")}')


if __name__ == "__main__":
    """
    prevents code execution on importation
    """
    main()
