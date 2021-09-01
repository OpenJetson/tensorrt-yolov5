import ctypes
import os
import random
import sys
import threading
import time

import cv2
import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import tensorrt as trt
import torch
import torchvision

def test_func(frame=np.array([])):
    flag = not np.any(frame)
    if flag:
        print ('not a frame')
    else:
        print(np.shape(frame))

capture = cv2.VideoCapture("test/video_2.mp4")

if not(capture.isOpened()):
    print('error')

test_func()

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        cv2.imshow('Frame',frame)
        print(np.shape(frame))
        test_func(frame)
        cv2.waitKey(1)
        # if cv2.waitKey(25):
        #     break
    else:
        print('ret status:',ret)
        break
