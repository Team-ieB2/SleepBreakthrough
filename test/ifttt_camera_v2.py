import time
import camera.camera_test_v2 as camera

def main():
    camera_system = camera.CameraTest()
    sleep_time = 0

    while True:
        camera_system.set_time()
        end_system_frag = camera_system.launch_camera()
        if end_system_frag:
            break
        camera_system.set_faces()
        camera_system.set_eyes()
        camera_system.surround_face()
        camera_system.surround_eyes()

        if camera_system.is_eye_close():
            print("Eyes are colsing")
            sleep_time += camera_system.count_close_eye_time() - camera_system.get_time()
        else:
            print("Eyes are open")
            sleep_time = camera_system.reset_count_close_eye_time()

        if sleep_time >= 10:
            print("You are sleeping for eye close!")
            camera_system.set_sleep_frag()
            break

        if camera_system.is_head_down():
            print("Head is down")
            camera_system.count_head_down()
            if camera_system.get_head_down_count() >= 20:
                print("You are sleeping for head down!")
                break
    
    camera_system.camera_release()

if __name__ == '__main__':
    main()