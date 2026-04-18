#!/bin/bash
# displays allowed HTTP methods for a URL
curl -sI "$1" | grep Allow | cut -d " " -f2-
