#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ["54.144.156.245", "54.210.109.65"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False
    put(archive_path, '/tmp/')
    file_name = archive_path[archive_path.find('w'):]
    remote_path = f"/data/web_static/releases/{file_name[:-4]}"
    run(f"sudo mkdir -p {remote_path}")
    archive_path = '/tmp/'+file_name
    run(f"sudo tar -xzf {archive_path} -C {remote_path}/")
    run("sudo rm {}".format(archive_path))
    run(f"sudo mv {remote_path}/web_static/* {remote_path}")
    run(f"sudo rm -rf {remote_path}/web_static")
    run("sudo rm -rf /data/web_static/current")
    run(f"sudo ln -s {remote_path} /data/web_static/current")
    print("New version deployed!")
    return True
