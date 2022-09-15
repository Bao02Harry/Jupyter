#!/bin/bash

# Get data from excel file
python3 source.py

# Create users in system from DefaultPassword.txt 
# Default password is "1234"
for i in $(cat List_Users.txt)
do
    cat "DefaultPassword.txt" | sudo adduser --force-badname $i
done

# Add below script to header of jupyterhub_config.py in /opt/jupyterhub/etc/jupyterhub/

# import sys 
# import os
# sys.path.append(os.path.abspath("/home/Your_UserName/Add_User_JupyterHub"))
# from source import users
# 

# Restart jupyterhub.service to reload users in database
sudo systemctl restart jupyterhub.service


