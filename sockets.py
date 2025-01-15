import os
import pwd
import grp
import subprocess
import shutil

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
def delete_socket(serverID, serviceName, socketName):
    stop_socket(socketName)
    hostPath = f"/home/servers/{serverID}"
    shutil.rmtree(hostPath)
    if os.path.exists(f"/etc/systemd/system/{serviceName}"):
        os.remove(f"/etc/systemd/system/{serviceName}")
    if os.path.exists(f"/etc/systemd/system/{socketName}"):
        os.remove(f"/etc/systemd/system/{socketName}")
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
    print(f"Service {socketName} stopped successfully!")
def restart_socket(socketName):
    subprocess.run(
        ["sudo", "systemctl", "restart", socketName],
        text=True,
    )
    print(f"Service {socketName} started successfully!")
def write_to_socket(socketName, msg):
        command = f"echo {msg} > /run/{socketName}"
        result = subprocess.run(
            ["sudo", "sh", "-c", command],
            text=True,
        )

def change_max_ram(socketName, maxRam):
    # read file
    with open(f"etc/systemd/system/{socketName}", 'r') as file:
        lines = file.readlines()

    # Modify the MemoryMax line
    with open(f"etc/systemd/system/{socketName}", 'w') as file:
        for line in lines:
            if line.startswith("MemoryMax="):
                file.write(f"MemoryMax={maxRam}\n")
            else:
                file.write(line)

def set_permissions(directory, user, group, mode):
    uid = pwd.getpwnam(user).pw_uid
    gid = grp.getgrnam(group).gr_gid

    # Change ownership and permissions for the root directory
    try:
        os.chown(directory, uid, gid)
        os.chmod(directory, mode)
    except PermissionError as e:
        print(f"Permission denied: {directory} ({e})")
        return

    # Iterate through the contents of the directory
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.islink(item_path):
                # Skip symbolic links
                continue
            elif os.path.isdir(item_path):
                # Recursively process subdirectories
                set_permissions(item_path, user, group, mode)
            else:
                # Change ownership and permissions for files
                os.chown(item_path, uid, gid)
                os.chmod(item_path, mode)
    except PermissionError as e:
        print(f"Permission denied: {directory} ({e})")