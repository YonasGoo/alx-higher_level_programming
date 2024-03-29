#!/bin/bash
# sends a req
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

RESPONSE_SIZE=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

echo "Size of the response body: $RESPONSE_SIZE bytes"

