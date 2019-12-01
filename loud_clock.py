minutes = 50
hours = 7
seconds = 30
import time
while True:
    print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 1
        minutes = minutes + 1
    if minutes == 60:
        hours = hours + 1
        minutes = 1
    if hours == 13:
        hours = 1