# -*- coding: utf-8 -*-

import cv2
import time
import numpy as np
import os
import pathlib

# 顔認識プログラムのパス(絶対パス)
face_cascade_path = os.path.abspath("learningdata/haarcascade_frontalface_alt.xml")
face_cascade_path = str(pathlib.PurePath(face_cascade_path))

# 目認識プログラムのパス(絶対パス)
eye_cascade_path = os.path.abspath("learningdata/haarcascade_eye_tree_eyeglasses.xml")
eye_cascade_path = str(pathlib.PurePath(eye_cascade_path))

def camera_recognition():

  # デバイスを読み込む
  camera = cv2.VideoCapture(0)

  # 時間の配列の場所指定
  index = 0

  # 目を閉じた回数を記録
  eye_close_count = 0

  # ループ回数が一定に達したかどうか判定する
  judge = 0

  # 頭を下げた回数を記録
  head_down_count = 0

  # 顔の枠面積を保存する配列
  face_frame_area = []

  # 顔だけで判定させるかどうかを決めるfrag
  eye_frag = True

  # 顔認識プログラムの呼び出し(プログラム単体呼び出しの場合)
  # face_cascade = cv2.CascadeClassifier('learningdata/haarcascade_frontalface_alt.xml')

  # 顔認識プログラムの呼び出し(関数呼び出しの場合)
  face_cascade = cv2.CascadeClassifier(face_cascade_path)

  # 目認識プログラムの呼び出し(プログラム単体呼び出しの場合)
  # eye_cascade = cv2.CascadeClassifier('learningdata/haarcascade_eye_tree_eyeglasses.xml')

  # 目認識プログラムの呼び出し(関数呼び出しの場合)
  eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

  # 目認識プログラムの呼び出し(メガネの場合)
  # glass_cascade = cv2.CascadeClassifier('learningdata/haarcascade_eye_tree_eyeglasses.xml')

  # 時間計測開始
  time.time()
  times = 0

  while True:
    # 現在の時間を取得する
    now_time = time.time()

    times += now_time

    # return するかどうかのfrag
    frag = False

    # 画像の取り出し
    ret, frame = camera.read()
    if not ret:
      break

    # 鏡表示
    frame = cv2.flip(frame, 1)

    # 画像を白黒にする
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 認識したものの枠の色を決める
    # recognition_frame = (0, 0, 255)

    face_frame = (255, 0, 0)
    eye_frame = (0, 0, 255)

    # 顔認識の実行
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minSize=(50,50))

    # 目認識の実行
    eyes = eye_cascade.detectMultiScale(gray, minSize=(75,75))

    # (初回時のみ)目認識ができなかった場合(メガネ・サングラスなどで認識不可だった)にeye_fragをおろす
    if judge <= 25:
      if len(eyes) == 0:
        eye_frag = False
      else:
        eye_frag = True

    # 認識した部分(顔)に枠と色をつける
    for (x,y,w,h) in faces:
      # cv2.rectangle(frame, (x, y), (x+w, y+h), recognition_frame, 2)
      cv2.rectangle(frame, (x, y), (x+w, y+h), face_frame, 2)
      # print(w*h)

    # 認識した部分(目)に枠と色をつける
    for (x,y,w,h) in eyes:
      # cv2.rectangle(frame, (x, y), (x+w, y+h), recognition_frame, 2)
      cv2.rectangle(frame, (x, y), (x+w, y+h), eye_frame, 2)

    # cv2.imshow("FaceRecognitionSystem", frame)
    key = cv2.waitKey(1)

    # 目を認識できた場合
    if eye_frag and judge > 25:
      # 目を閉じている場合
      if len(eyes) < 2 and len(faces) >= 1:
        closed_time = time.time()
        times -= closed_time
        print("eye: " + str(eye_close_count))

        if times < 0:
          eye_close_count += 1
          times = 0
        else:
          eye_close_count = 0

        if eye_close_count >= 100:
          frag = True
          break

        times = 0
    # 顔の下がった回数をカウント
    elif judge > 25:
      if len(faces) != 0:
        for (x, y, w, h) in faces:
          face_frame_area.append(w * h)
          frame_avg = np.mean(face_frame_area)
          index += 1

        if index >= 2 and len(face_frame_area) > 2:
          print(head_down_count)
          # face_diff = face_frame_area[index-1] - face_frame_area[index-2]
          face_diff =  w * h - frame_avg
          if face_diff < -10000:
            head_down_count += 1

          else:
            face_frame_area = []
            index = 0
            continue

          if head_down_count >= 50:
            frag = True
            break

    judge += 1

    # Escキーを入力されたら画面を閉じる
    if key == 27:
      break

  camera.release()
  cv2.destroyAllWindows()

  return frag


if __name__ == "__main__":
  camera_recognition()

if __name__ == "camera.cameratest":
  face_cascade_path = os.path.abspath("camera/learningdata/haarcascade_frontalface_alt.xml")
  eye_cascade_path = os.path.abspath("camera/learningdata/haarcascade_eye_tree_eyeglasses.xml")