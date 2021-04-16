#!/usr/bin/python3
"""
Fabric is a Python library and command-line tool for streamlining the use
of SSH for application deployment or systems administration tasks. It
provides a basic suite of operations for executing local or remote shell
commands (normally or via sudo) and uploading/downloading files, as well
as auxiliary functionality such as prompting the running user for input,
or aborting execution.
"""
import os
from fabric.api import local, hide, env, run, put
from datetime import datetime

env.hosts = ["35.196.21.242", "35.231.11.206"]


def do_pack():
    """
    Fabric script that generates a .tgz archive from the contents of the
    web_static folder
    """

    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")

        with hide('running', 'stdout'):
            local("mkdir -p versions")

        file_path = "versions/web_static_{}.tgz".format(date)

        local("tar -cvzf {} web_static".format(file_path))

        return file_path

    except BaseException:
        return None


def do_deploy(archive_path):
    """
    Fabric script that distributes an archive to your web servers
    """

    if not os.path.exists(archive_path):
        return(False)
    try:
        put(file_path, "/tmp/")
        folder = "/data/web_static/releases/" + archive_path[9:-4]
        file_name = archive_path[9:]
        folder_name = archive_path[9:-4]
        date = archive_path[21:-4]
        releases_path = "/data/web_static/releases/"

        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder))
        run("rm /tmp/{}".format(file_name))
        run("mv {}{}/web_static/* {}{}/"
            .format(releases_path, folder_name, releases_path, folder_name)\
)
        run("rm -rf {}{}/web_static".format(releases_path, folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        print("New version deployed!")

        return (True)

    except BaseException:
        return (False)
