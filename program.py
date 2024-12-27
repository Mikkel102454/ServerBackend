import docker
import time
# Initialize Docker client
client = docker.from_env()

activeContainers = []
def create_container(serverID, ram):
    try:
        # Create a container with memory limits
        container = client.containers.run(
            "alpine",  # Base image
            name=serverID,
            command="sh -c 'while true; do echo hello; sleep 1; done'",
            detach=True,
            volumes=[
                f"/home/user/containers/ids/{serverID}:/containers/data/ids/{serverID}:rw"
            ],
            mem_limit=ram
        )
        activeContainers.append(container)
        print(serverID)
    except Exception as e:
        print(f"There has been an error while creating a docker: {e}")
def stop_container(serverID):
    try:
        container = get_container(serverID)
        if container is not None:
            container.stop()
            activeContainers.remove(container)
        else:
            print(f"No docker with id: {serverID}")
    except Exception as e:
        print(f"There has been an error while stopping a docker: {e}")

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
        _ram = input("ram:")
        create_container(_id, _ram)
    if(_cmd == "remove"):
        _id = input("id:")
        stop_container(_id)
    if(_cmd == "help"):
        print("list | create | remove")
    time.sleep(10)