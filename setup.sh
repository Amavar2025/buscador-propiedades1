#!/bin/bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb || sudo apt-get -f install -y
CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
wget -N https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv -f chromedriver /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver