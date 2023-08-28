from typing import Union
import cv2
from time import time
from av import VideoFrame
from aiortc import VideoStreamTrack
import uuid



class Stream(VideoStreamTrack):
   
    def __init__(self, filename: Union[str, int],target_fps: int = None,  name:str = 'New',  preprocesing: bool = False):
        super().__init__()
        self.filename = filename
        self.name = name
        # self._id = str(uuid.uuid4())
        
        # cv2.namedWindow(self.name)
        # cv2.setMouseCallback(self.name, self.drawRectangle)
        self._cap = cv2.VideoCapture(self.filename)
        if not self.isOpened():
            raise FileNotFoundError("Stream not found")
        self.target_fps = target_fps
        self.fps = None
        self.extract_freq = None
        self.compute_extract_frequency()
        self._frame_index = 0
        self.preprocesing = preprocesing


    def drawRectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE :  
            colorsBGR = [x, y]
            print(colorsBGR)

    def compute_extract_frequency(self):
        """evaluate the frame rate over a period of 5 seconds"""
        self.fps = self._cap.get(cv2.CAP_PROP_FPS)
        if self.fps == 0:
            self.compute_origin_fps()

        if self.target_fps is None:
            self.extract_freq = 1
        else:
            self.extract_freq = int(self.fps / self.target_fps)
            # print(self.extract_freq, self.fps , self.target_fps)
            if self.extract_freq == 0:
                raise ValueError("desired_fps is higher than half the stream frame rate")

    def compute_origin_fps(self, evaluation_period: int = 5):
        """evaluate the frame rate over a period of 5 seconds"""
        while self.isOpened():
            ret, _ = self._cap.read()
            if ret is True:
                if self._frame_index == 0:
                    start = time()

                self._frame_index += 1

                if time() - start > evaluation_period:
                    break

        self.fps = round(self._frame_index / (time() - start), 2)

    def frame_preprocesing(self, frame):
        """Grabs, decodes and returns the next subsampled video frame."""
        if self.preprocesing:
            return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    

    def read(self):
        """Grabs, decodes and returns the next subsampled video frame."""
        ret, frame = self._cap.read()
        if ret is True:
            self._frame_index += 1
            if self._frame_index == self.extract_freq:
                self._frame_index = 0
                frame = self.frame_preprocesing(frame)
                return ret, frame

        return False, False
    
    async def recv(self):

        
        pts, time_base = await self.next_timestamp()
        res, img = self._cap.read()
        img = self.frame_preprocesing(img)
        frame = VideoFrame.from_ndarray(img, format='rgb24')
        frame.pts = pts
        frame.time_base = time_base
        return frame

    def isOpened(self):
        """Returns true if video capturing has been initialized already."""
        # print(self.__dict__)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     return False
        return self._cap.isOpened()

    def release(self):
        """Closes video file or capturing device."""
        self._cap.release()
        cv2.destroyAllWindows() 



class VideoTransformTrack(VideoStreamTrack):
    def __init__(self, file_name):
        super().__init__()  # don't forget this!
        # self.video = cv2.VideoCapture(self.filename)
        # video1 = 'rtsp://root:Password01@172.16.10.245:554/live.sdp'
        video = cv2.VideoCapture(file_name)
        # video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        # video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

        self.video = video

    async def recv(self):
        pts, time_base = await self.next_timestamp()
        res, img = self.video.read()
        frame = VideoFrame.from_ndarray(img, format="bgr24")
        print(pts)
        frame.pts = pts
        frame.time_base = time_base
        return frame