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
    Fabric script that distributes an archive to your web servers.
    """

    if not os.path.isfile(archive_path):
        return(False)
    try:
        versions/web_static_20170314233357.tgz
        file_path = archive_path
        put(file_path, "/tmp/")

        # Uncompress the archive to the folder
        folder = file_path.split("/")

        # Path to releases dir
        releases_path = "/data/web_static/releases/"

        # folder_name <archive filename without extension> to uncompress
        unzip_path = "{}{}".format(releases_path, folder[1][0:-4])

        # filename.tgz
        file_name = folder[1]

        # folder_name <archive filename without extension>
        folder_name = folder[1][0:-4]
        date = folder[1][11:-4]

        # Folder to /data/web_static/releases/<archive filename without .tgz>
        run("mkdir -p {}".format(unzip_path))
        run("tar -xzf /tmp/{} -C {}"
            .format(file_name, unzip_path))
        run("rm /tmp/{}".format(file_name))
        run("mv {}{}/web_static/* {}{}/"
            .format(releases_path, folder_name, releases_path, folder_name))
        run("rm -rf {}{}/web_static"
            .format(releases_path, folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current"
            .format(unzip_path))

        print("New version deployed!")
        return True

    except BaseException:
        return False
