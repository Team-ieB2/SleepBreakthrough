"""
active_buzzer.py
Active Buzzer Controller.

Copyright (C) 2023 Team ieB2. All Rights Reserved.
"""
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

class ActiveBuzzer:
    """
    ActiveBuzzerのクラス
    """
    def __init__(self,buzzer_pin):
        """
        ActiveBuzzerクラスのコンストラクタ

        Args:
            buzzer_pin (int): どのピンを用いるのか指定する。
        """
        self.buzzer_pin = buzzer_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        GPIO.output(self.buzzer_pin, GPIO.LOW)

    def warning_sound(self, time):
        """
        Buzzerをtimeで指定した秒数の間鳴らす

        Args:
            time (int): 鳴らす時間
        """
        start = time.time()
        while True:
            GPIO.output(self.buzzer_pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.buzzer_pin, GPIO.LOW)
            time.sleep(0.5)
            now = time.time()
            if (now - start >= time):
                break

    def destroy(self):
        """
        終了時動作させる。
        """
        GPIO.output(self.buzzer_pin, GPIO.LOW)

    def motion(self, time):
        """
        timeで指定した秒数Buzzerを鳴らせた後、終了動作を行う。

        Args:
            time (int): 鳴らせる時間
        """
        self.warning_sound(time)
        self.destroy()