#!/usr/bin/python
#
# decolib [version 1.4]
#
# decolib.py is a Python module for Decollo that holds the functions to install the individual programs
#
# Copyright 2014 Dalton Duvio <dalt.duvi@gmail.com>
#
# Distributed under the terms of the GNU General Public License v3.
# See http://www.gnu.org/licenses/gpl.txt for the full text

# Import module
import subprocess

# Clears text from terminal.
def clear():
    subprocess.call("clear", shell = True)

# Gives intro to program
def intro():
    print """Welcome to DecolloX, a script written in Python. This was originally authored by @dlduvio. You can check out their repo at:

    github.com/dlduvio/decollo

    This fork is maintained by @SubSeven57.

    Please press enter to continue......."""

    raw_input()

    clear()

# Gives finish to program
def fini():
    print """
END
===



Thank you for using Decollo.




"""

    enter = raw_input('Press enter to return.....')
    clear()

# Checks the answer ("answer") and executes a shell command from a parameter named "command"
def promptInstall(answer, command):

    ans = answer.lower().strip()

    if ans in ['y', 'yes', '']:
        clear()
        subprocess.call(command, shell = True)
        return True
    elif ans in ['n', 'no']:
        return False
    else:
        promptInstall(raw_input("(Y)es or (N)o? "), command)

    clear()

# Performs a 'sudo apt-get update' in terminal
def aptUpdate(answer):
    x = promptInstall(answer, "sudo apt-get update")
    clear()
    return x

# Performs a 'sudo apt-get upgrade' in terminal
def aptUpgrade(answer):
    x = promptInstall(answer, "sudo apt-get -y upgrade")
    clear()

# Installs a program parameter via promptInstall
def simpleInstall(program, answer):
    x = promptInstall(answer, "sudo apt-get install -y {0}".format(program))
    clear()

# Installs a stated program from a ppa parameter via promptInstall
def ppaInstall(ppa, program, answer):
    x = promptInstall(answer, "sudo add-apt-repository {0} && sudo apt-get update && sudo apt-get install -y {1}".format(ppa, program))
    clear()

## Applications ###

# Installs Steam
def steam(answer):
    simpleInstall('steam', answer)

# Install Conky
def conky(answer):
    simpleInstall('conky', answer)

# Install Caffeine
def caffeine(answer):
    ppa = "ppa:caffeine-developers/ppa"
    program = "caffeine"
    ppaInstall(ppa, program, answer)

# Installs RAR and UnRAR
def  rar(answer):
    x= promptInstall(answer, 'sudo apt-get install -y rar unrar')
    clear()

# Installs Spotify from repository
def spotify(answer):
    x = promptInstall(answer, 'sudo add-apt-repository "deb http://repository.spotify.com stable non-free" && sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 94558F59 && sudo apt-get update && sudo apt-get install -y spotify-client')
    clear()

# Installs VLC media player
def vlc(answer):
    x = promptInstall(answer, 'sudo apt-get install -y vlc')
    clear()
    return x

# Installs Ubuntu Restricted Extras
def ubuntuRestricted(answer):
    simpleInstall('ubuntu-restricted-extras', answer)

# Installs OpenSSH
def openssh(answer):
    simpleInstall('openssh-server ssh-askpass', answer)


# Installs git
def git(answer):
    simpleInstall('git', answer)

# Installs Tilda
def guake(answer):
    simpleInstall('guake', answer)
