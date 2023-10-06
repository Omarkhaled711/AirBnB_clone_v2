#!/usr/bin/python3
"""
A module that contains a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os


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
