#!/bin/bash
# This Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI 0.0.0.0:5000 | grep Content-Length | -d " " -f 2
