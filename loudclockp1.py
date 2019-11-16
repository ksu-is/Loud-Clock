minutes = 50
hours = 7
seconds = 30
import time
while True:
    print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
    seconds = seconds + 1
    time.sleep(1)
    
