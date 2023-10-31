# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:00:22 2023

@author: Isabella Lalena
"""

# imports
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from psychopy import locale_setup, gui, visual, core, data, event, logging, clock, constants, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import os 
import sys  
import random as rand
from numpy.random import random, randint, normal, shuffle
import numpy as np
#import fpstimer

# define path
path = os.getcwd()

# define timer
#timer = fpstimer.FPSTimer(120)

# define wait function 
#def wait(x):
#  dur = int(x * 120)
#  for i in range(dur):
#    timer.sleep()
    
# store info about experiment session
expName = u'eeg-localizer' 
expInfo = {'a. session': '01', 'b. participant': '', 'c. run': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = path + '/' + expInfo['b. participant'] + '/' + expInfo['b. participant'] + '_' + expName + '_' + expInfo['c. run'] + '_' + expInfo['date']
# an ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=path + u'/eeg_localizer.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detailed info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# clocks
globalClock = core.Clock()
trialClock = core.Clock()
taskClock = core.Clock()
frameTolerance = 0.001 
# setup the window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=u'grey', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 25.0  # could not measure, so guess
    
# instructions
Instructions = visual.TextStim(win=win, name='Start',
    text=u'In this task you will see two shapes. Each shape will lead to a series of images and may or may not lead to a reward. Using the left and right arrow keys, indicate which shape you wish to choose. \n\n When you are ready, press space to continue.',
    font=u'Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# fixation cross
fixation = visual.TextStim(win=win, name='fixation',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# shape stimuli
shapes = [path + '/task_images/circle.png',
          path + '/task_images/square.png'];

shape_names = ['circle', 'square',];

shape_idx = [0,1];

pathShape1 = visual.ImageStim(
    win=win, image= path + '/task_images/circle.png',
    units='deg', pos=(-10, 0), size = 10, flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

pathShape2 = visual.ImageStim(
    win=win, image= path + '/task_images/square.png',
    units='deg', pos=(10, 0), size = 10, flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

# image stimuli
images = [path + '/task_images/building.png',
                    path + '/task_images/animal.png',
                    path + '/task_images/furniture.png',
                    path + '/task_images/tree.png',
                    path + '/task_images/body_part.png',
                    path + '/task_images/automobile.png',
                    path + '/task_images/handheldobj.png'];

image_names = ['building',
                                'animal',
                                'furniture',
                                'tree',
                                'body part',
                                'automobile',
                                'handheld object',];

image_idx = [0,1,2,3,4,5,6]; 

pathImage1 = visual.ImageStim(
    win=win, image= path + '/task_images/building',
    units='deg', pos=(0, 0), flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

pathImage2 = visual.ImageStim(
    win=win, image= path + '/task_images/animal',
    units='deg', pos=(0, 0), flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

pathImage3 = visual.ImageStim(
    win=win, image= path + '/task_images/furniture',
    units='deg', pos=(0, 0), flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

pathImage4 = visual.ImageStim(
    win=win, image= path + '/task_images/tree',
    units='deg', pos=(0, 0), flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

pathImage5 = visual.ImageStim(
    win=win, image= path + '/task_images/automobile',
    units='deg', pos=(0, 0), flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

pathImage6 = visual.ImageStim(
    win=win, image= path + '/task_images/handheldobj',
    units='deg', pos=(0, 0), flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

# reward stimuli
reward = [path + '/task_images/sweet.png','task_images/savory.jpg', '/task_images/none.png'];

reward_names = ['sweet', 'savory','none'];

reward_idx = [0,1,2];

pathSweet = visual.ImageStim(
    win=win, image= path + '/task_images/sweet.png',
    units='deg', pos=(0, 0), size = 10, flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

pathSavory = visual.ImageStim(
    win=win, image= path + '/task_images/savory.jpg',
    units='deg', pos=(0, 0), size = 10, flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

pathNoReward = visual.ImageStim(
    win=win, image= path + '/task_images/none.png',
    units='deg', pos=(0, 0), size = 10, flipHoriz=False, 
    flipVert=False, name='outcome_low', autoLog=None)

# create timers 
globalClock = core.Clock()  # to track the time since experiment started
nTrials = 1

conditions=[]
for Idx in range (100): # trials
    conditions.append("chair")

trials = data.TrialHandler(nReps=nTrials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=conditions,
    seed=None, name='trials')
    
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialize stimuli with some values
      
# display instructions 
Instructions.draw()
win.flip()
paused = True 
while paused:
    if event.getKeys(keyList=['space']):
        paused = False
        taskClock.reset()
        T=0
        k = 0
    else:
        paused = True

# start trials 
for i in range(trials.nTotal): # number of trials 
    fixation.draw() # display fixation cross and two shapes
    pathShape1.draw()
    pathShape2.draw()
    win.flip()
    currentLoop = trials
    paused = True
    while paused:
        if event.getKeys(keyList=['left']): # if left arrow key pressed 
            paused = False
            for frame in range (120): 
                fixation.draw()
                win.flip()
            for frame in range (120):
                pathImage1.draw()
                win.flip()
            for frame in range (120):
                fixation.draw()
                win.flip() 
            for frame in range (120):
                pathImage2.draw()
                win.flip()
            for frame in range (120):
                fixation.draw()
                win.flip() 
            for frame in range (120):
                pathImage3.draw()
                win.flip()  
            probSweet = rand.randint(0, 1) # random probability of sweet reward 
            for frame in range (120):
                # drifting reward probability for sweet 
                if probSweet == 1: # if reward:
                    pathSweet.draw() # display reward screen
                    win.flip()
                else: # if no reward 
                    pathNoReward.draw() # display no reward screen
                    win.flip()
        elif event.getKeys(keyList=['right']): # if right arrow key pressed
            paused = False 
            for frame in range (120):
                fixation.draw()
                win.flip() 
            for frame in range (120):
                pathImage4.draw()
                win.flip()
            for frame in range (120):
                fixation.draw()
                win.flip()
            for frame in range (120):
                pathImage5.draw()
                win.flip()
            for frame in range (120):
                fixation.draw()
                win.flip() 
            for frame in range (120):
                pathImage6.draw()
                win.flip()
            probSavory = rand.randint(0, 1) # random probability of savory reward 
            for frame in range (120):
                # drifting reward probability for savory 
                if probSavory == 1: # if reward:
                    pathSavory.draw() # display reward screen
                    win.flip()
                else: # if no reward 
                    pathNoReward.draw() # display no reward screen
                    win.flip()
        else:
            paused = True 
        if event.getKeys(keyList=['escape']):
            win.close()
            core.quit()
    
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

# break inbetween trials -- how long? 1 minute? option to skip?

# drifting probability of reward on each trial 

# synch to eeg

# what output? 

# end screen 