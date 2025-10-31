#!/bin/bash
# setup.sh — Installs Python + boto3

echo "Updating system..."
sudo apt update -y

echo "Installing Python3 + pip..."
sudo apt install python3 python3-pip -y

echo "Installing boto3 (AWS SDK)..."
pip3 install boto3

echo "Done! Run: python3 -c 'import boto3; print(boto3.__version__)'"
