#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests


def main():
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(r.text)}')
    print(f'\t- content: {r.text}')


if __name__ == "__main__":
    main()
