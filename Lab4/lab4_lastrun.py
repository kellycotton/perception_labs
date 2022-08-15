#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Mon Aug 15 10:23:15 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.1.4')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'lab4'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/kellycotton/Dropbox/Teaching/PSY103L/Lab4/lab4_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "setup"
setupClock = core.Clock()
import colorsys
import math
import re

circle_size = (0.2, 0.2)
dot_size = (0.05, 0.05)
dot_pos_resp = [0,0]
fix_time = .5
block_n = 1
trial_n = 1
block_total = 2
trial_total = 1
i = 0

def scalar_to_rgb(scalar):
    color_list = colorsys.hsv_to_rgb(scalar, 1, 1)
    color_list = [element for element in color_list]
    return color_list

win.mouseVisible = False

error_rgb = [0]*6
error_hsv = [0]*6

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruct_text = visual.TextStim(win=win, name='instruct_text',
    text="Welcome to the experiment!\n\nDuring this experiment, you will see two circles on the screen. The left circle will colored while the right circle will initially be gray. When you move your mouse, the gray circle will begin to change color. Your job is to adjust the color of the right circle until it matches the color of the left circle. When the two circles match, click the mouse button to submit your response and begin the next trial.\n\nLet's try a few practice trials.\n\nPress SPACE to begin the practice.",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "trial_rgb_practice"
trial_rgb_practiceClock = core.Clock()
mouse_resp_perc_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_resp_perc_3.mouseClock = core.Clock()
circle_target_3 = visual.ShapeStim(
    win=win, name='circle_target_3',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(-.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
dot_resp1_9 = visual.Polygon(
    win=win, name='dot_resp1_9',
    edges=75, size=[1.0, 1.0],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-3.0, interpolate=True)
circle_response_3 = visual.ShapeStim(
    win=win, name='circle_response_3',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
circle_response_gray_3 = visual.ShapeStim(
    win=win, name='circle_response_gray_3',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
circle_resp_9 = visual.Polygon(
    win=win, name='circle_resp_9',
    edges=75, size=[1.0, 1.0],
    ori=0.0, pos=[.25,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=None,
    opacity=None, depth=-6.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
circle_target_4 = visual.ShapeStim(
    win=win, name='circle_target_4',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(-.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
circle_response_4 = visual.ShapeStim(
    win=win, name='circle_response_4',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='Original color:',
    font='Open Sans',
    pos=(-.25, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Your response:',
    font='Open Sans',
    pos=(.25, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press SPACE to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, -.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "practice_end"
practice_endClock = core.Clock()
end_practice_text = visual.TextStim(win=win, name='end_practice_text',
    text="You have finished the practice!\n\nNow it's time to begin the real experimental trials. These will be exactly the same as what you just practiced, but you will no longer receive feedback. \n\nYou will see a screen encouraging you to take a break at several times during the experiment. When you have completed all trials, you will see your accuracy results. Record these results and report them to your instructor.\n\nIf you have any questions, please ask your instructor now. \n\nPress SPACE when you are ready to begin.",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "trial_rgb"
trial_rgbClock = core.Clock()
mouse_resp_perc = event.Mouse(win=win)
x, y = [None, None]
mouse_resp_perc.mouseClock = core.Clock()
circle_target = visual.ShapeStim(
    win=win, name='circle_target',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(-.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
dot_resp1_8 = visual.Polygon(
    win=win, name='dot_resp1_8',
    edges=75, size=[1.0, 1.0],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-3.0, interpolate=True)
circle_response = visual.ShapeStim(
    win=win, name='circle_response',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
circle_response_gray = visual.ShapeStim(
    win=win, name='circle_response_gray',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
circle_resp_8 = visual.Polygon(
    win=win, name='circle_resp_8',
    edges=75, size=[1.0, 1.0],
    ori=0.0, pos=[.25,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=None,
    opacity=None, depth=-6.0, interpolate=True)

# Initialize components for Routine "end_block"
end_blockClock = core.Clock()
block_message1_2 = visual.TextStim(win=win, name='block_message1_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block_message2_2 = visual.TextStim(win=win, name='block_message2_2',
    text='Please take a short break.\n\nPress SPACE when you are ready to continue.',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_block_cont_2 = keyboard.Keyboard()

# Initialize components for Routine "trial_hsv"
trial_hsvClock = core.Clock()
mouse_resp_perc_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_resp_perc_2.mouseClock = core.Clock()
circle_target_2 = visual.ShapeStim(
    win=win, name='circle_target_2',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(-.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='hsv',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
dot_resp1 = visual.Polygon(
    win=win, name='dot_resp1',
    edges=75, size=[1.0, 1.0],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-3.0, interpolate=True)
circle_response_2 = visual.ShapeStim(
    win=win, name='circle_response_2',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='hsv',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
circle_response_gray_2 = visual.ShapeStim(
    win=win, name='circle_response_gray_2',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
circle_resp = visual.Polygon(
    win=win, name='circle_resp',
    edges=75, size=[1.0, 1.0],
    ori=0.0, pos=[.25,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=None,
    opacity=None, depth=-6.0, interpolate=True)

# Initialize components for Routine "end_block"
end_blockClock = core.Clock()
block_message1_2 = visual.TextStim(win=win, name='block_message1_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block_message2_2 = visual.TextStim(win=win, name='block_message2_2',
    text='Please take a short break.\n\nPress SPACE when you are ready to continue.',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_block_cont_2 = keyboard.Keyboard()

# Initialize components for Routine "final"
finalClock = core.Clock()
end_text1 = visual.TextStim(win=win, name='end_text1',
    text='Results:',
    font='Open Sans',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
end_text2 = visual.TextStim(win=win, name='end_text2',
    text='',
    font='Open Sans',
    pos=(-.25, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
end_text3 = visual.TextStim(win=win, name='end_text3',
    text='',
    font='Open Sans',
    pos=(.25, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
end_text4 = visual.TextStim(win=win, name='end_text4',
    text='Record this result.\n\nPress SPACE when you are ready to end the experiment.',
    font='Open Sans',
    pos=(0, -.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
instructionsComponents = [instruct_text, key_resp_13]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_text* updates
    if instruct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text.frameNStart = frameN  # exact frame index
        instruct_text.tStart = t  # local t and not account for scr refresh
        instruct_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text, 'tStartRefresh')  # time at next scr refresh
        instruct_text.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_practice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('colors.csv'),
    seed=None, name='trials_practice')
thisExp.addLoop(trials_practice)  # add the loop to the experiment
thisTrials_practice = trials_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
if thisTrials_practice != None:
    for paramName in thisTrials_practice:
        exec('{} = thisTrials_practice[paramName]'.format(paramName))

for thisTrials_practice in trials_practice:
    currentLoop = trials_practice
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
    if thisTrials_practice != None:
        for paramName in thisTrials_practice:
            exec('{} = thisTrials_practice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_rgb_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_resp_perc_3
    gotValidClick = False  # until a click is received
    mouse_resp_perc.getPos()
    mouse_resp_perc.setPos([0.25, 0])
    current_pos = mouse_resp_perc.setPos([0.25, 0])
    
    if color_category == "red":
        angles = list(range(1,21)) + list(range(326, 361))
    elif color_category == "orange":
        angles = list(range(21,51))
    elif color_category == "yellow":
        angles = list(range(51,76))
    elif color_category == "green":
        angles = list(range(76,166))
    elif color_category == "blue":
        angles = list(range(166,261))
    elif color_category == "purple":
        angles = list(range(261,325))
    
    shuffle(angles)
    trial_angles = [angles[0]]
    
    stim_color = scalar_to_rgb(trial_angles[0]/360)
    
    win.mouseVisible = True
    
    circle_target_3.setFillColor(stim_color)
    circle_target_3.setLineColor(stim_color)
    dot_resp1_9.setSize(dot_size)
    circle_resp_9.setSize(circle_size)
    # keep track of which components have finished
    trial_rgb_practiceComponents = [mouse_resp_perc_3, circle_target_3, dot_resp1_9, circle_response_3, circle_response_gray_3, circle_resp_9]
    for thisComponent in trial_rgb_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_rgb_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_rgb_practice"-------
    while continueRoutine:
        # get current time
        t = trial_rgb_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_rgb_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_resp_perc_3* updates
        if mouse_resp_perc_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_resp_perc_3.frameNStart = frameN  # exact frame index
            mouse_resp_perc_3.tStart = t  # local t and not account for scr refresh
            mouse_resp_perc_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_resp_perc_3, 'tStartRefresh')  # time at next scr refresh
            mouse_resp_perc_3.status = STARTED
            mouse_resp_perc_3.mouseClock.reset()
            prevButtonState = mouse_resp_perc_3.getPressed()  # if button is down already this ISN'T a new click
        
        mouse_x = mouse_resp_perc_3.getPos()[0]
        mouse_y = mouse_resp_perc_3.getPos()[1]
        adj_x = 0.25
        adj_y = 0
        
        mouse_x = mouse_x-(adj_x)
        mouse_y = mouse_y-(adj_y)
        r = np.linalg.norm([mouse_x,mouse_y])
        current_pos = [(mouse_x),(mouse_y)]
        
        cterm = [0, (- 50)];
        if (r == 0):
            theta = 0;
        elif (r != 0):
            theta = math.acos(np.dot(current_pos, cterm) / (r * -50))
        if (mouse_x < 0):
            theta = ((2 * pi) - theta)
        
        curr_angle = round(theta*(180/pi))
        
        dot_pos_resp = [(0.25 + ((circle_size[0] / 2) * sin(theta))), 
            (0 + ((circle_size[0] / 2) * cos(theta)))] 
        
        color_rgb = scalar_to_rgb(curr_angle/360)
        
        if (all(current_pos) != all([0.25,0.0])) & (mouse_resp_perc_3.getPressed() != [0, 0, 0]):
            continueRoutine = False
        
        
        # *circle_target_3* updates
        if circle_target_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_target_3.frameNStart = frameN  # exact frame index
            circle_target_3.tStart = t  # local t and not account for scr refresh
            circle_target_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_target_3, 'tStartRefresh')  # time at next scr refresh
            circle_target_3.setAutoDraw(True)
        
        # *dot_resp1_9* updates
        if dot_resp1_9.status == NOT_STARTED and all(current_pos) != all([0.0,0.0]):
            # keep track of start time/frame for later
            dot_resp1_9.frameNStart = frameN  # exact frame index
            dot_resp1_9.tStart = t  # local t and not account for scr refresh
            dot_resp1_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dot_resp1_9, 'tStartRefresh')  # time at next scr refresh
            dot_resp1_9.setAutoDraw(True)
        if dot_resp1_9.status == STARTED:  # only update if drawing
            dot_resp1_9.setPos(dot_pos_resp, log=False)
        
        # *circle_response_3* updates
        if circle_response_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_response_3.frameNStart = frameN  # exact frame index
            circle_response_3.tStart = t  # local t and not account for scr refresh
            circle_response_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_response_3, 'tStartRefresh')  # time at next scr refresh
            circle_response_3.setAutoDraw(True)
        if circle_response_3.status == STARTED:  # only update if drawing
            circle_response_3.setFillColor(color_rgb, log=False)
            circle_response_3.setLineColor(color_rgb, log=False)
        
        # *circle_response_gray_3* updates
        if circle_response_gray_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_response_gray_3.frameNStart = frameN  # exact frame index
            circle_response_gray_3.tStart = t  # local t and not account for scr refresh
            circle_response_gray_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_response_gray_3, 'tStartRefresh')  # time at next scr refresh
            circle_response_gray_3.setAutoDraw(True)
        if circle_response_gray_3.status == STARTED:
            if bool(all(current_pos) != all([0.25,0.0])):
                # keep track of stop time/frame for later
                circle_response_gray_3.tStop = t  # not accounting for scr refresh
                circle_response_gray_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle_response_gray_3, 'tStopRefresh')  # time at next scr refresh
                circle_response_gray_3.setAutoDraw(False)
        if circle_response_gray_3.status == STARTED:  # only update if drawing
            circle_response_gray_3.setFillColor('gray', log=False)
            circle_response_gray_3.setLineColor('gray', log=False)
        
        # *circle_resp_9* updates
        if circle_resp_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            circle_resp_9.frameNStart = frameN  # exact frame index
            circle_resp_9.tStart = t  # local t and not account for scr refresh
            circle_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_resp_9, 'tStartRefresh')  # time at next scr refresh
            circle_resp_9.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_rgb_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_rgb_practice"-------
    for thisComponent in trial_rgb_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_practice (TrialHandler)
    x, y = mouse_resp_perc_3.getPos()
    buttons = mouse_resp_perc_3.getPressed()
    trials_practice.addData('mouse_resp_perc_3.x', x)
    trials_practice.addData('mouse_resp_perc_3.y', y)
    trials_practice.addData('mouse_resp_perc_3.leftButton', buttons[0])
    trials_practice.addData('mouse_resp_perc_3.midButton', buttons[1])
    trials_practice.addData('mouse_resp_perc_3.rightButton', buttons[2])
    err_angle = (trial_angles[0] - curr_angle + 360) % 360
    if (err_angle > 180):
        err_angle = 360 - err_angle
        
    win.mouseVisible = False
    display_warning = 0
    # the Routine "trial_rgb_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    circle_target_4.setFillColor(stim_color)
    circle_target_4.setLineColor(stim_color)
    circle_response_4.setFillColor(color_rgb)
    circle_response_4.setLineColor(color_rgb)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    text_4.setText(f"Error: {err_angle} degree(s)")
    # keep track of which components have finished
    feedbackComponents = [circle_target_4, circle_response_4, text, text_2, text_3, key_resp, text_4]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *circle_target_4* updates
        if circle_target_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_target_4.frameNStart = frameN  # exact frame index
            circle_target_4.tStart = t  # local t and not account for scr refresh
            circle_target_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_target_4, 'tStartRefresh')  # time at next scr refresh
            circle_target_4.setAutoDraw(True)
        
        # *circle_response_4* updates
        if circle_response_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_response_4.frameNStart = frameN  # exact frame index
            circle_response_4.tStart = t  # local t and not account for scr refresh
            circle_response_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_response_4, 'tStartRefresh')  # time at next scr refresh
            circle_response_4.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_practice'


# ------Prepare to start Routine "practice_end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
practice_endComponents = [end_practice_text, key_resp_7]
for thisComponent in practice_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_end"-------
while continueRoutine:
    # get current time
    t = practice_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_practice_text* updates
    if end_practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_text.frameNStart = frameN  # exact frame index
        end_practice_text.tStart = t  # local t and not account for scr refresh
        end_practice_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_text, 'tStartRefresh')  # time at next scr refresh
        end_practice_text.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_end"-------
for thisComponent in practice_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_rgb = data.TrialHandler(nReps=block_total, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block_rgb')
thisExp.addLoop(block_rgb)  # add the loop to the experiment
thisBlock_rgb = block_rgb.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_rgb.rgb)
if thisBlock_rgb != None:
    for paramName in thisBlock_rgb:
        exec('{} = thisBlock_rgb[paramName]'.format(paramName))

for thisBlock_rgb in block_rgb:
    currentLoop = block_rgb
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_rgb.rgb)
    if thisBlock_rgb != None:
        for paramName in thisBlock_rgb:
            exec('{} = thisBlock_rgb[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_rgb = data.TrialHandler(nReps=trial_n, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('colors.csv'),
        seed=None, name='trials_rgb')
    thisExp.addLoop(trials_rgb)  # add the loop to the experiment
    thisTrials_rgb = trials_rgb.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_rgb.rgb)
    if thisTrials_rgb != None:
        for paramName in thisTrials_rgb:
            exec('{} = thisTrials_rgb[paramName]'.format(paramName))
    
    for thisTrials_rgb in trials_rgb:
        currentLoop = trials_rgb
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_rgb.rgb)
        if thisTrials_rgb != None:
            for paramName in thisTrials_rgb:
                exec('{} = thisTrials_rgb[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_rgb"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_resp_perc
        gotValidClick = False  # until a click is received
        mouse_resp_perc.getPos()
        mouse_resp_perc.setPos([0.25, 0])
        current_pos = mouse_resp_perc.setPos([0.25, 0])
        
        if color_category == "red":
            angles = list(range(1,21)) + list(range(326, 361))
        elif color_category == "orange":
            angles = list(range(21,51))
        elif color_category == "yellow":
            angles = list(range(51,76))
        elif color_category == "green":
            angles = list(range(76,166))
        elif color_category == "blue":
            angles = list(range(166,261))
        elif color_category == "purple":
            angles = list(range(261,325))
        
        shuffle(angles)
        trial_angles = [angles[0]]
        
        stim_color = scalar_to_rgb(trial_angles[0]/360)
        
        win.mouseVisible = True
        
        circle_target.setFillColor(stim_color)
        circle_target.setLineColor(stim_color)
        dot_resp1_8.setSize(dot_size)
        circle_resp_8.setSize(circle_size)
        # keep track of which components have finished
        trial_rgbComponents = [mouse_resp_perc, circle_target, dot_resp1_8, circle_response, circle_response_gray, circle_resp_8]
        for thisComponent in trial_rgbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_rgbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_rgb"-------
        while continueRoutine:
            # get current time
            t = trial_rgbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_rgbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse_resp_perc* updates
            if mouse_resp_perc.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_resp_perc.frameNStart = frameN  # exact frame index
                mouse_resp_perc.tStart = t  # local t and not account for scr refresh
                mouse_resp_perc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_resp_perc, 'tStartRefresh')  # time at next scr refresh
                mouse_resp_perc.status = STARTED
                mouse_resp_perc.mouseClock.reset()
                prevButtonState = mouse_resp_perc.getPressed()  # if button is down already this ISN'T a new click
            
            mouse_x = mouse_resp_perc.getPos()[0]
            mouse_y = mouse_resp_perc.getPos()[1]
            adj_x = 0.25
            adj_y = 0
            
            mouse_x = mouse_x-(adj_x)
            mouse_y = mouse_y-(adj_y)
            r = np.linalg.norm([mouse_x,mouse_y])
            current_pos = [(mouse_x),(mouse_y)]
            
            cterm = [0, (- 50)];
            if (r == 0):
                theta = 0;
            elif (r != 0):
                theta = math.acos(np.dot(current_pos, cterm) / (r * -50))
            if (mouse_x < 0):
                theta = ((2 * pi) - theta)
            
            curr_angle = round(theta*(180/pi))
            
            dot_pos_resp = [(0.25 + ((circle_size[0] / 2) * sin(theta))), 
                (0 + ((circle_size[0] / 2) * cos(theta)))] 
            
            color_rgb = scalar_to_rgb(curr_angle/360)
            
            if (all(current_pos) != all([0.25,0.0])) & (mouse_resp_perc.getPressed() != [0, 0, 0]):
                continueRoutine = False
            
            
            # *circle_target* updates
            if circle_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_target.frameNStart = frameN  # exact frame index
                circle_target.tStart = t  # local t and not account for scr refresh
                circle_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_target, 'tStartRefresh')  # time at next scr refresh
                circle_target.setAutoDraw(True)
            
            # *dot_resp1_8* updates
            if dot_resp1_8.status == NOT_STARTED and all(current_pos) != all([0.0,0.0]):
                # keep track of start time/frame for later
                dot_resp1_8.frameNStart = frameN  # exact frame index
                dot_resp1_8.tStart = t  # local t and not account for scr refresh
                dot_resp1_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dot_resp1_8, 'tStartRefresh')  # time at next scr refresh
                dot_resp1_8.setAutoDraw(True)
            if dot_resp1_8.status == STARTED:  # only update if drawing
                dot_resp1_8.setPos(dot_pos_resp, log=False)
            
            # *circle_response* updates
            if circle_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_response.frameNStart = frameN  # exact frame index
                circle_response.tStart = t  # local t and not account for scr refresh
                circle_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_response, 'tStartRefresh')  # time at next scr refresh
                circle_response.setAutoDraw(True)
            if circle_response.status == STARTED:  # only update if drawing
                circle_response.setFillColor(color_rgb, log=False)
                circle_response.setLineColor(color_rgb, log=False)
            
            # *circle_response_gray* updates
            if circle_response_gray.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_response_gray.frameNStart = frameN  # exact frame index
                circle_response_gray.tStart = t  # local t and not account for scr refresh
                circle_response_gray.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_response_gray, 'tStartRefresh')  # time at next scr refresh
                circle_response_gray.setAutoDraw(True)
            if circle_response_gray.status == STARTED:
                if bool(all(current_pos) != all([0.25,0.0])):
                    # keep track of stop time/frame for later
                    circle_response_gray.tStop = t  # not accounting for scr refresh
                    circle_response_gray.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle_response_gray, 'tStopRefresh')  # time at next scr refresh
                    circle_response_gray.setAutoDraw(False)
            if circle_response_gray.status == STARTED:  # only update if drawing
                circle_response_gray.setFillColor('gray', log=False)
                circle_response_gray.setLineColor('gray', log=False)
            
            # *circle_resp_8* updates
            if circle_resp_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                circle_resp_8.frameNStart = frameN  # exact frame index
                circle_resp_8.tStart = t  # local t and not account for scr refresh
                circle_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_resp_8, 'tStartRefresh')  # time at next scr refresh
                circle_resp_8.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_rgbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_rgb"-------
        for thisComponent in trial_rgbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_rgb (TrialHandler)
        x, y = mouse_resp_perc.getPos()
        buttons = mouse_resp_perc.getPressed()
        trials_rgb.addData('mouse_resp_perc.x', x)
        trials_rgb.addData('mouse_resp_perc.y', y)
        trials_rgb.addData('mouse_resp_perc.leftButton', buttons[0])
        trials_rgb.addData('mouse_resp_perc.midButton', buttons[1])
        trials_rgb.addData('mouse_resp_perc.rightButton', buttons[2])
        thisExp.addData('disp_angle', trial_angles[0])
        thisExp.addData('resp_angle', curr_angle)
        thisExp.addData('block_n', block_n)
        thisExp.addData('trial_n', trial_n)
        
        err_angle = (trial_angles[0] - curr_angle + 360) % 360
        if (err_angle > 180):
            err_angle = 360 - err_angle
            
        thisExp.addData('err_angle_rgb', err_angle)
        
        error_rgb[color_condition-1] += err_angle
        i += 1
        
        win.mouseVisible = False
        display_warning = 0
        # the Routine "trial_rgb" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed trial_n repeats of 'trials_rgb'
    
    
    # ------Prepare to start Routine "end_block"-------
    continueRoutine = True
    # update component parameters for each repeat
    block_msg = "You have reached the end of block " + str(block_n) + " of " + str(block_total*2) + "." 
    
    i = 0
    block_message1_2.setText(block_msg)
    key_resp_block_cont_2.keys = []
    key_resp_block_cont_2.rt = []
    _key_resp_block_cont_2_allKeys = []
    # keep track of which components have finished
    end_blockComponents = [block_message1_2, block_message2_2, key_resp_block_cont_2]
    for thisComponent in end_blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_block"-------
    while continueRoutine:
        # get current time
        t = end_blockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_blockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block_message1_2* updates
        if block_message1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_message1_2.frameNStart = frameN  # exact frame index
            block_message1_2.tStart = t  # local t and not account for scr refresh
            block_message1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_message1_2, 'tStartRefresh')  # time at next scr refresh
            block_message1_2.setAutoDraw(True)
        
        # *block_message2_2* updates
        if block_message2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_message2_2.frameNStart = frameN  # exact frame index
            block_message2_2.tStart = t  # local t and not account for scr refresh
            block_message2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_message2_2, 'tStartRefresh')  # time at next scr refresh
            block_message2_2.setAutoDraw(True)
        
        # *key_resp_block_cont_2* updates
        waitOnFlip = False
        if key_resp_block_cont_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_block_cont_2.frameNStart = frameN  # exact frame index
            key_resp_block_cont_2.tStart = t  # local t and not account for scr refresh
            key_resp_block_cont_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_block_cont_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_block_cont_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_block_cont_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_block_cont_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_block_cont_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_block_cont_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_block_cont_2_allKeys.extend(theseKeys)
            if len(_key_resp_block_cont_2_allKeys):
                key_resp_block_cont_2.keys = _key_resp_block_cont_2_allKeys[-1].name  # just the last key pressed
                key_resp_block_cont_2.rt = _key_resp_block_cont_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_block"-------
    for thisComponent in end_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_n += 1
    # the Routine "end_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed block_total repeats of 'block_rgb'


# set up handler to look after randomisation of conditions etc
block_hsv = data.TrialHandler(nReps=block_total, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block_hsv')
thisExp.addLoop(block_hsv)  # add the loop to the experiment
thisBlock_hsv = block_hsv.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_hsv.rgb)
if thisBlock_hsv != None:
    for paramName in thisBlock_hsv:
        exec('{} = thisBlock_hsv[paramName]'.format(paramName))

for thisBlock_hsv in block_hsv:
    currentLoop = block_hsv
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_hsv.rgb)
    if thisBlock_hsv != None:
        for paramName in thisBlock_hsv:
            exec('{} = thisBlock_hsv[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_hsv = data.TrialHandler(nReps=trial_n, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('colors.csv'),
        seed=None, name='trials_hsv')
    thisExp.addLoop(trials_hsv)  # add the loop to the experiment
    thisTrials_hsv = trials_hsv.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_hsv.rgb)
    if thisTrials_hsv != None:
        for paramName in thisTrials_hsv:
            exec('{} = thisTrials_hsv[paramName]'.format(paramName))
    
    for thisTrials_hsv in trials_hsv:
        currentLoop = trials_hsv
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_hsv.rgb)
        if thisTrials_hsv != None:
            for paramName in thisTrials_hsv:
                exec('{} = thisTrials_hsv[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_hsv"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_resp_perc_2
        gotValidClick = False  # until a click is received
        mouse_resp_perc_2.getPos()
        mouse_resp_perc_2.setPos([0.25, 0])
        current_pos = mouse_resp_perc_2.setPos([0.25, 0])
        
        if color_category == "red":
            angles = list(range(1,21)) + list(range(326, 361))
        elif color_category == "orange":
            angles = list(range(21,51))
        elif color_category == "yellow":
            angles = list(range(51,76))
        elif color_category == "green":
            angles = list(range(76,166))
        elif color_category == "blue":
            angles = list(range(166,261))
        elif color_category == "purple":
            angles = list(range(261,325))
            
        shuffle(angles)
        
        trial_angles = [angles[0]]
        err_total = 0
        
        stim_color = (trial_angles[0], 1, 1)
        
        win.mouseVisible = True
        circle_target_2.setFillColor(stim_color)
        circle_target_2.setLineColor(stim_color)
        dot_resp1.setSize(dot_size)
        circle_resp.setSize(circle_size)
        # keep track of which components have finished
        trial_hsvComponents = [mouse_resp_perc_2, circle_target_2, dot_resp1, circle_response_2, circle_response_gray_2, circle_resp]
        for thisComponent in trial_hsvComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_hsvClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_hsv"-------
        while continueRoutine:
            # get current time
            t = trial_hsvClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_hsvClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse_resp_perc_2* updates
            if mouse_resp_perc_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_resp_perc_2.frameNStart = frameN  # exact frame index
                mouse_resp_perc_2.tStart = t  # local t and not account for scr refresh
                mouse_resp_perc_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_resp_perc_2, 'tStartRefresh')  # time at next scr refresh
                mouse_resp_perc_2.status = STARTED
                mouse_resp_perc_2.mouseClock.reset()
                prevButtonState = mouse_resp_perc_2.getPressed()  # if button is down already this ISN'T a new click
            
            mouse_x = mouse_resp_perc_2.getPos()[0]
            mouse_y = mouse_resp_perc_2.getPos()[1]
            adj_x = 0.25
            adj_y = 0
            
            mouse_x = mouse_x-(adj_x)
            mouse_y = mouse_y-(adj_y)
            r = np.linalg.norm([mouse_x,mouse_y])
            current_pos = [(mouse_x),(mouse_y)]
            
            cterm = [0, (- 50)];
            if (r == 0):
                theta = 0;
            elif (r != 0):
                theta = math.acos(np.dot(current_pos, cterm) / (r * -50))
            if (mouse_x < 0):
                theta = ((2 * pi) - theta)
            
            curr_angle = round(theta*(180/pi))
            
            dot_pos_resp = [(0.25 + ((circle_size[0] / 2) * sin(theta))), 
                (0 + ((circle_size[0] / 2) * cos(theta)))] 
            
            color_hsv = (curr_angle, 1, 1)
            
            if (all(current_pos) != all([0.25,0.0])) & (mouse_resp_perc_2.getPressed() != [0, 0, 0]):
                continueRoutine = False
            
            # *circle_target_2* updates
            if circle_target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_target_2.frameNStart = frameN  # exact frame index
                circle_target_2.tStart = t  # local t and not account for scr refresh
                circle_target_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_target_2, 'tStartRefresh')  # time at next scr refresh
                circle_target_2.setAutoDraw(True)
            
            # *dot_resp1* updates
            if dot_resp1.status == NOT_STARTED and all(current_pos) != all([0.0,0.0]):
                # keep track of start time/frame for later
                dot_resp1.frameNStart = frameN  # exact frame index
                dot_resp1.tStart = t  # local t and not account for scr refresh
                dot_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dot_resp1, 'tStartRefresh')  # time at next scr refresh
                dot_resp1.setAutoDraw(True)
            if dot_resp1.status == STARTED:  # only update if drawing
                dot_resp1.setPos(dot_pos_resp, log=False)
            
            # *circle_response_2* updates
            if circle_response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_response_2.frameNStart = frameN  # exact frame index
                circle_response_2.tStart = t  # local t and not account for scr refresh
                circle_response_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_response_2, 'tStartRefresh')  # time at next scr refresh
                circle_response_2.setAutoDraw(True)
            if circle_response_2.status == STARTED:  # only update if drawing
                circle_response_2.setFillColor(color_hsv, log=False)
                circle_response_2.setLineColor(color_hsv, log=False)
            
            # *circle_response_gray_2* updates
            if circle_response_gray_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_response_gray_2.frameNStart = frameN  # exact frame index
                circle_response_gray_2.tStart = t  # local t and not account for scr refresh
                circle_response_gray_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_response_gray_2, 'tStartRefresh')  # time at next scr refresh
                circle_response_gray_2.setAutoDraw(True)
            if circle_response_gray_2.status == STARTED:
                if bool(all(current_pos) != all([0.25,0.0])):
                    # keep track of stop time/frame for later
                    circle_response_gray_2.tStop = t  # not accounting for scr refresh
                    circle_response_gray_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle_response_gray_2, 'tStopRefresh')  # time at next scr refresh
                    circle_response_gray_2.setAutoDraw(False)
            if circle_response_gray_2.status == STARTED:  # only update if drawing
                circle_response_gray_2.setFillColor('gray', log=False)
                circle_response_gray_2.setLineColor('gray', log=False)
            
            # *circle_resp* updates
            if circle_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                circle_resp.frameNStart = frameN  # exact frame index
                circle_resp.tStart = t  # local t and not account for scr refresh
                circle_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_resp, 'tStartRefresh')  # time at next scr refresh
                circle_resp.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_hsvComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_hsv"-------
        for thisComponent in trial_hsvComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_hsv (TrialHandler)
        x, y = mouse_resp_perc_2.getPos()
        buttons = mouse_resp_perc_2.getPressed()
        trials_hsv.addData('mouse_resp_perc_2.x', x)
        trials_hsv.addData('mouse_resp_perc_2.y', y)
        trials_hsv.addData('mouse_resp_perc_2.leftButton', buttons[0])
        trials_hsv.addData('mouse_resp_perc_2.midButton', buttons[1])
        trials_hsv.addData('mouse_resp_perc_2.rightButton', buttons[2])
        thisExp.addData('disp_angle', trial_angles[0])
        thisExp.addData('resp_angle', curr_angle)
        thisExp.addData('block_n', block_n)
        thisExp.addData('trial_n', trial_n)
        
        err_angle = (trial_angles[0] - curr_angle + 360) % 360
        if (err_angle > 180):
            err_angle = 360 - err_angle
            
        thisExp.addData('err_angle_hsv', err_angle)
        
        
        error_hsv[color_condition-1] += err_angle
        i += 1
        
        win.mouseVisible = False
        # the Routine "trial_hsv" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed trial_n repeats of 'trials_hsv'
    
    
    # ------Prepare to start Routine "end_block"-------
    continueRoutine = True
    # update component parameters for each repeat
    block_msg = "You have reached the end of block " + str(block_n) + " of " + str(block_total*2) + "." 
    
    i = 0
    block_message1_2.setText(block_msg)
    key_resp_block_cont_2.keys = []
    key_resp_block_cont_2.rt = []
    _key_resp_block_cont_2_allKeys = []
    # keep track of which components have finished
    end_blockComponents = [block_message1_2, block_message2_2, key_resp_block_cont_2]
    for thisComponent in end_blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_block"-------
    while continueRoutine:
        # get current time
        t = end_blockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_blockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block_message1_2* updates
        if block_message1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_message1_2.frameNStart = frameN  # exact frame index
            block_message1_2.tStart = t  # local t and not account for scr refresh
            block_message1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_message1_2, 'tStartRefresh')  # time at next scr refresh
            block_message1_2.setAutoDraw(True)
        
        # *block_message2_2* updates
        if block_message2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_message2_2.frameNStart = frameN  # exact frame index
            block_message2_2.tStart = t  # local t and not account for scr refresh
            block_message2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_message2_2, 'tStartRefresh')  # time at next scr refresh
            block_message2_2.setAutoDraw(True)
        
        # *key_resp_block_cont_2* updates
        waitOnFlip = False
        if key_resp_block_cont_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_block_cont_2.frameNStart = frameN  # exact frame index
            key_resp_block_cont_2.tStart = t  # local t and not account for scr refresh
            key_resp_block_cont_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_block_cont_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_block_cont_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_block_cont_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_block_cont_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_block_cont_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_block_cont_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_block_cont_2_allKeys.extend(theseKeys)
            if len(_key_resp_block_cont_2_allKeys):
                key_resp_block_cont_2.keys = _key_resp_block_cont_2_allKeys[-1].name  # just the last key pressed
                key_resp_block_cont_2.rt = _key_resp_block_cont_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_block"-------
    for thisComponent in end_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_n += 1
    # the Routine "end_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed block_total repeats of 'block_hsv'


# ------Prepare to start Routine "final"-------
continueRoutine = True
# update component parameters for each repeat
msg_1 = 'Color Space 1 Mean Error:\n\n'
msg_2 = 'Color Space 2 Mean Error:\n\n'

colors = ["RED", "GREEN", "BLUE", "YELLOW", "PURPLE", "ORANGE"]

for i in range(6):
    msg_1 += f"{colors[i]}: {round(error_rgb[i]/(trial_n*block_total), 2)}\n"
    thisExp.addData(f"{colors[i]} error rgb", round(error_rgb[i]/(trial_n*block_total), 2))

for i in range(6):
    msg_2 += f"{colors[i]}: {round(error_hsv[i]/(trial_n*block_total), 2)}\n"
    thisExp.addData(f"{colors[i]} error hsv", round(error_hsv[i]/(trial_n*block_total), 2))

    
    
end_text2.setText(msg_1)
end_text3.setText(msg_2)
key_resp_end.keys = []
key_resp_end.rt = []
_key_resp_end_allKeys = []
# keep track of which components have finished
finalComponents = [end_text1, end_text2, end_text3, end_text4, key_resp_end]
for thisComponent in finalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "final"-------
while continueRoutine:
    # get current time
    t = finalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text1* updates
    if end_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text1.frameNStart = frameN  # exact frame index
        end_text1.tStart = t  # local t and not account for scr refresh
        end_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text1, 'tStartRefresh')  # time at next scr refresh
        end_text1.setAutoDraw(True)
    
    # *end_text2* updates
    if end_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text2.frameNStart = frameN  # exact frame index
        end_text2.tStart = t  # local t and not account for scr refresh
        end_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text2, 'tStartRefresh')  # time at next scr refresh
        end_text2.setAutoDraw(True)
    
    # *end_text3* updates
    if end_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text3.frameNStart = frameN  # exact frame index
        end_text3.tStart = t  # local t and not account for scr refresh
        end_text3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text3, 'tStartRefresh')  # time at next scr refresh
        end_text3.setAutoDraw(True)
    
    # *end_text4* updates
    if end_text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text4.frameNStart = frameN  # exact frame index
        end_text4.tStart = t  # local t and not account for scr refresh
        end_text4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text4, 'tStartRefresh')  # time at next scr refresh
        end_text4.setAutoDraw(True)
    
    # *key_resp_end* updates
    waitOnFlip = False
    if key_resp_end.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
        # keep track of start time/frame for later
        key_resp_end.frameNStart = frameN  # exact frame index
        key_resp_end.tStart = t  # local t and not account for scr refresh
        key_resp_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_end.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_end.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_end_allKeys.extend(theseKeys)
        if len(_key_resp_end_allKeys):
            key_resp_end.keys = _key_resp_end_allKeys[-1].name  # just the last key pressed
            key_resp_end.rt = _key_resp_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final"-------
for thisComponent in finalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "final" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
