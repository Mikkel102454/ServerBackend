import os
import shutil
import subprocess


def create_socket(serverID, serviceName, service, socketName, socket):
    print("creating container...")
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
        check=True,
        text=True,
        apture_output=True
    )
    print(f"Service {socketName} started successfully!")
def stop_socket(socketName):
    subprocess.run(
        ["sudo", "systemctl", "stop", socketName],
        check=True,
        text=True,
        apture_output=True
    )
    print(f"Service {socketName} started successfully!")

def write_to_socket(socketName, msg):
        command = f"echo {msg} > /run/{socketName}"
        result = subprocess.run(
            ["sudo", "sh", "-c", command],
            check=True,
            text=True,
            capture_output=True
        )
