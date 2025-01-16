import os
import shutil

from sockets import create_socket
from sockets import start_socket
from sockets import stop_socket
from sockets import write_to_socket
from sockets import set_permissions
from sockets import restart_socket
from sockets import delete_socket

from std import generate_uuid
from database import insert_table
from database import delete_from_table
server_files = "/home/mikkel/ServerBackend/ServerFiles/Minecraft/"
socket_files = "/home/servers/"

def create_new_server(name, version):
    id = name
    # id = generate_uuid()
    insert_table("mc-servers", "uuid, version, name, ram, port", (id, version, name, "2G", 0))
    service = f'''
        [Unit]
        Description=Minecraft:{id}
        After=network.target
        [Service]
        User=servers
        Group=servers
        Type=simple
        ExecStart=/bin/sh -c "exec /home/servers/{id}/start.sh </run/server.mc.{id}.stdin"
        ExecStop=/bin/sh -c "echo stop > /run/server.mc.{id}.stdin"
        WorkingDirectory=/home/servers/{id}/
        MemoryMax=2G
        MemoryAccounting=true
        Sockets=server.mc.{id}.stdin
        [Install]
        WantedBy=multi-user.target
    '''
    socket = f'''
        [Unit]
        BindsTo=server.mc.{id}.service
        [Socket]
        ListenFIFO=%t/server.mc.{id}.stdin
        RemoveOnStop=true
        SocketMode=0660
        SocketUser=servers
        SocketGroup=servers
    '''
    create_socket(id, f"server.mc.{id}.service", service, f"server.mc.{id}.socket", socket)
    
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

    set_permissions(f"/home/servers/{id}", "servers", "servers", 0o770)
def delete_server(id):
    delete_from_table("mc-servers", "uuid", id)
    delete_socket(id, f"server.mc.{id}.service", f"server.mc.{id}.socket")
def start_server(id):
    start_socket(f"server.mc.{id}.socket")
def stop_server(id):
    stop_socket(f"server.mc.{id}.service")
def restart_server(id):
    stop_socket(f"server.mc.{id}.service")
    start_socket(f"server.mc.{id}.socket")
## OTHER ##

#Get player list

#Get server.properties
def read_propertie(id, property):
    # read file
    with open(f"/home/server/{id}/server.properties", 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(property + "="):
                return line.split('=', 1)[1]

#Set server.properties
def change_propertie(id, property, value):
    # read file
    with open(f"/home/server/{id}/server.properties", 'r') as file:
        lines = file.readlines()

    # Modify the MemoryMax line
    with open(f"/home/server/{id}/server.properties", 'w') as file:
        for line in lines:
            if line.startswith(property):
                file.write(f"{property}={value}\n")
            else:
                file.write(line)

def send_command(command, id):
    write_to_socket(f"server.mc.{id}.stdin", command)
    return