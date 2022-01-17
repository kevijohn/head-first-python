# Author: Kevin Johnson
# Created date: JAN 17 2022

from datetime import datetime as dt
import time
import random

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for i in range(5):
    right_this_minute = dt.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd.  ", end='')
    else:
        print("Not an odd minute.  ", end='')
    wait_time = random.randint(1, 60)
    print("Waiting for", wait_time, "seconds")
    time.sleep(wait_time)
