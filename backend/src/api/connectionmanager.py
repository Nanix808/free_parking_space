from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
        self.client_id: list[int] = []

    async def connect(self, websocket: WebSocket, client_id: int):
        await websocket.accept()
        websocket.data = False
        self.active_connections.append(websocket)
        self.client_id.append(client_id)

    async def get_by_id(self, client_id: int):
        index = self.client_id.index(client_id)
        return self.active_connections[index]

    def disconnect(self, websocket: WebSocket,  client_id: int):

        self.active_connections.remove(websocket)
        self.client_id.remove(client_id)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_json(message)


manager = ConnectionManager()
