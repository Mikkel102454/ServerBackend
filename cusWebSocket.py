import asyncio
import websockets
import json

# Map server IDs to connected clients
server_clients = {}

async def handler(websocket, path):
    # Extract server ID from the path (e.g., ws://ip/serverID)
    server_id = path.strip("/")
    if server_id not in server_clients:
        server_clients[server_id] = set()

    # Register the client
    server_clients[server_id].add(websocket)
    print(f"Client connected to {server_id}")

    try:
        async for message in websocket:
            print(f"Received from {server_id}: {message}")
    except websockets.ConnectionClosed:
        print(f"Client disconnected from {server_id}")
    finally:
        # Unregister the client
        server_clients[server_id].remove(websocket)
        if not server_clients[server_id]:
            del server_clients[server_id]



async def broadcast_update(server_id, update):
    # Broadcast the update to all connected clients of the given server
    if server_id in server_clients:
        message = json.dumps(update)
        await asyncio.wait([client.send(message) for client in server_clients[server_id]])

async def simulate_console_updates():
    # Simulate updates for multiple servers
    while True:
        for server_id in server_clients.keys():
            update = {
                "timestamp": "2025-01-17 12:00:00",
                "server": server_id,
                "log": f"Console update for {server_id}"
            }
            await broadcast_update(server_id, update)
        await asyncio.sleep(1)  # Simulate 1-second delay

async def start_websocket_server():
    """Starts the WebSocket server."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    websocket_server = websockets.serve(handler, "localhost", 8765)
    loop.run_until_complete(websocket_server)
    loop.run_until_complete(simulate_console_updates())
    loop.run_forever()