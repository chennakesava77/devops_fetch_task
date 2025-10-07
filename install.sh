#!/bin/bash
echo "Installing dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip nginx docker.io lsof ss
pip3 install tabulate

echo "Setting up devopsfetch..."
sudo mkdir -p /opt/devopsfetch
sudo cp -r * /opt/devopsfetch
sudo cp devopsfetch.service /etc/systemd/system/

echo "Enabling service..."
sudo systemctl daemon-reexec
sudo systemctl enable devopsfetch
sudo systemctl start devopsfetch
