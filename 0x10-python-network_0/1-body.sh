#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -fL -H "GET"  "$1" 
