#!/bin/bash
#takes in a URL, sends a DELETE request to the URL, and displays the body of the response
curl -s -X "POST" --data-raw "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
