import os
import shutil

from sockets import create_socket
from sockets import start_socket
from sockets import stop_socket
from sockets import write_to_socket

from std import generate_uuid
from database import insert_table
from database import read_value
from database import delete_from_table
server_files = "/home/mikkel/ServerBackend/ServerFiles/Minecraft/"
socket_files = "/home/servers/"

def create_new_server(name, version):
    id = name
    # id = generate_uuid()
    service = f'''
        [Unit]
        Description=Minecraft:{id}
        After=network.target
        [Service]
        User=servers
        Group=servers
        Type=simple
        ExecStart=/bin/sh -c "exec /home/servers/{id}/start.sh </run/mc.server.{id}.stdin"
        WorkingDirectory=/home/servers/{id}/
        MemoryMax=2G
        MemoryAccounting=true
        Sockets=mc.server.{id}.stdin
        [Install]
        WantedBy=multi-user.target
    '''
    socket = f'''
        [Unit]
        BindsTo=mc.server.{id}.service
        [Socket]
        ListenFIFO=%t/mc.server.{id}.stdin
        RemoveOnStop=true
        SocketMode=0660
        SocketUser=servers
        SocketGroup=servers
    '''
    create_socket(id, f"mc.server.{id}.service", service, f"mc.server.{id}.socket", socket)
    
    print("Generated with UUID: " + id)


    dir = os.path.join(server_files, version)
    destDir = os.path.join(socket_files, id)
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
    start_socket(f"mc.server.{id}.socket")

def stop_server(id):
    stop_socket(f"mc.server.{id}.socket")

## OTHER ##

#Get player list

#Get server.properties

#Set server.properties

def send_command(command, id):
    write_to_socket(f"mc.server.{id}.stdin", command)
    return