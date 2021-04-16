#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

# To update
sudo apt-get update -y

# To install nginx (-y flag to say yes to all)
sudo apt install nginx -y

# Create the folders if it doesnt already exist
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "Holberton School, Holberton is cool!" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Permissions
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static)
VAR="\\\tlocation /hbnb_static/ \{\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}"
sed -i "49i $VAR" /etc/nginx/sites-available/default

# Restart service
sudo service nginx restart
