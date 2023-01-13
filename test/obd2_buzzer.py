import OBD2.obd2_test_v2 as obd2
import GPIO.passive_buzzer_test as passive_buzzer
import GPIO.active_buzzer_test as active_buzzer
import IFTTT.ifttt_test as ifttt
import time

PASSIVE_PIN = 7
ACTIVE_PIN = 23
KEY = "d-RW0to_f71L1cSRgRT7Y1MXg6ohfzf8N9udnWioJMW"

def main():
    obd2_system = obd2.OBD2()
    passive_buzzer_system = passive_buzzer.PassiveTest(PASSIVE_PIN)
    active_buzzer_system = active_buzzer.ActiveBuzzer(ACTIVE_PIN)
    ifttt_system = ifttt.IftttTest(KEY)
    warningspeed = 60
    dangerspeed = 80
    speeds = []

    while True:
        speed = obd2_system.get_speed()

        if speed > warningspeed:
            ifttt_system.ifttt_webhook("line_event", "スピード超過")
            active_buzzer_system.warning_sound(1)

        if speed > dangerspeed:
            break

        if len(speeds) != 0:
            if speed - speeds[-1] >= 10:
                break

        speeds.append(speed)

    # passive_buzzer_system.coffin()

if __name__ == "__main__":
    main()