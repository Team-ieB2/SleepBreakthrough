# Sleep Breakthrough
![GitHub watchers](https://img.shields.io/github/watchers/Team-ieB2/SleepBreakthrough?style=social)
![RaspberryPi](https://img.shields.io/badge/-Raspberrypi-C51A4A.svg?logo=raspberrypi&style=plastic)
![Python](https://img.shields.io/badge/python-v3.9.12-007396.svg?logo=python&style=popout)

本プログラムは、RaspberryPiを使用した、車載用居眠り運転検出システムである。
RaspberryPiに接続されたカメラを使用して、対象の頭の位置を認識する。頭の位置が下がった場合、居眠りと判定しブザーを鳴らす。
また、OBD2コネクターを使用し、車両の走行スピードを監視する。走行スピードが法定速度を超えた場合、スピード違反を知らせるため、ブザーを鳴らす。

# Requirement

* Raspberry Pi OS Lite
* python 3.9.12
* numpy 1.24.1
* obd 0.7.0
* opencv-python 4.7.0.68
* [buzzer](https://www.amazon.co.jp/gp/product/B01FYQ6EWC/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li3&tag=creepfablic-22&linkId=a2dadd6988f2cc6594454eb38ee7f435&language=ja_JP)
* [Web Camera](https://www.amazon.co.jp/-/en/Logitech-C270n-Streaming-Compatible-Windows/dp/B07QMKND9M/ref=sr_1_5?adgrpid=110957742715&hvadid=651071561209&hvdev=c&hvlocphy=9053273&hvnetw=g&hvqmt=b&hvrand=6623804605978176530&hvtargid=kwd-1013038288684&hydadcr=4771_13316645&jp-ad-ap=0&keywords=%E3%82%AB%E3%83%A1%E3%83%A9%E3%82%A6%E3%82%A7%E3%83%96&qid=1682880391&sr=8-5)
* [OBD2 Connector](https://www.amazon.co.jp/Diagnostic-Bluetooth-Installation-Information-supported/dp/B07RNHZS44/ref=sr_1_2_sspa?crid=6MS69KCUP4CJ&keywords=OBD2&qid=1682880410&sprefix=obd%2Caps%2C231&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTU1ZRlM3MkdMUlg3JmVuY3J5cHRlZElkPUEwNDY3MjY1MzVEVzFMWVdFRlZVSiZlbmNyeXB0ZWRBZElkPUEyQlFFSTlUVEQ5VEpWJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)

# Usage

ラズパイにて、以下のコマンドを実行する。

```
$ mkdir src
$ cd src
$ git clone git@github.com:Team-ieB2/SleepBreakthrough.git
$ cd SleepBreakthrough
$ pip install -r requirements.txt
$ mv ./sh/etc/rc.local /etc/
$ mv ./sh/usr/local/bin/bluetooth_setup.sh /usr/local/bin/
$ mv ./sh/usr/local/bin/start.sh /usr/local/bin/
$ sudo reboot
```

再起動後、本プログラムが自動的に実行される。

# Note
本プログラムの動作には、RaspberryPiにwebカメラとOBD2コネクタが接続されている必要がある。

# Author
 
* Team ieB2
* 琉球大学工学部工学科知能情報コース
* e215726@ie.u-ryukyu.ac.jp

# License
ライセンスを明示する
 
"SleepBreakthrough" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).