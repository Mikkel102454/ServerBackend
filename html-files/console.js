async function ExchangeServer(request){
    console.log(request);
    var response = await fetch("http://192.168.10.197:5000/exchange", {
        method: "POST",
        headers: {'Content-Type': 'application/json' },
        body: JSON.stringify(request)
    });
    var data = await response.json();

    if(data.newToken) {
        SetToken(data.newToken);
        token = data.newToken;
    }
    console.log(data);
    return data;
}

function startServer(){
    serverID = document.getElementById("serverID").value.trim();
    ExchangeServer({"handleCode": 1, "stateCode": 1, "serverID": serverID});
}
function stopServer(){
    serverID = document.getElementById("serverID").value.trim();
    ExchangeServer({"handleCode": 1, "stateCode": 2, "serverID": serverID});
}
function restartServer(){
    serverID = document.getElementById("serverID").value.trim();
    ExchangeServer({"handleCode": 1, "stateCode": 3, "serverID": serverID});
}
function sendCommand(){
    serverID = document.getElementById("serverID").value.trim();
    command = document.getElementById("command").value.trim();
    ExchangeServer({"handleCode": 2, "command": command, "serverID": serverID});
}

