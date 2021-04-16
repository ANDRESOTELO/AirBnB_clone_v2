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
from fabric.api import local, hide
from datetime import datetime


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
