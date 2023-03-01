 #import the time module
import time

#input time in seconds
seconds = input("Enter the time in seconds: ")  

#define the timer
def countdown_timer(seconds):

    while seconds>0:
        mins = int(seconds/60)
        secs = int(seconds % 60)

        timer = f'{mins}:{secs}'

        print(timer,end = '\r')
        time.sleep(1)
        seconds -= 1

    print('Time Up!')

# input time in seconds
#seconds = input("Enter the time in number of seconds")

#function call
countdown_timer(int(seconds))

     