"""
app.py
Main Application.

Copyright (C) 2023 Team ieB2. All Rights Reserved.
"""
# -*- coding: utf-8 -*-
from active_buzzer import ActiveBuzzer
from passive_buzzer import PassiveBuzzer
from camera import Camera
from obd2 import OBD2
from ifttt import Ifttt
import RPi.GPIO as GPIO
from threading import Thread
import time
import sys

class SleepBreakthrough():
    """
    メインクラス
    """
    def __init__(self):
        """
        コンストラクタ
        """
        active_buzzer_pin_GPIO_number  = 23
        passive_buzzer_pin_GPIO_number =  7
        ifttt_key = "d-RW0to_f71L1cSRgRT7Y1MXg6ohfzf8N9udnWioJMW"
        self.warning_speed = 60
        self.danger_speed = 80
        self.speeds = []

        self.active_buzzer = ActiveBuzzer(active_buzzer_pin_GPIO_number)
        self.passive_buzzer = PassiveBuzzer(passive_buzzer_pin_GPIO_number)
        self.camera = Camera()
        self.obd2 = OBD2()
        self.ifttt = Ifttt(ifttt_key)

    def run(self):
        """
        アプリケーションを起動する
        """
        try:
            while True:
                # 居眠り検出スレッド
                self.doze_detection_task()
                # スピード違反検出スレッド
                self.speed_detection_task()
        except KeyboardInterrupt:
            self._exit()

    def doze_detection_task(self):
        """
        居眠り検出タスク
        """
        sleep_time_for_eye  = 0
        sleep_time_for_head = 0
        try:
            self.camera.set_time()
            self.camera.launch_camera()
            self.camera.set_faces()
            self.camera.set_eyes()
            self.camera.surround_face()
            self.camera.surround_eyes()

            if self.camera.is_eye_close():
                print("Eyes are closing")
                sleep_time_for_eye += self.camera.count_close_eye_time() - self.camera.get_time()
            else:
                sleep_time_for_eye = self.camera.reset_count_close_eye_time()

            if sleep_time_for_eye >= 1:
                print("You are sleeping because your eyes are close!")
                self.active_buzzer.warning_sound(1)
                self.ifttt.ifttt_webhook("line_event", "居眠り運転")
                self.ifttt.ifttt_webhook("post_tweet", "居眠り運転")
                sleep_time_for_eye = 0

            if self.camera.is_head_down():
                print("Head is down")
                sleep_time_for_head += self.camera.count_head_down_time() - self.camera.get_time()
            else:
                print("Head is up")
                sleep_time_for_head = self.camera.reset_count_head_down_time()

            if sleep_time_for_head >= 1:
                print("You are sleeping because your head is down")
                self.active_buzzer.warning_sound(1)
                self.ifttt.ifttt_webhook("line_event", "居眠り運転")
                self.ifttt.ifttt_webhook("post_tweet", "居眠り運転")
                sleep_time_for_head = 0

        except KeyboardInterrupt:
            self._exit()

    def speed_detection_task(self):
        """
        スピード違反検出タスク
        """
        try:
            speed = self.obd2.get_speed()

            if speed > self.warning_speed:
                self.active_buzzer.warning_sound(1)
                self.ifttt.ifttt_webhook("line_event", "スピード超過")

            if speed > self.warning_speed:
                self.active_buzzer.warning_sound(3)
                self.ifttt.ifttt_webhook("line_event", "スピード超過")

            if len(self.speeds) != 0:
                if speed - self.speeds[-1] >= 10:
                    pass

            self.speeds.append(speed)
            time.sleep(0.5)
        except KeyboardInterrupt:
            self._exit()
        except TypeError:
            pass
        except AttributeError:
            pass

    def exit(self):
        """
        アプリケーションを終了する
        """
        if self.obd2.is_connected():
            self.obd2.exit()
        self.active_buzzer.destroy()
        self.passive_buzzer.destroy()
        GPIO.cleanup()
        sys.exit(0)

    def _exit(self):
        """
        アプリケーションを強制終了する
        """
        if self.obd2.is_connected():
            self.obd2.exit()
        self.active_buzzer.destroy()
        self.passive_buzzer.destroy()
        GPIO.cleanup()
        sys.exit("Error")

if __name__ == "__main__":
    App = SleepBreakthrough()
    try:
        App.run()
    except KeyboardInterrupt:
        App.exit()
    except:
        App._exit()