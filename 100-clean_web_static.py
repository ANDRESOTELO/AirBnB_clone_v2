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
from fabric.context_managers import cd, lcd

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

    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            folder_path = "/data/web_static/releases/" + archive_path[9:-4]
            name_file = archive_path[9:]
            name_folder = archive_path[9:-4]
            date = archive_path[21:-4]
            releases = "/data/web_static/releases/"

            run("mkdir -p {}".format(folder_path))
            run("tar -xzf /tmp/{} -C {}".format(name_file, folder_path))
            run("rm /tmp/{}".format(name_file))
            run("mv {}{}/web_static/* {}{}/"
                .format(releases, name_folder, releases, name_folder))
            run("rm -rf {}{}/web_static".format(releases, name_folder))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(folder_path))
            print("New version deployed!")

            return (True)
        except BaseException:
            return (False)
    else:
        return (False)


def deploy():
    """
    Fabric script that creates and distributes an archive to your web servers
    """

    path_file = do_pack()

    if path_file is None:
        return(False)

    path_created = do_deploy(path_file)

    return(path_created)


def do_clean(number=0):
    """
    Fabric script that deletes out-of-date archives
    """

    try:
        number = int(number)
    except:
        return None

    if number < 0:
        return None

    if (number == 0 or number == 1):
        number = 2
    else:
        number += 1

    with lcd("./versions"):
        local('ls -t | tail -n +{} | xargs rm -rf --'.format(number))

    with cd("/data/web_static/releases"):
        run('ls -t | tail -n +{} | xargs rm -rf --'.format(number))
