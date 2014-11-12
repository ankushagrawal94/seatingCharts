#!/bin/bash
echo Creating txt files based on sections.txt
echo Create txt files
python generateSeats.py
echo Generating pdfs
./allVisuals.sh
echo Creating alphabetized files
python alpha.py
echo completed
echo upload this to server for email
echo upload pdf and alphabetized lists to piazza
