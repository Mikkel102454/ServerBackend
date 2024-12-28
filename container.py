import docker
import os
import shutil

# Initialize Docker client
client = docker.from_env()

activeContainers = []
def start_container(serverID, ram):
    try:
        print("starting container...")
        hostPath = f"/home/user/containers/ids/{serverID}"
        # Create a container with memory limits
        container = client.containers.run(
            "alpine",  # Base image
            name=serverID,
            command="sh -c 'cd /host_path && sh container.sh'",
            volumes={
                hostPath: {'bind': '/host_path', 'mode': 'rw'}  # Host path mounted to /host_path in container
            },
            detach=True,
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


