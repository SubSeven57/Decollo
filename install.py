#!/usr/bin/python
#
# install script of Decollo [version 1.1.3]
# 
# install.py is a Python module for Decollo that installs the program
# 
# Splynt <splyntm@gmail.com>
#
# Do whatever the fuck you want with this script. It's too simple to give a shit about anyways.

# Import module subprocess
import subprocess

# Creates a command function for bash commands
def command(command):
    subprocess.call(command, shell=True)

# Puts files in necessary places for Ubuntu
def run():
    
    command('sudo cp decollo /usr/bin')
    command('sudo cp decodescript.py /usr/lib/python2.7')
    command('sudo cp decolib.py /usr/lib/python2.7')
    command('sudo chmod +x /usr/bin/decollo')

run()
