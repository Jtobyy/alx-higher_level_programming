#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""
import urllib.request


req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    html = response.read()

print('Body response:')
print(f'\t- type: {type(html)}')
print(f'\t- content: {html}')
print(f'\t- utf8 content: {html.decode("utf-8")}')

if "__name__" == "__main__":
    pass
