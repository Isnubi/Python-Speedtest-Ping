# Author: isnubi

# Update and install curl
sudo apt update
sudo apt install curl

# Install speedtest package by Ookla and python3
curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash
sudo apt-get install speedtest python3 python3-pip python3-tk -y

# Install python3 requirements
sudo python3 -m pip install -r requirements.txt

# Launch a first speedtest to accept the license and the EULA
sudo speedtest