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
        # Get the UID and GID of the user and group
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(group).gr_gid

        # Recursively change ownership and permissions
        for root, dirs, files in os.walk(directory):
            # Change ownership and permissions of the current directory
            os.chown(root, uid, gid)
            os.chmod(root, mode)

            # Change ownership and permissions of all files
            for file in files:
                file_path = os.path.join(root, file)
                os.chown(file_path, uid, gid)
                os.chmod(file_path, mode)

            # Change ownership and permissions of all subdirectories
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.chown(dir_path, uid, gid)
                os.chmod(dir_path, mode)