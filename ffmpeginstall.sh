#############################################################################################
#                               Author:     Nate Nesler                                     #
#                               Date:       June 1st 2013                                   #
#                               License:    LGPL                                            #
#############################################################################################

# ffmpeg installs

#!/bin/bash

# ubuntu 14.04 only
# edit /etc/apt/sources.list and insert the following two lines in the file and save it
# remember to remove the # sign when you insert these lines as it will comment out the line.
# deb http://ppa.launchpad.net/jon-severinsson/ffmpeg/ubuntu trusty main 
# deb-src http://ppa.launchpad.net/jon-severinsson/ffmpeg/ubuntu trusty main 

# below ubuntu 14.04 you can use the standard ffmpeg install
# sudo apt-get install -y ffmpeg

sudo apt-get install libavcodec-devc
# you must force it for ubuntu 14.04 
sudo apt-get --force-yes install ffmpeg

# Handbrake for ubuntu 12.04 and up
sudo add-apt-repository ppa:noobslab/apps
# Handbrake for below ubuntu 12.04
# sudo add-apt-repository ppa:stebbins/handbrake-releases

sudo apt-get update -y
sudo apt-get install -y handbrake-cli

sudo apt-get install -y ffmpeg2theora
sudo apt-get install -y gifsicle

exit 0

