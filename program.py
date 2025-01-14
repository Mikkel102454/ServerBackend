
from servers import create_new_server
from servers import start_server
from servers import stop_server
from servers import send_command
#from database import connect_to_database
#from database import create_table
#connect_to_database("mikkel", "Bredsten7182")
#create_table("mc-servers", "ID INT AUTO_INCREMENT PRIMARY KEY, uuid VARCHAR(255), version VARCHAR(255), name VARCHAR(255), ram VARCHAR(255)")

while True:
    _cmd = input("Command:")

    if(_cmd == "create"):
        _name = input("name:")
        _v = input("version:")
        create_new_server(_name, _v)
    elif(_cmd == "start"):
        _id = input("id:")
        _port = input("port:")
        start_server(_id, _port)
    elif(_cmd == "remove"):
        _id = input("id:")
        stop_server(_id)
    elif(_cmd == "cmd"):
        _id = input("id:")
        _cmd = input("cmd:")
        send_command(_cmd, _id)
    elif(_cmd == "help"):
        print("list | create | remove")


