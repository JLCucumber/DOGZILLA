#!/usr/bin/env python2
# encoding: utf-8
import os
import threading
import platform
import getpass
import time
from line_common import *
import cv2 as cv
from DOGZILLALib import DOGZILLA


class LineDetect:
    def __init__(self):
        self.img = None
        self.circle = ()
        self.hsv_range = ()
        self.Roi_init = ()
        self.scale = 1000

        self.dyn_update = True

        self.select_flags = False
        self.Track_state = 'identify'
        self.windows_name = 'frame'
        self.color = color_follow()
        self.cols, self.rows = 0, 0
        self.Mouse_XY = (0, 0)
        # text_path = ''
        text_path = '/home/pi/DOGZILLA/Samples/3_AI_Visual/11_12.followline/'
        self.hsv_text = text_path+"CrossingHSV.text"
        # self.FollowLinePID = (100, 1, 50)
        self.FollowLinePID = (50, 0, 30)
        self.PID_init()

        self.dog = DOGZILLA()
        self.dog_init()
        self.cross_state = 0
        
    # 执行命令 executive command
    def execute(self, point_x, point_y, radius):
        print("point_x:%d, point_y:%d, radius:%d" % (point_x, point_y, radius))
        if point_y > 300 and radius > 150:
            if self.cross_state == 0:
                self.dog_crossing()
                self.cross_state = 1
        if self.cross_state == 0:
            [z_Pid, _] = self.PID_controller.update([(point_x - 320), 0])
            # print("point_x:%d, point_y:%d, radius:%d, z_Pid:%d" % (point_x, point_y, radius, int(z_Pid)))
            self.dog.forward(25)
            self.dog.turn(int(z_Pid))
    # 停止 stop
    def cancel(self):
        self.dog.reset()
        
    # 开启越障模式 Enable obstacle crossing mode
    def dog_crossing(self):
        self.dog.stop()
        time.sleep(.01)
        self.dog.gait_type("high_walk")
        time.sleep(.01)
        self.dog.forward(25)

    # 初始化机器狗  init DOGZILLA
    def dog_init(self):
        self.dog.stop()
        time.sleep(.01)
        self.dog.pace("slow")
        time.sleep(.01)
        self.dog.translation('z', 90)
        time.sleep(.01)
        self.dog.attitude('p', 10)

    # 程序处理 program processing
    def process(self, rgb_img, action):
        binary = []
        rgb_img = cv.resize(rgb_img, (640, 480))

        # rgb_img = cv.flip(rgb_img, 1)
        if action == 32: self.Track_state = 'tracking'
        elif action == ord('i') or action == 105: self.Track_state = "identify"
        elif action == ord('r') or action == 114: self.Reset()

        if self.Track_state == 'init':
            cv.namedWindow(self.windows_name, cv.WINDOW_AUTOSIZE)
            cv.setMouseCallback(self.windows_name, self.onMouse, 0)
            if self.select_flags == True:
                cv.line(rgb_img, self.cols, self.rows, (255, 0, 0), 2)
                cv.rectangle(rgb_img, self.cols, self.rows, (0, 255, 0), 2)
                if self.Roi_init[0]!=self.Roi_init[2] and self.Roi_init[1]!=self.Roi_init[3]:
                    rgb_img, self.hsv_range = self.color.Roi_hsv(rgb_img, self.Roi_init)
                    self.dyn_update = True
                else: self.Track_state = 'init'
        elif self.Track_state == "identify":
            if os.path.exists(self.hsv_text): self.hsv_range = read_HSV(self.hsv_text)
            else: self.Track_state = 'init'
        if self.Track_state != 'init' and len(self.hsv_range) != 0:
            rgb_img, binary, self.circle = self.color.line_follow(rgb_img, self.hsv_range)
            if self.dyn_update == True :
                write_HSV(self.hsv_text, self.hsv_range)
                self.dyn_update = False
        if self.Track_state == 'tracking':
            if len(self.circle) != 0:
                threading.Thread(target=self.execute, args=(self.circle[0], self.circle[1], self.circle[2])).start()
        return rgb_img, binary
    
    # 鼠标操作 mouse action
    def onMouse(self, event, x, y, flags, param):
        if event == 1:
            self.Track_state = 'init'
            self.select_flags = True
            self.Mouse_XY = (x,y)
        if event == 4:
            self.select_flags = False
            self.Track_state = 'mouse'
        if self.select_flags == True:
            self.cols = min(self.Mouse_XY[0], x), min(self.Mouse_XY[1], y)
            self.rows = max(self.Mouse_XY[0], x), max(self.Mouse_XY[1], y)
            self.Roi_init = (self.cols[0], self.cols[1], self.rows[0], self.rows[1])

    # 重置 reset
    def Reset(self):
        self.PID_init()
        self.Track_state = 'init'
        self.hsv_range = ()
        self.dog_init()
        self.cross_state = 0

    # 初始化PID参数 init PID parameter
    def PID_init(self):
        self.PID_controller = simplePID(
            [0, 0],
            [self.FollowLinePID[0] / 1.0 / (self.scale), 0],
            [self.FollowLinePID[1] / 1.0 / (self.scale), 0],
            [self.FollowLinePID[2] / 1.0 / (self.scale), 0])


if __name__ == '__main__':
    line_detect = LineDetect()

    capture = cv.VideoCapture(0)
    cv_edition = cv.__version__
    if cv_edition[0]=='3': capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'XVID'))
    else: capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc('M', 'J', 'P', 'G'))
    capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    while capture.isOpened():
        start = time.time()
        ret, frame = capture.read()
        action = cv.waitKey(10) & 0xFF
        frame, binary = line_detect.process(frame, action)
        end = time.time()
        fps = 1 / (end - start)
        text = "FPS : " + str(int(fps))
        cv.putText(frame, text, (30, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (100, 200, 200), 1)
        if len(binary) != 0: cv.imshow('frame', ManyImgs(1, ([frame, binary])))
        else:cv.imshow('frame', frame)
        if action == ord('q') or action == 113:
            line_detect.cancel()
            break
    
    capture.release()
    cv.destroyAllWindows()
