#!/usr/bin/python
#
# decodescript [version 1.4]
#
# decodescript.py is a Python module for Decollo which holds the descriptions of each step
#
# Copyright 2014 Dalton Duvio <dalt.duvi@gmail.com>
#
# Distributed under the terms of the GNU General Public License v3
# See http://www.gnu.org/licenses/gpl.txt for the full text

# Import module as lib
import decolib as lib


# Desc. of media programs installation
def mediaPrograms():

    print '''




=====
MEDIA
=====




'''

    enter = raw_input('Press enter to continue.....')
    lib.clear()

#Desc. of theme programs
def themePrograms():

    print '''



=========================
THEMES AND CONFIGURATIONS
=========================




'''

    enter = raw_input('Press enter to continue.....')
    lib.clear()

# Desc. of extra programs
def extraPrograms():

    print '''




======
EXTRAS
======




'''

    enter = raw_input('Press enter to continue.....')
    lib.clear()

# Desc. of Developer programs
def developerPrograms():

    print '''



===========
DEVELOPMENT
===========




'''

    enter = raw_input('Press enter to continue.....')
    lib.clear()

# Desc. of Update process
aptUpdate = '''
REFRESH PACKAGES LIST
=====================

This step is necessary for continuing with the program, which is refreshing or updating the list of packages. This step will perform the following command:

    sudo apt-get update

Note: Without accepting this option, the Decollo will not continue.

Would you like to refresh? (Y/n)

'''

# Desc. of Upgrade process
aptUpgrade = '''
UPDATE SYSTEM
=============

This step updates your system with the following command:

    sudo apt-get upgrade

Would you like to update system? (Y/n)

'''

# Desc. of removal of Shopping suggestions
removeShopping = '''
DISABLE SHOPPING SUGGESTIONS
============================

This step disables shopping suggestions from the Dash with the following command:

    sudo gsettings set com.canonical.Unity.Lenses disabled-scopes "['more_suggestions-amazon.scope', 'more_suggestions-u1ms.scope', 'more_suggestions-populartracks.scope', 'music-musicstore.scope', 'more_suggestions-ebay.scope', 'more_suggestions-ubuntushop.scope', 'more_suggestions-skimlinks.scope']"

Would you like to disable shopping suggestions? (Y/n)

'''

# Desc. of Steam installation
steam = '''
STEAM
=====

Steam is used for buying and playing games. The following package will be installed:

    steam

Would you like to install Steam? (Y/n)

'''

# Desc. of Conky installation
conky = '''
CONKY
=====

Conky is a customizable overlay for your desktop that can display system information. The following package will be installed:

    conky

Would you like to install Conky? (Y/n)

'''

# Desc. of Caffeine installation
caffeine = '''
CAFFEINE
========

Caffeine prevents the monitor or screen from turning off while a full-screen program is active, such as while watching a movie. The following package will be installed:

    caffeine-plus

from the following PPA:

    ppa:caffeine-developers/ppa

Would you like to install Caffeine? (Y/n)

'''

# Desc. of Spotify installation
spotify = '''
SPOTIFY
=======

Spotify is a program that lets you listen to music from a large database. However, you need an account, which costs money to use the program. The following package will be installed:

    spotify-client

from the following repository:

    deb http://repository.spotify.com stable non-free

Would you like to install Spotify? (Y/n)

'''

# Desc. of Numix installation
numix = '''
NUMIX
=====

Numix is theme series the has GTK and icon themes with an orange and grey color scheme. To activate this theme, you will need to install the Unity Tweak Tool, which you are able to install in the next step. The following packages will be installed:

    numix-gtk-theme numix-icon-theme numix-icon-theme-circle numix-icon-theme-shine

from the following PPA:

    ppa:numix/ppa

Would you like to install the Numix theme? (Y/n)

'''

# Desc. of Unity Tweak Tool installation
unityTweak = '''
UNITY TWEAK TOOL
================

Unity Tweak Tool is a program that helps you install themes and perform other customizations to the Unity desktop environment, which is the default of Ubuntu. The following package will be installed:

    unity-tweak-tool

Would you like to install the Unity Tweak Tool? (Y/n)

'''

# Desc. of RAR and UnRar installation
rar = '''
RAR & UNRAR
===========

RAR and UnRAR are tools to help you compress and decompress files. The following packages will be installed:

    rar unrar

Would you like to install RAR and UnRAR? (Y/n)

'''

# Desc. of Ubuntu Restricted Extras installation
ubuntuRestricted = '''
UBUNTU RESTRICTED EXTRAS
========================

Ubuntu Restricted Extras are a series of packages that installs extra codecs and programs that do not come pre-installed with Ubuntu. The following package will be installed:

    ubuntu-restricted-extras

Would you like to install the Ubuntu Restricted Extras? (Y/n)

'''

# Desc. of VLC installation
vlc = '''
VLC
===

VLC is a media player capable of playing a wide range of video and audio formats. Ubuntu comes preinstalled with the Totem media player, but for many, VLC plays more formats. The following package will be installed:

    vlc

Would you like to install VLC player? (Y/n)

'''

#Desc. of OpenSSH installation
openssh = '''
OPENSSH
=======

OpenSSH is an ssh program, which allows you to remotely connect to your computer via a command line interface. The following packages will be installed:

    openssh-server ssh-askpass

Would you like to install OpenSSH? (Y/n)

'''

#Desc. of deconf editor installation
dconf = '''
DCONF EDITOR
============

Dconf editor is a GNOME configuration editor, similar to the Windows Registry. The following packages will be installed:

    dconf-editor dconf-tools

Would you like to install Dconf Editor? (Y/n)

'''

#Desc. of git installation
git = '''
GIT
===

Git is a source code management system and is integrated with GitHub. The following package will be installed:

    git

Would you like to install git? (Y/n)

'''

#Desc. of Clementine installation
clementine = '''
CLEMENTINE
==========

Clementine is an alternate music player to Rhythmbox. The following package will be installed:

    clementine

Would you like to install Clementine? (Y/n)

'''

# Desc. of Radiotray installation
radiotray = '''
RADIOTRAY
=========

Radiotray is an application that lets you listen to internet radio stations straight from the top panel of the desktop. The following package will be installed:

    radiotray

Would you like to install Radiotray? (Y/n)

'''

# Desc. of Tilda installation
guake = '''
GUAKE
=====

Guake is an alternative terminal emulator to the default. Instead of a window, Tild drops down from the top panel and is always on top. The following package will be installed:

    guake

Would you like to install Guake? (Y/n)

'''

# Desc of Diodon installation
diodon = '''
DIODON
======

Diodon is a clipboard manager for Ubuntu. The following package will be installed:

    diodon

Would you like to install Diodon? (Y/n)

'''

# Desc. of Moka theme
moka = '''
MOKA
====

Moka is a theme series featuring GTK themes and icons. For the most part, Moka uses a white, grey, and purple color scheme. The following packages will be installed:

    moka-gtk-theme
    orchis-gtk-theme
    stark-gtk-theme
    moka-icon-theme
    faba-icon-theme
    faba-mono-icons
    faba-colors

from the following PPA:

    ppa:moka/stable

Would you like to install the Moka theme series? (Y/n)

'''

# Desc. of Mixxx installation
mixxx = '''
MIXXX
=====

Mixxx is an open-source DJing program. It is a full featured DJ program with many features. The following package will be installed:

    mixxx

Would you like to install Mixxx? (Y/n)

'''

# Desc. of Oxygen cursor theme installation
oxygenCursorTheme = '''
OXYGEN CURSOR THEME
===================

The Oxygen cursor theme is simply a cursor theme that is default on KDE-based distros, such as Kubuntu. The following package will be installed:

    oxygen-cursor-theme

Would you like to install the Oxygen cursor theme? (Y/n)

'''

# Desc. of Vim installation

vim = '''
VIM
===

Vim is a terminal-based text editor that is lauded by programmers and power users for it's flexibility and power. The following package will be installed:

    vim

Would you like to install Vim? (Y/n)

'''

# Desc. of Fix Ubuntu
fixUbuntu = '''
FIX UBUNTU PRIVACY
==================

Fix Ubuntu is a script to secure the user's privacy, specifically for Unity. It disables Remote Search and remote shopping scopes from the Dash. The following command will be run:

    wget -q -O - https://fixubuntu.com/fixubuntu.sh | bash

Would you like to run the Fix Ubuntu script? (Y/n)

'''

# Desc. of Compiz Config Settings Manager
compizConfig = '''
Compiz Settings Manager
=======================

Compiz Config Settings Manager is an application that gives you access to the settings of Compiz, the compositing window manager for Unity. The following package will be installed:

    compizconfig-settings-manager

Would you like to install Compiz Config Settings Manager? (Y/n)

'''
