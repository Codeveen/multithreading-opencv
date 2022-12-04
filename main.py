import cv2
from threading import Thread
import time

class WebcamStream:

    def __init__(self, stream_id=0):
        self.stream_id = stream_id

        self.vcap = cv2.VideoCapture(self.stream_id)
        if self.vcap.isOpened() is False:
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)
        fps_input_stream = int(self.vcap.get(5))  # hardware fps
        print("FPS of input stream: {}".format(fps_input_stream))

        # reading a single frame from vcap stream for initializing
        self.grabbed, self.frame = self.vcap.read()
        if self.grabbed is False:
            print('[Exiting] No more frames to read')
            exit(0)
        # self.stopped is initialized to False
        self.stopped = True
        # thread instantiation
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True  # daemon threads run in background

        # method to start thread
    def start(self):
            self.stopped = False
            self.t.start()

        # method passed to thread to read next available frame
    def update(self):
            while True:
                if self.stopped is True:
                    break
                self.grabbed, self.frame = self.vcap.read()
                if self.grabbed is False:
                    print('[Exiting] No more frames to read')
                    self.stopped = True
                    break
            self.vcap.release()

        # method to return latest read frame
    def read(self):
            return self.frame

        # method to stop reading frames
    def stop(self):
            self.stopped = True

webcam_0 = WebcamStream(stream_id=0) # 0 id for main camera
webcam_1 = WebcamStream(stream_id=1)
webcam_2 = WebcamStream(stream_id=2)
webcam_3 = WebcamStream(stream_id=3)
webcam_4 = WebcamStream(stream_id=4)


webcam_0.start()
webcam_1.start()
webcam_2.start()
webcam_3.start()
webcam_4.start()

while True :
    if webcam_0.stopped is True or webcam_1.stopped is True :
        break
    else :
        frame1 = webcam_0.read()
        frame2 = webcam_1.read()
        frame3 = webcam_2.read()
        frame4 = webcam_3.read()
        frame5 = webcam_4.read()

    delay = 0.03 # delay value in seconds
    time.sleep(delay)

    cv2.imshow('frame1' , frame1)
    cv2.imshow('frame2', frame2)
    cv2.imshow('frame3', frame3)
    cv2.imshow('frame4', frame4)
    cv2.imshow('frame5', frame5)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

webcam_0.stop() # stop the webcam stream
webcam_1.stop()
webcam_2.stop()
webcam_3.stop()
webcam_4.stop()
cv2.destroyAllWindows()