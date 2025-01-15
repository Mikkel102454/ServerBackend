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
    try:
        # Get the UID and GID of the user and group
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(group).gr_gid

        # Recursively change ownership and permissions
        for root, dirs, files in os.walk(directory):
            # Change ownership and permissions for the current directory
            os.chmod(root, mode)

            # Change ownership and permissions for all files in the current directory
            for file in files:
                file_path = os.path.join(root, file)
                os.chmod(file_path, mode)  # Remove execute bit for files

            # Change ownership and permissions for all subdirectories in the current directory
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.chmod(dir_path, mode)  # Directories keep execute permissions

        print(f"Permissions successfully updated for '{directory}'")
    except KeyError as e:
        print(f"Error: {e}")
        print("Ensure the user and group exist.")
    except PermissionError as e:
        print(f"Permission denied: {e}")
        print("Run the script with elevated permissions (e.g., sudo).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")