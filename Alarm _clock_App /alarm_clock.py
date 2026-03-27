# Python Alarm Clock Application
import time
import datetime
import pygame

# Funtion to set the alarm time
def set_alarm(alarm_time):
    print(f"Alarm set for: {alarm_time}")
    sound_file = "Alarm Clock.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UR ASS UP !!! 😎")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

# Main program
if __name__ == "__main__":
    alarm_time = input("Please enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)