from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640, 480)
camera.start_preview()
sleep(60)
camera.stop_preview()
camera.capture("temp.jpg")
