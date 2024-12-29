
from servers import create_new_server
from servers import start_server
from container import get_all_containers
from container import stop_container

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
        _port = input("port:")
        start_server(_id, _ram, _port)
    if(_cmd == "remove"):
        _id = input("id:")
        stop_container(_id)
    if(_cmd == "help"):
        print("list | create | remove")