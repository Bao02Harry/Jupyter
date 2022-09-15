#!/bin/bash
for i in $(cat List_Users.txt)
do
    sudo deluser $i 
    sudo rm -rf /home/$i
done

sudo systemctl restart jupyterhub.service