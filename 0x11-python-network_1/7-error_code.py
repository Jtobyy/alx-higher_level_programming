#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the
URL and displays the body of the response.
"""
import requests
import sys


def main():
    url = sys.argv[1]
