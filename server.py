from flask import Flask, send_from_directory, request, jsonify
app = Flask(__name__)
@app.route('/')
def GetIndexHTML():
    return send_from_directory("html-files", "index.html")

@app.route('/<path:filename>')
def GetCSSFiles(filename):
    return send_from_directory("html-files", filename)



from servers import start_server
from servers import stop_server
from servers import restart_server
from servers import send_command
@app.route('/exchange', methods=['POST'])
def HandleExcahnge():
    data = request.json
    print(data)
    if data.get('handleCode') is None:
        return jsonify({"status": "failure", "exitCode": 400})
    
    handleCode = data.get('handleCode')
    if handleCode == 1: # change up state
        state = handleCode = data.get('stateCode')
        serverID = handleCode = data.get('serverID')
        if state == 1: #start
            start_server(serverID)
        if state == 2: #stop
            stop_server(serverID)
        if state == 3: #restart
            restart_server(serverID)
        return jsonify({"status": "succes", "exitCode": 0})
    elif handleCode == 2: # send command
        command = handleCode = data.get('command')
        serverID = handleCode = data.get('serverID')
        send_command(command, serverID)
        return jsonify({"status": "succes", "exitCode": 0})
    elif handleCode == 3: # load data
        # Current Console
        # Player max
        # Player Count
        return jsonify({"status": "succes", "exitCode": 0})


import cusWebSocket         
cusWebSocket.start_websocket_server()

if __name__ == '__main__':
    app.run(host='192.168.10.198')