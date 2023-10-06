#!/usr/bin/python3
"""
a Fabric script  that creates and distributes an archive to your
web servers, using the function deploy:
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ["54.144.156.245", "54.210.109.65"]
env.user = "ubuntu"


def do_pack():
    """
    Prototype: def do_pack():
    * All files in the folder web_static must be added to the final archive
    * All archives must be stored in the folder versions (your function
    should create this folder if it doesnot exist)
    * The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    * The function do_pack must return the archive path if the archive has
    been correctly generated. Otherwise, it should return None
    """

    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{time}"
        local(f"tar -czvf versions/{archive_name}.tgz web_static")
        return (f"versions/web_static_{time}.tgz")
    except Exception:
        return None


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


def deploy():
    """
    a function that distributes an archive to your web servers,
    """
    local_path = do_pack()
    if local_path is None:
        return False
    return do_deploy(local_path)
