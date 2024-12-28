from container import create_container
from container import start_container
def create_new_server(id, ram):
    create_container(id)

def start_server(id):
    start_container(id, "256M")