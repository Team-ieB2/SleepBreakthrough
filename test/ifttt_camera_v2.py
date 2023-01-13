import time
import camera.camera_test_v2 as camera
import IFTTT.ifttt_test as ifttt
import GPIO.active_buzzer_test as active_buzzer

KEY = "d-RW0to_f71L1cSRgRT7Y1MXg6ohfzf8N9udnWioJMW"
LINE_EVENT = "line_event"
TWITTER_EVENT = "post_tweet"
ACTIVE_PIN = 23

def main():
    camera_system = camera.CameraTest()
    ifttt_system = ifttt.IftttTest(KEY)
    active_buzzer_system = active_buzzer.ActiveBuzzer(ACTIVE_PIN)
    sleep_time_for_eye = 0
    sleep_time_for_head = 0

    while True:
        camera_system.set_time()
        camera_system.launch_camera()
        camera_system.set_faces()
        camera_system.set_eyes()
        camera_system.surround_face()
        camera_system.surround_eyes()

        if camera_system.is_eye_close():
            print("Eyes are colsing")
            sleep_time_for_eye += camera_system.count_close_eye_time() - camera_system.get_time()
        else:
            print("Eyes are open")
            sleep_time_for_eye = camera_system.reset_count_close_eye_time()

        # if sleep_time - camera_system.get_time() >= 10:
        if sleep_time_for_eye >= 10:
            print("You are sleeping for eye close!")
            camera_system.set_sleep_frag()
            break

        if camera_system.is_head_down():
            print("Head is down")
            sleep_time_for_head += camera_system.count_head_down_time() - camera_system.get_time()
        else:
            print("Head is up")
            sleep_time_for_head = camera_system.reset_count_head_down_time()

        if sleep_time_for_head >= 10:
            print("You are sleeping for head down!")
            camera_system.set_sleep_frag()
            break


    if camera_system.get_sleep_frag():
        camera_system.camera_release()
        ifttt_system.ifttt_webhook(LINE_EVENT, "居眠り運転")
        ifttt_system.ifttt_webhook(TWITTER_EVENT, "居眠り運転")
        active_buzzer_system.warning_sound(1)

if __name__ == '__main__':
    main()