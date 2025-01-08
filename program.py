
from servers import create_new_server
from servers import start_server
from container import get_all_containers
from container import stop_container
from database import connect_to_database
from database import create_table
connect_to_database("root", "Bredsten7182")
create_table("mc-servers", "uuid VARCHAR(255), version VARCHAR(255), javaVersion VARCHAR(255), name VARCHAR(255), ram VARCHAR(255)")

while True:
    _cmd = input("Command:")

    if(_cmd == "list"):
        #List all servers from database
        get_all_containers()
    if(_cmd == "create"):
        _name = input("name:")
        _v = input("version:")
        create_new_server(_name, _v)
    if(_cmd == "start"):
        _id = input("id:")
        _port = input("port:")
        start_server(_id, _port)
    if(_cmd == "remove"):
        _id = input("id:")
        stop_container(_id)
    if(_cmd == "help"):
        print("list | create | remove")


