#!/bin/bash
source ./venv/bin/activate
while true
do
	python3 Source/mailfilter.py --interactive
done
