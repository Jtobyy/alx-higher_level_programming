#!/bin/bash
#takes in a URL, sends a DELETE request to the URL, and displays the body of the response
curl -s -H "DELETE"  "$1" 
