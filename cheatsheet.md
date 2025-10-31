# Linux Cheatsheet (Werkstudent Ready)

```bash
# Navigation
pwd; ls -la; cd /var/www; mkdir logs; touch app.py

# File Ops
cp app.py backup.py; mv app.py /var/www/; rm -rf old/

# Grep + Pipe
grep "ERROR" access.log > errors.txt
cat errors.txt | wc -l

# Package (Ubuntu)
sudo apt update && sudo apt install python3-pip -y
pip3 install boto3

# Permissions
sudo useradd devops
sudo chmod 755 /var/www
