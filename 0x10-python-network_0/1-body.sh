#!/bin/bash
# Script that shows the body if Status Code is 200
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -s "$1"
