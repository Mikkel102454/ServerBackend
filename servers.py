import os
import shutil

from container import create_container
from container import start_container

server_files = "/home/mikkel102454/hosting/src/ServerFiles/Minecraft/"
container_files = "/home/user/containers/ids/"

def create_new_server(id, version, ram):
    create_container(id)
    dir = os.path.join(server_files, version)
    destDir = os.path.join(container_files, id)
    for item in os.listdir(dir):
        source_item = os.path.join(dir, item)
        dest_item = os.path.join(destDir, item)

        if os.path.isfile(source_item):
            # Copy files
            shutil.copy2(source_item, dest_item)
            print(f"Copied file: {source_item} -> {dest_item}")
        elif os.path.isdir(source_item):
            # Copy directories
            shutil.copytree(source_item, dest_item, dirs_exist_ok=True)
            print(f"Copied directory: {source_item} -> {dest_item}")


def start_server(id, ram):
    start_container(id, ram, 21)
