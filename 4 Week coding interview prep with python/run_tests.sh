#!/bin/bash

cd /usercode/FILESYSTEM

result=$(python3 -m unittest discover -s /usercode/FILESYSTEM/tests  -p '*.py' 2>&1)

echo "${result}"
