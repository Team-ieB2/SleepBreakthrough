"""
app.py
Main Application.

Copyright (C) 2023 Team ieB2. All Rights Reserved.
"""
# -*- coding: utf-8 -*-
from active_buzzer import ActiveBuzzer
from passive_buzzer import PassiveBuzzer
from obd2 import OBD2
import RPi.GPIO as GPIO
import sys
import os

class SleepBreakthrough():
    """
    メインクラス
    """
    def __init__(self):
        """
        コンストラクタ
        """
        self.obd2 = OBD2()

        self.active_buzzer_pin_GPIO_number  = 11
        self.passive_buzzer_pin_GPIO_number =  7

        self.warning_speed = 60
        self.danger_speed = 80

    def run(self):
        """
        アプリケーションを起動する
        """
        pass

    def exit(self):
        """
        アプリケーションを終了する
        """
        self.obd2.exit()
        GPIO.cleanup()
        sys.exit(0)

    def _exit(self):
        """
        アプリケーションを強制終了する
        """
        self.obd2.exit()
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