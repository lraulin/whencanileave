#!/bin/bash

# Correct pathname if necessary
# I could do it programmatically, but it's really ugly.
DIR=/Users/leeraulin/Projects/whencanileave
DATE=$(date +"%Y-%m-%d" )
echo -en '\001\033[01;31m\002' # light red
#pmset -g log|grep -E "$DATE 0.*Wake " > $DIR/today.txt
pmset -g log|grep -E "$DATE 0.*Wake " | python3 ${DIR}/whencanileave.py

#pmset -g log|grep -E "$DATE 08.*Wake from Normal Sleep.*EC.LidOpen" > $DIR/today.txt
#python3 ${DIR}/whencanileave.py