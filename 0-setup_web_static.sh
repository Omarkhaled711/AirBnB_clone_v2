#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt update
sudo apt install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
cat << EOT | sudo tee -a /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOT

if [ -L /data/web_static/current ]; then
    # Delete the existing symbolic link
    sudo rm /data/web_static/current
fi

# Create the new symbolic link
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
config_file="/etc/nginx/sites-available/default"
sudo sed -i '/^server {/a \    location /hbnb_static {\n        alias /data/web_static/current/;\n    }\n' "$config_file"
sudo service nginx restart
