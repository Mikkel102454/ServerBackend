import os
import shutil

from container import create_container
from container import start_container
from std import generate_uuid
#from database import insert_table
#from database import read_value
server_files = "/home/mikkel/hosting/src/ServerFiles/Minecraft/"
container_files = "/home/user/containers/ids/"

def create_new_server(name, version):
    ram = "2G"
    # Uplaod To database
    id = name
    #id = generate_uuid()
    print("Generated with UUID: " + id)
    #insert_table("MinecraftServers", "uuid, version, name, ram", f"{id}, {version}, {name}, {ram}")
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


def start_server(id, port):
    #ram = read_value("mc_servers", "ram", "UUID", id)
    start_container(id, ram, int(port))

def delete_server():
    return

## OTHER ##