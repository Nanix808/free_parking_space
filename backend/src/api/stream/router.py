from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from .schemas import Offer
from api.database import get_db
from aiortc import RTCPeerConnection, RTCSessionDescription
from api.parking.service import ParkingDAL
from aiortc import (
    RTCPeerConnection,
    RTCSessionDescription,
)
from .stream import Stream
from sqlalchemy.ext.asyncio import AsyncSession
from api.connectionmanager import manager

stream_to_web = APIRouter()
pcs = set()


@stream_to_web.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_json()
            websocket.data = data
            await manager.send_personal_message(f"You wrote: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket,  client_id)


@stream_to_web.post("/offer")
async def offer(params: Offer, db: AsyncSession = Depends(get_db)):
    async with db as session:
        async with session.begin():
            offer = RTCSessionDescription(sdp=params.sdp, type=params.type)
            client_id = params.client_id
            setting = params.setting
            pc = RTCPeerConnection()
            pcs.add(pc)
           
            WebSocket_id = await manager.get_by_id(client_id=client_id)

            @pc.on("connectionstatechange")
            async def on_connectionstatechange():
                print("Connection state is %s" % pc.connectionState)
                if pc.connectionState == "failed":
                    await pc.close()
                    pcs.discard(pc)

            if not setting:
                parking_dal = ParkingDAL(session)

                answer = await parking_dal.get_parking_by_rtsp(
                    rtsp=params.rtsp
                )
                circles = answer.circle
                conf = answer.conf
                iou = answer.iou
                video = Stream(params.rtsp, circles=circles, preprocesing=True,
                               conf=conf, iou=iou, websoket=WebSocket_id)
            else:
                client_id = params.client_id
                video = Stream(params.rtsp, preprocesing=True,
                               websoket=WebSocket_id)
            if video:
                pc.addTrack(video)
            await pc.setRemoteDescription(offer)

            answer = await pc.createAnswer()
            await pc.setLocalDescription(answer)

            return {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
