# -*- coding: utf-8 -*-

import requests
import datetime

class IftttTest:
    """
    IFTTTでメッセージを送ることができるか確かめるクラス
    """
    def __init__(self,key):
        """
        IftttTestクラスのコンストラクタ

        Args:
            key (str): IFTTTのkey
        """
        self.key = key
        
    def get_date(self):
        """
        日付を得る。

        Returns:
            str: date (日付)を年月日で返す。 例:2022年10月09日
        """
        d = datetime.datetime.today()
        date = "{:04d}年{:02d}月{:02d}日".format(d.year, d.month, d.day)
        return date
    
    def get_time(self):
        """
        時刻を得る。

        Returns:
            str: time (現在時刻)を「:」区切りで返す。 例:12:34:05
        """
        t = datetime.datetime.now()
        time = "{:02d}:{:02d}:{:02d}".format(t.hour, t.minute, t.second)
        return time
    
    def ifttt_webhook(self,eventid,offence): 
        """
        IFTTTを用いてメッセージを飛ばす。

        Args:
            eventid (str): 行いたいappletのEvent Name
            offence (str): 送りたい文字列
        """
        send_date = self.get_date()
        send_time = self.get_time()
        payload = {"value1": "日付:" + send_date, "value2": "時刻" + send_time, "value3": offence}
        url = "https://maker.ifttt.com/trigger/" + eventid + "/with/key/" + self.key
        requests.post(url, data=payload)


if __name__ == '__main__':
    key = "bWxY8YDIyu6O_pyDNE61XJ"
    ifttt_test = IftttTest(key)
    try:
        print("IFTTTでのメッセージ送信開始します。")
        ifttt_test.ifttt_webhook("Line","居眠り運転")
    
    except KeyboardInterrupt:
        print("強制終了されました。")
    else:
        print("IFTTTでのメッセージ送信完了しました。\n送信先を確認してください。")
    finally:
        print("IFTTTでのメッセージ送信を終了します。")