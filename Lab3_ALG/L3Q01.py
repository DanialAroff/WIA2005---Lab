import time

seconds = 52
minutes = 59
hours = 0

from turtle import *
t1 = Turtle()

while True:
    t1.clear()
    t1.write(str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2),
             font=('open sans', 30, 'normal'))
    seconds = seconds + 1
    time.sleep(1)
    if seconds > 59:
        seconds = 0
        minutes = minutes + 1
    if minutes > 59:
        minutes = 0
        hours = hours + 1
