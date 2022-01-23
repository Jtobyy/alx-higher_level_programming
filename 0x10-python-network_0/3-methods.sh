#!/bin/bash
#takes in a URL, sends a DELETE request to the URL, and displays the body of the response
curl -s -I  "$1" | grep "Allow" | cut -f 1 -d " " -d ":" --complement
