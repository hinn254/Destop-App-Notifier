'''
 desktop notifier app runs on your system 
 and it will be used to send you notifications 
 after every specific interval of time
'''

import notify2
import time

# Initialize notify - app name
notify2.init('foo')
# title,message,icon
n = notify2.Notification('Unrivaled deals','Sony XP is now 5000')
# specify the urgency
n.set_urgency(notify2.URGENCY_NORMAL)
# set the timeout
n.set_timeout(10)
# shows the notification
n.show()
time.sleep(2)

# Updates the notification
n.update('Sports','KW Win trophy')
n.show()

# test with a for loop
i = 200
for y in range(10000000):
    if y == i:
        notify2.init('Alarm')
        n = notify2.Notification('Guess What','The value of i is 20!!!')
        n.set_urgency(notify2.URGENCY_CRITICAL)
        n.show()

