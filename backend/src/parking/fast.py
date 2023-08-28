import cv2
from typing import Union
import uvicorn
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse

async def gen_frames():
    cap=  cv2.VideoCapture(0)

    while True:
        # for cap in caps:
        # # Capture frame-by-frame
        success, frame = cap.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  
    

app = FastAPI()


@app.get("/webcam")
async def webcam_display():
    return StreamingResponse(gen_frames(),media_type = 'multipart/x-mixed-replace; boundary=frame')

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.websocket("/ws")
async def get_stream(websocket: WebSocket):
    camera =  cv2.VideoCapture(0)
    await websocket.accept()
    try:
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                await websocket.send_bytes(buffer.tobytes())  
    except WebSocketDisconnect:
        print("Client disconnected")  


if __name__ =="__main__":
    print('2222')
    # uvicorn.run(app="main:app", reload=True, port=8080, host="0.0.0.0")
    uvicorn.run(app="fast:app", host='127.0.0.1',  port=8000, reload=True)