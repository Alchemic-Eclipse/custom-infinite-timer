import os
import time
import datetime
from winotify import Notification, audio
from termcolor import colored

os.system('color')

text = str(input("Please Input a text for your reminder: "))
time_gap = int(input("In minutes, please input the intervals of reminders: "))

def color_str(text, color):
    return colored(text, color)

confirmation = input(f"\n{color_str("Confirmation:", "red")} You want to be reminded to {text} every {time_gap} minute(s).\nPress Enter to continue ")

print(colored(f"\nThe Timer has started.", "green"))


while True: 
    now = datetime.datetime.now()
    later = now + datetime.timedelta(minutes=time_gap)  # Current time + time interval

    print(f"\n{color_str("Current", "yellow")} time: {now.time()}\n{color_str("Next", "yellow")} Reminder at: {later.time()}")

    time.sleep(time_gap*60) # Time takes input in seconds 
    print(f"\n{color_str("REMINDER:", "red")} {text}")
    toast = Notification(
        app_id="Reminder",
        title=f"Reminder to {text}",
        msg=f"Next reminder on {later.time()}",
        duration="short"
    )

    toast.add_actions(label="Okay Okay, Doing..!!")
    toast.show()


