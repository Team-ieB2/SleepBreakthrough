import cv2

camera = cv2.VideoCapture(0)

# 顔認識プログラムの呼び出し
face_cascade = cv2.CascadeClassifier('learningdata/haarcascade_frontalface_alt.xml')

# 目認識プログラムの呼び出し
eye_cascade = cv2.CascadeClassifier('learningdata/haarcascade_eye.xml')

# 目認識プログラムの呼び出し(メガネの場合)
# glass_cascade = cv2.CascadeClassifier('learningdata/haarcascade_eye_tree_eyeglasses.xml')

while True:
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

  # 認識した部分(顔)に枠と色をつける
  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), recognition_frame, 2)
  
  # 認識した部分(目)に枠と色をつける
  for (x,y,w,h) in eyes:
    cv2.rectangle(frame, (x, y), (x+w, y+h), recognition_frame, 2)

  cv2.imshow("FaceRecognitionSystem", frame)
  key = cv2.waitKey(1)

  # Escキーを入力されたら画面を閉じる
  if key == 27:
    break

camera.release()
cv2.destroyAllWindows()