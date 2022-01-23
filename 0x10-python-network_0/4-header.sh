#!/bin/bash
#takes in a URL, sends a DELETE request to the URL, and displays the body of the response
curl -s -G -H "X-School-User-Id: 98" "$1"
