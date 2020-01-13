#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays:
- The body of the response if there are no errors
- The error code when there is an HTTP error.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.status_code) if r.status_code >= 400 else print(r.text)
