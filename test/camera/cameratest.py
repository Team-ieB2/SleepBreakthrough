# -*- coding: utf-8 -*-

import cv2
import time
import numpy as np


def camera_recognition():
  # デバイスを読み込む
  camera = cv2.VideoCapture(0)

  # 初回だけ判定する変数
  at_first = 0

  # 時間の配列の場所指定
  index = 0

  # 目を閉じた回数を記録
  eye_close_count = 0

  # 頭を下げた回数を記録
  head_down_count = 0

  # 目を閉じた時間を計測する配列
  eye_close_times = []

  # 顔の枠面積を保存する配列
  face_frame_area = []

  # 顔だけで判定させるかどうかを決めるfrag
  eye_frag = True

  # 顔認識プログラムの呼び出し
  face_cascade = cv2.CascadeClassifier('learningdata/haarcascade_frontalface_alt.xml')

  # 目認識プログラムの呼び出し
  eye_cascade = cv2.CascadeClassifier('learningdata/haarcascade_eye.xml')

  # 目認識プログラムの呼び出し(メガネの場合)
  # glass_cascade = cv2.CascadeClassifier('learningdata/haarcascade_eye_tree_eyeglasses.xml')

  # 時間計測開始
  time_start = time.time()

  while True:
    now_time = time.time()
    frag = True

    # 画像の取り出し
    ret, frame = camera.read()
    if not ret:
      break

    # 鏡表示
    frame = cv2.flip(frame, 1)

    # 画像を白黒にする
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 認識したものの枠の色を決める
    recognition_frame = (0, 0, 255)

    # 顔認識の実行
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # 目認識の実行
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)

    # (初回時のみ)目認識ができなかった場合(メガネ・サングラスなどで認識不可だった)にeye_fragをおろす
    if at_first == 0 and len(eyes) == 0:
      eye_frag = False

    # 認識した部分(顔)に枠と色をつける
    for (x,y,w,h) in faces:
      cv2.rectangle(frame, (x, y), (x+w, y+h), recognition_frame, 2)
      print(x, y, w, h)
    
    # 認識した部分(目)に枠と色をつける
    for (x,y,w,h) in eyes:
      cv2.rectangle(frame, (x, y), (x+w, y+h), recognition_frame, 2)

    cv2.imshow("FaceRecognitionSystem", frame)
    key = cv2.waitKey(1)

    # 目を認識できた場合
    if eye_frag:
      # 目を閉じている場合
      if len(eyes) < 2 and len(faces) >= 1:
        eye_close_times.append(time.time()-now_time)

        if index == 0:
          continue
        else:
          if eye_close_times[index] - eye_close_times[index-1] < 0.5:
            eye_close_count += 1
          else:
            eye_close_count = 0
            eye_close_times = []
            index = 0
            continue
        
        if eye_close_count >= 300:
          frag = True
          break

        index += 1
    # 顔の下がった回数をカウント
    else:
      face_frame_area.append(faces[-2]*faces[-1])
      frame_avg = np.mean(face_frame_area)

      if index <= 2:
        continue

      else:
        face_diff = face_frame_area[index] - face_frame_area[index-1]
        if face_diff < frame_avg:
          frag = True
          break
        else:
          face_frame_area = []
          index = 0
          continue

      index += 1
    
    at_first += 1

    # Escキーを入力されたら画面を閉じる
    if key == 27:
      break

    return frag

  camera.release()
  cv2.destroyAllWindows()