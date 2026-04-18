#!/bin/bash
# sends a GET request with custom header and displays body
curl -s -H "X-School-User-Id: 98" "$1"
