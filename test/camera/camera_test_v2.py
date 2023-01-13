import cv2
import time
import numpy as np
import os


class CameraTest():
    def __init__(self):
        print("カメラシステムの初期化開始")
        self.time = 0.0
        self.camera = None
        self.eye_close_time = 0
        self.head_down_count = 0
        self.ret = None
        self.frame = None
        self.faces = None
        self.face_diff = 0
        self.face_avg = 0
        self.eyes = None
        self.face_frame = (255, 0, 0)
        self.eye_frame = (0, 0, 255)
        self.face_cascade_path = os.path.abspath("camera/learningdata/haarcascade_frontalface_alt.xml")
        self.eye_cascade_path = os.path.abspath("camera/learningdata/haarcascade_eye_tree_eyeglasses.xml")
        self.gray = None
        self.face_area = []
        print("カメラシステム初期化完了")
    
    def launch_camera(self):
        self.camera = cv2.VideoCapture(0)
        self.ret, self.frame = self.camera.read()
        if not self.ret:
            return True
        self.frame = cv2.flip(self.frame, 1)
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.face_cascade = cv2.CascadeClassifier(self.face_cascade_path)
        self.eye_cascade = cv2.CascadeClassifier(self.eye_cascade_path)
    
    def surround_face(self):
        for (x, y, w, h) in self.get_faces():
            cv2.rectangle(self.frame, (x, y), (x+w, y+h), self.face_frame, 2)
    
    def surround_eyes(self):
        for (x, y, w, h) in self.get_eyes():
            cv2.rectangle(self.frame, (x, y), (x+w, y+h), self.eye_frame, 2)

    def count_close_eye_time(self):
        self.count_close_eye_time = time.time()
    

    def count_head_down(self):
        self.head_down_count += 1


    def is_eye_close(self):
        if len(self.get_eyes()) == 0:
            return True

    def is_head_down(self):
        if len(self.get_faces()) != 0:
            for (x, y, w, h) in self.get_faces():
                self.add_face_area(h)
                self.culc_face_avg(self.get_face_area())

            self.set_face_diff(h - self.get_face_avg())

        if self.get_face_diff() > 10:
            return True

    def add_face_area(self, area):
        self.face_area.append(area)

    def culc_face_avg(self, face_area):
        self.face_avg = np.mean(face_area)

    def set_faces(self):
        self.faces = self.face_cascade.detectMultiScale(self.gray, scaleFactor=1.1, minSize=(50,50))
    
    def set_eyes(self):
        self.eyes = self.eye_cascade.detectMultiScale(self.gray)

    def set_face_diff(self, diff):
        self.face_diff = diff

    def set_time(self):
        self.time = time.time()

    def get_count_close_eye_time(self):
        return self.count_close_eye_time
    
    def get_head_down_count(self):
        return self.head_down_count

    def get_face_area(self):
        return self.face_area
    
    def get_face_avg(self):
        return self.face_avg
    
    def get_face_diff(self):
        return self.face_diff

    def get_eyes(self):
        return self.eyes
    
    def get_faces(self):
        return self.faces

    def get_time(self):
        return self.time

    def reset_count_close_eye_time(self):
        self.eye_close_time = 0

    def reset_count_head_down(self):
        self.head_down_count = 0

    def wait_time(self):
        time.sleep(0.2)