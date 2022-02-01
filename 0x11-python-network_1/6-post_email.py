#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""
import requests
import sys

def main():
    url = sys.argv[1]
    email - sys.argv[2]
    r = requests.post(url, data = {'email': email})
    print(r)


if __name__ == "__main__":
    main()

