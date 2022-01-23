#!/bin/bash
#takes in a URL, sends a DELETE request to the URL, and displays the body of the response
curl -s -X "POST" --data-binary "email=test@gmail.com" --data-binary "subject=I will always be here for PLD" "$1"
