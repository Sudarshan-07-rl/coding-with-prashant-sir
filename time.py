#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = int(s[0:2])
    minute = s[3:5]
    second = s[6:8]
    am_pm = s[8:10]
    
    if am_pm == "PM":
        if hour != 12:
            hour += 12
    else:  # AM
        if hour == 12:
            hour = 0
    
    military_hour = str(hour).zfill(2)
    return f"{military_hour}:{minute}:{second}"

    
if __name__ == '__main__':
    s = input().strip()
    result = timeConversion(s)
    print(result)
