import docker
import os
import shutil

from servers import create_new_server
from servers import start_server
# Initialize Docker client
client = docker.from_env()

activeContainers = []
def start_container(serverID, ram):
    try:
        print("starting container...")
        hostPath = f"/home/user/containers/ids/{serverID}"
        containerPath = f"/containers/data/ids/{serverID}"
        # Create a container with memory limits
        container = client.containers.run(
            "alpine",  # Base image
            name=serverID,
            command=f"sh -c 'cd {containerPath} && sh container.sh'",
            detach=True,
            volumes=[
                f"{hostPath}:{containerPath}:rw"
            ],
            mem_limit=ram
        )
        activeContainers.append(container)
        print(serverID)
    except Exception as e:
        print(f"There has been an error while creating a docker: {e}")
def stop_container(serverID):
    try:
        print("stopping container...")
        container = get_container(serverID)
        if container is not None:
            container.stop()
            activeContainers.remove(container)
        else:
            print(f"No docker with id: {serverID}")
    except Exception as e:
        print(f"There has been an error while stopping a docker: {e}")
def delete_container(serverID):
    print("creating container...")
    hostPath = f"/home/user/containers/ids/{serverID}"
    containerPath = f"/containers/data/ids/{serverID}"
    shutil.rmtree(hostPath)
    shutil.rmtree(containerPath)
    
def create_container(serverID):
    print("creating container...")
    hostPath = f"/home/user/containers/ids/{serverID}"
    containerPath = f"/containers/data/ids/{serverID}"
    os.makedirs(hostPath, exist_ok=True)
    os.makedirs(containerPath, exist_ok=True)

def get_container(serverID):
    for container in activeContainers:
        if container.name == serverID:
            return container
    return None

def get_all_containers():
    for container in activeContainers:
        print (container.name)


while True:
    _cmd = input("Command:")

    if(_cmd == "list"):
        get_all_containers()
    if(_cmd == "create"):
        _id = input("id:")
        _v = input("version:")
        create_new_server(_id, _v, "2G")
    if(_cmd == "start"):
        _id = input("id:")
        _ram = input("ram:")
        start_server(_id, _ram)
    if(_cmd == "remove"):
        _id = input("id:")
        stop_container(_id)
    if(_cmd == "help"):
        print("list | create | remove")