import camera.cameratest as camera
import IFTTT.iftttTest as ifttt

key = "d-RW0to_f71L1cSRgRT7Y1MXg6ohfzf8N9udnWioJMW"
# eventid = "post_tweet"

def main():
    judge = camera.camera_recognition()
    
    if judge:
        # ifttt.ifttt_webhook("post_tweet", "居眠り運転", key)
        ifttt.ifttt_webhook("line_event", "居眠り運転", key)


if __name__ == '__main__':
    main()