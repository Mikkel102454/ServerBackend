import os
import pwd
import grp
import subprocess


def create_socket(serverID, serviceName, service, socketName, socket):
    print("creating socket...")
    hostPath = f"/home/servers/{serverID}"

    f = open(f"/etc/systemd/system/{serviceName}", "w")
    f.write(service)
    f.close()

    f = open(f"/etc/systemd/system/{socketName}", "w")
    f.write(socket)
    f.close()
    os.makedirs(hostPath, exist_ok=True)
def start_socket(socketName):
    subprocess.run(
        ["sudo", "systemctl", "start", socketName],
        text=True,
    )
    print(f"Service {socketName} started successfully!")
def stop_socket(socketName):
    subprocess.run(
        ["sudo", "systemctl", "stop", socketName],
        text=True,
    )
    print(f"Service {socketName} started successfully!")

def write_to_socket(socketName, msg):
        command = f"echo {msg} > /run/{socketName}"
        result = subprocess.run(
            ["sudo", "sh", "-c", command],
            text=True,
        )



def set_permissions(directory, user, group, mode):
    uid = pwd.getpwnam(user).pw_uid
    gid = grp.getgrnam(group).gr_gid

    items = os.listdir(directory)
    os.chown(directory, uid, gid)
    os.chmod(directory, mode)
    for item in items:
        item_path = os.path.join(directory, item)
        os.chown(item_path, uid, gid)
        os.chmod(item_path, mode)