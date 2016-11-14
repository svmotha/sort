'''
Designed to test if application arranges faster than a song a second.
'''

import time

class TimeKeeper:
    '''
    Keeping track of process time once called upon.
    '''
    # def __init__(self):

    def stopWatch(self):
        start_time = time.time()
        return start_time


class Song_second:
    '''
    Designed to compare time taken to rate of 1 song per second (default
    rate). To change your required rate to any desired rate edit desired
    rate varaible below.
    '''
    # global variables
    desiredRate = 1

    def __init__(self, currentRate):
        self.currentRate = currentRate

    def rateTest(self, currentRate, desiredRate):
        if currentRate >= desiredRate :
            return True
        else:
            return False
