'''
|--------------------------------------------------------------------------
|
| Jam arrange: Jam arrange Speed Test
| Author: Victor Motha
| Copyright 2016
| Objective: Test if application arranges faster than a song a second.
| Current stable version: 0.0.4
|
'''

'''
|--------------------------------------------------------------------------
| Importing built-in package(s):
|--------------------------------------------------------------------------
|
| This is where we import the built-in python package - time. Used to 
| measure rates of code runs.
|
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


class Song_second(object):
    '''
    Designed to compare time taken to rate of 1 song per second (default
    rate). To change your required rate to any desired rate edit desired
    rate varaible below.
    '''
    desiredRate = 1  # Global Variables
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    # def __init__(self, currentRate):
    #     self.currentRate = currentRate

    def rateTest(self, currentRate, desiredRate):
        if currentRate >= desiredRate :
            return True
        else:
            return False
