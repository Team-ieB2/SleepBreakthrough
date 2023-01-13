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
import sys

class SleepBreakthrough():
    """
    メインクラス
    """
    def __init__(self):
        """
        コンストラクタ
        """
        active_buzzer_pin_GPIO_number  = 11
        passive_buzzer_pin_GPIO_number =  7
        ifttt_key = "bWxY8YDIyu6O_pyDNE61XJ"
        self.warning_speed = 60
        self.danger_speed = 80

        self.active_buzzer = ActiveBuzzer(active_buzzer_pin_GPIO_number)
        self.passive_buzzer = PassiveBuzzer(passive_buzzer_pin_GPIO_number)
        self.camera = Camera()
        self.obd2 = OBD2()
        self.ifttt = Ifttt(ifttt_key)

    def run(self):
        """
        アプリケーションを起動する
        """
        while True:
            # 居眠り検出スレッド
            Thread(target=self.doze_detection_task).start()
            # スピード違反検出スレッド
            Thread(target=self.speed_detection_task).start()

    def doze_detection_task(self):
        """
        居眠り検出タスク
        """
        pass

    def speed_detection_task(self):
        """
        スピード違反検出タスク
        """
        pass

    def exit(self):
        """
        アプリケーションを終了する
        """
        self.obd2.exit()
        self.active_buzzer.destroy()
        self.passive_buzzer.destroy()
        GPIO.cleanup()
        sys.exit(0)

    def _exit(self):
        """
        アプリケーションを強制終了する
        """
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