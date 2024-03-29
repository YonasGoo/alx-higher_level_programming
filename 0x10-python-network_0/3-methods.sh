#!/bin/bash
# curl only method
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
