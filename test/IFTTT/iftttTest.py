import requests
import datetime

def ifttt_webhook(eventid, offence, key):
    d = datetime.datetime.today()
    send_date = "{:04d}年{:02d}月{:02d}日".format(d.year, d.month, d.day)
    t = datetime.datetime.now()
    send_time = "{:02d}:{:02d}:{:02d}".format(t.hour, t.minute, t.second)
    
    payload = {"value1": "日付:" + send_date, "value2": "時刻" + send_time, "value3": offence}
    
    url = "https://maker.ifttt.com/trigger/" + eventid + "/with/key/" + key
    
    response = requests.post(url, data=payload)