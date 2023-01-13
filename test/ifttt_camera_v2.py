import time
import camera.camera_test_v2 as camera


def main():
    camera_system = camera.CameraTest()
    camera_system.set_time()

    while True:
        end_system_frag = camera_system.launch_camera()
        if end_system_frag:
            break
        camera_system.set_faces()
        camera_system.set_eyes()
        camera_system.surround_face()
        camera_system.surround_eyes()

        camera_system.wait_time()

        if camera_system.is_eye_close():
            print("Eyes are colsing")
            sleep_time = time.time()
        else:
            print("Eyes are open")
            camera_system.reset_count_close_eye_time()
            sleep_time = 0

        if sleep_time - camera_system.get_time() >= 20:
            print("You are sleeping for eye close!")
            break

        if camera_system.is_head_down():
            print("Head is down")
            camera_system.count_head_down()
            if camera_system.get_head_down_count() >= 30:
                print("You are sleeping for head down!")
                break


if __name__ == '__main__':
    main()