# weekday.py
#this program knows what day it is and outputs happiness or disappointment with the fact
#author Nikolina

import datetime
today = datetime.datetime.today()
if today.weekday() == 5 or today.weekday() == 6:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")