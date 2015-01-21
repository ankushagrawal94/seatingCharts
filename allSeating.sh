#!/bin/bash
echo Creating txt files based on sections.xls
python xlsToRosters.py
echo Generating pdfs
./allVisuals.sh
echo Creating alphabetized files
python alphabetize.py
echo modifying config files
python modifyConfig.py
echo upload pdf and alphabetized lists to piazza
./copyToDrive.sh
echo uploading to cs12x account and executing commands
./connectToRemoteServer.sh

