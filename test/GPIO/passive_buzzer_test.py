# -*- coding: utf-8 -*-
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

class PassiveTest:
    """
    PassiveBuzzerのテストを行うクラス。
    """
    #演奏速度
    speed = 1

    #音階
    TONES = {"c6":1047,
        "b5":988,
        "a5":880,
        "g5":784,
        "f5":698,
        "e5":659,
        "eb5":622,
        "d5":587,
        "c5":523,
        "b4":494,
        "a4":440,
        "ab4":415,
        "g4":392,
        "f4":349,
        "e4":330,
        "eb4":311,
        "d4":294,
        "c4":262}

    #エリーゼのために (サンプルコードから)
    ELISE_SONG =	[
        ["e5",16],["eb5",16],
        ["e5",16],["eb5",16],["e5",16],["b4",16],["d5",16],["c5",16],
        ["a4",8],["p",16],["c4",16],["e4",16],["a4",16],
        ["b4",8],["p",16],["e4",16],["ab4",16],["b4",16],
        ["c5",8],["p",16],["e4",16],["e5",16],["eb5",16],
        ["e5",16],["eb5",16],["e5",16],["b4",16],["d5",16],["c5",16],
        ["a4",8],["p",16],["c4",16],["e4",16],["a4",16],
        ["b4",8],["p",16],["e4",16],["c5",16],["b4",16],["a4",4]
        ]

    #棺桶のやつ (自作 未検証)
    COFFIN_SONG =	[
        ["a4",32],["a4",16],["e4",16],["eb4",16],["c4",16],["p",16],
        ["b4",32],["b4",16],["c5",16],["d5",8],["p",8],["d5",16],["c5",8],["b4",16],
        ["a4",32],["a4",16],["c6",16],["b5",16],["c6",16],["b5",16],["c6",16],
        ["a4",32],["a4",16],["c6",16],["b5",16],["c6",16],["b5",16],["c6",16],["p",8]
        ]
    def __init__(self,buzzer_pin):
        """
        PassiveTestクラスのコンストラクタ

        Args:
            buzzer_pin (int): どのピンを用いるのか指定する。
        """
        self.buzzer_pin = buzzer_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(buzzer_pin, GPIO.OUT)

    def change_speed(self, speed):
        """
        演奏速度の変更を行う
        Args:
            speed (int): 変更後の速度
        """
        self.speed = speed
        
    def playTone(self,p,tone):
        """
        音を鳴らす

        Args:
            p (Any): GPIO.PWM
            tone (list): 鳴らす音とその時間
        """
        duration = (1./(tone[1]*0.25*self.speed))

        if tone[0] == "p": #休符
            time.sleep(duration)
        else: #演奏する部分
            frequency = self.TONES[tone[0]]
            p.ChangeFrequency(frequency)
            p.start(0.5)
            time.sleep(duration)
            p.stop()


    
    def elise(self):
        """
        「エリーゼのために」を演奏する
        """
        p = GPIO.PWM(self.buzzer_pin, 440)
        p.start(0.5)
        for t in self.ELISE_SONG:
            self.playTone(p,t)
    
    def coffin(self):
        """
        Coffin Danceの曲を演奏する
        """
        p = GPIO.PWM(self.buzzer_pin, 440)
        p.start(0.5)
        for t in self.COFFIN_SONG:
            self.playTone(p,t)
    
    def destroy(self):
        """
        終了時動作させる。
        """
        GPIO.output(self.buzzer_pin, GPIO.HIGH)
        GPIO.cleanup()
        

if __name__ == '__main__':
    passive_test = PassiveTest(11)
    print("演奏を開始します。")
    try:
        print("エリーゼのために")
        passive_test.elise()
        
        print("coffin")
        passive_test.coffin()
    except KeyboardInterrupt:
        print("強制終了されました。")
    else:
        print("正常に演奏できました。")
    finally:
        print("演奏を終了します。")
        passive_test.destroy()