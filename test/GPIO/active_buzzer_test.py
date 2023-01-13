# -*- coding: utf-8 -*-
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

class ActiveBuzzer:
    """
    ActiveBuzzerのテストを行うクラス
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

    def warning_sound(self, con_time):
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
            if (now - start >= con_time):
                break

    def destroy(self):
        """
        終了時動作させる。
        """
        GPIO.output(self.buzzer_pin, GPIO.LOW)
        GPIO.cleanup()

    def motion(self, time):
        """
        timeで指定した秒数Buzzerを鳴らせた後、終了動作を行う。

        Args:
            time (int): 鳴らせる時間
        """
        self.warning_sound(time)
        self.destroy()

if __name__ == '__main__':
    active_buzzer = ActiveBuzzer(23)
    print("ActiveBuzzerを鳴らすテストを開始します。")
    try:
        active_buzzer.warning_sound(3)

    except KeyboardInterrupt:
        print("強制終了されました。")

    else:
        print("正常に動作しました。")

    finally:
        print("これでテストを終了します。")
        active_buzzer.destroy()