#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Mon Aug 15 10:26:42 2022
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
expName = 'lab5'  # from the Builder filename that created this script
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
    originPath='/Users/kellycotton/Dropbox/Teaching/PSY103L/Lab5/lab5_lastrun.py',
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
    monitor='testMonitor', color=[0.0000, 0.0000, 0.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
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
trial_n = 1
block_n = 1
array_present_time = 1 # seconds
fix_time = 0.5

block_total = 3
block_total_multiplier = 2

total_accuracy_parallel = [0] * 6
total_accuracy_serial = [0] * 6

win.mouseVisible = False

red_square_opacity = 0
big_circle_opacity = 0
vertical_bar_opacity = 0
stim_t_opacity = 0



# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruct_text = visual.TextStim(win=win, name='instruct_text',
    text="Welcome to the experiment!\n\nDuring the experiment, you will see some objects on the screen. \n\nPress the RIGHT arrow if the target is present and press the LEFT arrow if the target is absent.\n\nLet's try a few practice trials.\n\nPress SPACE to begin the practice.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instruct = keyboard.Keyboard()

# Initialize components for Routine "target_remind"
target_remindClock = core.Clock()
big_circle_2 = visual.ShapeStim(
    win=win, name='big_circle_2',
    size=(0.075, 0.1), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-1.0, interpolate=True)
vertical_bar_2 = visual.Rect(
    win=win, name='vertical_bar_2',
    width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=1.0, depth=-2.0, interpolate=True)
red_square_2 = visual.Rect(
    win=win, name='red_square_2',
    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-3.0, interpolate=True)
stim_t_2 = visual.TextStim(win=win, name='stim_t_2',
    text='T',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_2 = keyboard.Keyboard()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Press SPACE to begin.',
    font='Open Sans',
    pos=(0, -.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='Target:',
    font='Open Sans',
    pos=(0, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.075, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()


big_circle = visual.ShapeStim(
    win=win, name='big_circle',
    size=(0.075, 0.1), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-3.0, interpolate=True)
vertical_bar = visual.Rect(
    win=win, name='vertical_bar',
    width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=1.0, depth=-4.0, interpolate=True)
red_square = visual.Rect(
    win=win, name='red_square',
    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-5.0, interpolate=True)
stim_t = visual.TextStim(win=win, name='stim_t',
    text='T',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "response"
responseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Target Absent \n>',
    font='Open Sans',
    pos=(.2, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Target Present \n<',
    font='Open Sans',
    pos=(-.2, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_feedback = keyboard.Keyboard()

# Initialize components for Routine "practice_end"
practice_endClock = core.Clock()
end_practice_text = visual.TextStim(win=win, name='end_practice_text',
    text="You have finished the practice!\n\nNow it's time to begin the real experimental trials. These will be exactly the same as what you just practiced, but you will no longer receive feedback. \n\nYou will see a screen encouraging you to take a break at several times during the experiment. When you have completed all trials, you will see your accuracy results. Record these results and report them to your instructor.\n\nIf you have any questions, please ask your instructor now. \n\nPress SPACE when you are ready to begin.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "target_remind"
target_remindClock = core.Clock()
big_circle_2 = visual.ShapeStim(
    win=win, name='big_circle_2',
    size=(0.075, 0.1), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-1.0, interpolate=True)
vertical_bar_2 = visual.Rect(
    win=win, name='vertical_bar_2',
    width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=1.0, depth=-2.0, interpolate=True)
red_square_2 = visual.Rect(
    win=win, name='red_square_2',
    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-3.0, interpolate=True)
stim_t_2 = visual.TextStim(win=win, name='stim_t_2',
    text='T',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_2 = keyboard.Keyboard()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Press SPACE to begin.',
    font='Open Sans',
    pos=(0, -.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='Target:',
    font='Open Sans',
    pos=(0, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.075, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()


big_circle = visual.ShapeStim(
    win=win, name='big_circle',
    size=(0.075, 0.1), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-3.0, interpolate=True)
vertical_bar = visual.Rect(
    win=win, name='vertical_bar',
    width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=1.0, depth=-4.0, interpolate=True)
red_square = visual.Rect(
    win=win, name='red_square',
    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-5.0, interpolate=True)
stim_t = visual.TextStim(win=win, name='stim_t',
    text='T',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "response"
responseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Target Absent \n>',
    font='Open Sans',
    pos=(.2, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Target Present \n<',
    font='Open Sans',
    pos=(-.2, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

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
    pos=(-.25, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
end_text3 = visual.TextStim(win=win, name='end_text3',
    text='',
    font='Open Sans',
    pos=(.25, 0), height=0.04, wrapWidth=None, ori=0.0, 
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
key_resp_instruct.keys = []
key_resp_instruct.rt = []
_key_resp_instruct_allKeys = []
# keep track of which components have finished
instructionsComponents = [instruct_text, key_resp_instruct]
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
    
    # *key_resp_instruct* updates
    waitOnFlip = False
    if key_resp_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instruct.frameNStart = frameN  # exact frame index
        key_resp_instruct.tStart = t  # local t and not account for scr refresh
        key_resp_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instruct, 'tStartRefresh')  # time at next scr refresh
        key_resp_instruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instruct.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instruct.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_instruct_allKeys.extend(theseKeys)
        if len(_key_resp_instruct_allKeys):
            key_resp_instruct.keys = _key_resp_instruct_allKeys[-1].name  # just the last key pressed
            key_resp_instruct.rt = _key_resp_instruct_allKeys[-1].rt
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
blocks_practice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block_conds.csv'),
    seed=None, name='blocks_practice')
thisExp.addLoop(blocks_practice)  # add the loop to the experiment
thisBlocks_practice = blocks_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_practice.rgb)
if thisBlocks_practice != None:
    for paramName in thisBlocks_practice:
        exec('{} = thisBlocks_practice[paramName]'.format(paramName))

for thisBlocks_practice in blocks_practice:
    currentLoop = blocks_practice
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_practice.rgb)
    if thisBlocks_practice != None:
        for paramName in thisBlocks_practice:
            exec('{} = thisBlocks_practice[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_practice = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('set_conds_prac.csv'),
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
        
        # ------Prepare to start Routine "target_remind"-------
        continueRoutine = True
        # update component parameters for each repeat
        if (block_type == "red_square_blue_square"):
            red_square_opacity = 1
        elif (block_type == "red_square_red_circle"):
            red_square_opacity = 1
        elif (block_type == "big_circle_little_circle"):
            big_circle_opacity = 1
        elif (block_type == "red_square_red_circle_blue_square"):
            red_square_opacity = 1
        elif (block_type == "vertical_bar_horizontal_bar"):
            vertical_bar_opacity = 1
        elif (block_type == "t_l"):
            stim_t_opacity = 1
        big_circle_2.setOpacity(big_circle_opacity)
        big_circle_2.setPos((0,0))
        vertical_bar_2.setOpacity(vertical_bar_opacity)
        vertical_bar_2.setPos((0,0))
        red_square_2.setOpacity(red_square_opacity)
        red_square_2.setPos((0,0))
        stim_t_2.setOpacity(stim_t_opacity)
        stim_t_2.setPos((0,0))
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        target_remindComponents = [big_circle_2, vertical_bar_2, red_square_2, stim_t_2, key_resp_2, text_5, text_3]
        for thisComponent in target_remindComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        target_remindClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "target_remind"-------
        while continueRoutine:
            # get current time
            t = target_remindClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=target_remindClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *big_circle_2* updates
            if big_circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                big_circle_2.frameNStart = frameN  # exact frame index
                big_circle_2.tStart = t  # local t and not account for scr refresh
                big_circle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(big_circle_2, 'tStartRefresh')  # time at next scr refresh
                big_circle_2.setAutoDraw(True)
            
            # *vertical_bar_2* updates
            if vertical_bar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vertical_bar_2.frameNStart = frameN  # exact frame index
                vertical_bar_2.tStart = t  # local t and not account for scr refresh
                vertical_bar_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vertical_bar_2, 'tStartRefresh')  # time at next scr refresh
                vertical_bar_2.setAutoDraw(True)
            
            # *red_square_2* updates
            if red_square_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_square_2.frameNStart = frameN  # exact frame index
                red_square_2.tStart = t  # local t and not account for scr refresh
                red_square_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_square_2, 'tStartRefresh')  # time at next scr refresh
                red_square_2.setAutoDraw(True)
            
            # *stim_t_2* updates
            if stim_t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_t_2.frameNStart = frameN  # exact frame index
                stim_t_2.tStart = t  # local t and not account for scr refresh
                stim_t_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_t_2, 'tStartRefresh')  # time at next scr refresh
                stim_t_2.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in target_remindComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "target_remind"-------
        for thisComponent in target_remindComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        red_square_opacity = 0
        blue_square_opacity = 0
        red_circle_opacity = 0
        big_circle_opacity = 0
        little_circle_opacity = 0
        vertical_bar_opacity = 0
        horizontal_bar_opacity = 0
        stim_t_opacity = 0
        stim_l_opacity = 0
        
        # the Routine "target_remind" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fix_cross]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation"-------
        while continueRoutine:
            # get current time
            t = fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_cross* updates
            if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross.frameNStart = frameN  # exact frame index
                fix_cross.tStart = t  # local t and not account for scr refresh
                fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(True)
            if fix_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_cross.tStartRefresh + fix_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_cross.tStop = t  # not accounting for scr refresh
                    fix_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                    fix_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        if target_present == True:
            corr_ans = 'left'
        else:
            corr_ans = 'right'
        
        
        stims = []
        
        if (block_type == "red_square_blue_square") & target_present == True:
            red_square_opacity = 1
            for x in range(set_size-1):
                stim = visual.Rect(
                    win=win, name='blue_square',
                    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                    opacity=1.0, depth=-3.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "red_square_red_circle") & target_present == True:
            red_square_opacity = 1
            for x in range(set_size-1):
                stim = visual.ShapeStim(
                    win=win, name='red_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-4.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "big_circle_little_circle") & target_present == True:
            big_circle_opacity = 1
            for x in range(set_size-1):
                stim = visual.ShapeStim(
                    win=win, name='little_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-5.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "red_square_red_circle_blue_square") & target_present == True:
            red_square_opacity = 1
            for x in range(int((set_size-1) /2)):
                stim = visual.ShapeStim(
                    win=win, name='red_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-4.0, interpolate=True)
                stims.append(stim)
            for x in range(int(set_size/2)):
                stim = visual.Rect(
                    win=win, name='blue_square',
                    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                    opacity=1.0, depth=-3.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "vertical_bar_horizontal_bar") & target_present == True:
            vertical_bar_opacity = 1
            for x in range(int((set_size-1) /2)):
                stim = visual.Rect(
                    win=win, name='horizontal_bar',
                    width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                    ori=90.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                    opacity=1.0, depth=-7.0, interpolate=True)
                stims.append(stim)
            for x in range(int(set_size /2)):
                stim = visual.Rect(
                    win=win, name='red_bar',
                    width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-9.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "t_l") & target_present == True:
            stim_t_opacity = 1
            for x in range(set_size-1):
                stim = visual.TextStim(win=win, name='stim_l',
                    text='L',
                    font='Open Sans',
                    pos=(random()-0.5, random()-0.5), height=0.05, wrapWidth=None, ori=0.0, 
                    color='black', colorSpace='rgb', opacity=1.0, 
                    languageStyle='LTR',
                    depth=-11.0);
                stims.append(stim)
        elif (block_type == "red_square_blue_square") :
            for x in range(set_size):
                stim = visual.Rect(
                    win=win, name='blue_square',
                    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                    opacity=1.0, depth=-3.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "red_square_red_circle") :
            for x in range(set_size):
                stim = visual.ShapeStim(
                    win=win, name='red_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-4.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "big_circle_little_circle") :
            for x in range(set_size):
                stim = visual.ShapeStim(
                    win=win, name='little_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-5.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "red_square_red_circle_blue_square") :
            if set_size == 1:
                for x in range(set_size):
                    stim = visual.ShapeStim(
                            win=win, name='red_circle',
                            size=(0.0375, 0.05), vertices='circle',
                            ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                            lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                            opacity=1.0, depth=-4.0, interpolate=True)
                    stims.append(stim)
            else:
                for x in range(int(set_size/2)):
                    stim = visual.ShapeStim(
                            win=win, name='red_circle',
                            size=(0.0375, 0.05), vertices='circle',
                            ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                            lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                            opacity=1.0, depth=-4.0, interpolate=True)
                    stims.append(stim)
                for x in range(int(set_size/2)):
                    stim = visual.Rect(
                        win=win, name='blue_square',
                        width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
                        ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                        lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                        opacity=1.0, depth=-3.0, interpolate=True)
                    stims.append(stim)
        elif (block_type == "vertical_bar_horizontal_bar") :
            if set_size == 1:
                for x in range(set_size):
                    stim = visual.Rect(
                        win=win, name='horizontal_bar',
                        width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                        ori=90.0, pos=(random()-0.5, random()-0.5), anchor='center',
                        lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                        opacity=1.0, depth=-7.0, interpolate=True)
                    stims.append(stim)
            else:
                for x in range(int(set_size/2)):
                    stim = visual.Rect(
                        win=win, name='horizontal_bar',
                        width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                        ori=90.0, pos=(random()-0.5, random()-0.5), anchor='center',
                        lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                        opacity=1.0, depth=-7.0, interpolate=True)
                    stims.append(stim)
                for x in range(int(set_size/2)):
                    stim = visual.Rect(
                        win=win, name='red_bar',
                        width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                        ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                        opacity=1.0, depth=-9.0, interpolate=True)
                    stims.append(stim)
        elif (block_type == "t_l") :
            for x in range(set_size):
                stim = visual.TextStim(win=win, name='stim_l',
                    text='L',
                    font='Open Sans',
                    pos=(random()-0.5, random()-0.5), height=0.05, wrapWidth=None, ori=0.0, 
                    color='black', colorSpace='rgb', opacity=1.0, 
                    languageStyle='LTR',
                    depth=-11.0);
                stims.append(stim)
        for stim in stims:
            stim.setAutoDraw(True)
        big_circle.setOpacity(big_circle_opacity)
        big_circle.setPos((random()-0.5, random()-0.5))
        vertical_bar.setOpacity(vertical_bar_opacity)
        vertical_bar.setPos((random()-0.5, random()-0.5))
        red_square.setOpacity(red_square_opacity)
        red_square.setPos((random()-0.5, random()-0.5))
        stim_t.setOpacity(stim_t_opacity)
        stim_t.setPos((random()-0.5, random()-0.5))
        # keep track of which components have finished
        trialComponents = [big_circle, vertical_bar, red_square, stim_t]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *big_circle* updates
            if big_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                big_circle.frameNStart = frameN  # exact frame index
                big_circle.tStart = t  # local t and not account for scr refresh
                big_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(big_circle, 'tStartRefresh')  # time at next scr refresh
                big_circle.setAutoDraw(True)
            if big_circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > big_circle.tStartRefresh + array_present_time-frameTolerance:
                    # keep track of stop time/frame for later
                    big_circle.tStop = t  # not accounting for scr refresh
                    big_circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(big_circle, 'tStopRefresh')  # time at next scr refresh
                    big_circle.setAutoDraw(False)
            
            # *vertical_bar* updates
            if vertical_bar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vertical_bar.frameNStart = frameN  # exact frame index
                vertical_bar.tStart = t  # local t and not account for scr refresh
                vertical_bar.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vertical_bar, 'tStartRefresh')  # time at next scr refresh
                vertical_bar.setAutoDraw(True)
            if vertical_bar.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > vertical_bar.tStartRefresh + array_present_time-frameTolerance:
                    # keep track of stop time/frame for later
                    vertical_bar.tStop = t  # not accounting for scr refresh
                    vertical_bar.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(vertical_bar, 'tStopRefresh')  # time at next scr refresh
                    vertical_bar.setAutoDraw(False)
            
            # *red_square* updates
            if red_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_square.frameNStart = frameN  # exact frame index
                red_square.tStart = t  # local t and not account for scr refresh
                red_square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_square, 'tStartRefresh')  # time at next scr refresh
                red_square.setAutoDraw(True)
            if red_square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_square.tStartRefresh + array_present_time-frameTolerance:
                    # keep track of stop time/frame for later
                    red_square.tStop = t  # not accounting for scr refresh
                    red_square.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(red_square, 'tStopRefresh')  # time at next scr refresh
                    red_square.setAutoDraw(False)
            
            # *stim_t* updates
            if stim_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_t.frameNStart = frameN  # exact frame index
                stim_t.tStart = t  # local t and not account for scr refresh
                stim_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_t, 'tStartRefresh')  # time at next scr refresh
                stim_t.setAutoDraw(True)
            if stim_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim_t.tStartRefresh + array_present_time-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_t.tStop = t  # not accounting for scr refresh
                    stim_t.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim_t, 'tStopRefresh')  # time at next scr refresh
                    stim_t.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        red_square_opacity = 0
        big_circle_opacity = 0
        vertical_bar_opacity = 0
        stim_t_opacity = 0
        
        for stim in stims:
            stim.setAutoDraw(False)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "response"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        responseComponents = [text_4, text_2, key_resp]
        for thisComponent in responseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "response"-------
        while continueRoutine:
            # get current time
            t = responseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=responseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
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
                theseKeys = key_resp.getKeys(keyList=['right', 'left'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(corr_ans)) or (key_resp.keys == corr_ans):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response"-------
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        if search_type == "parallel":
            total_accuracy_parallel[set_size_condition] += key_resp.corr
        else:
            total_accuracy_serial[set_size_condition] += key_resp.corr
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corr_ans).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_practice (TrialHandler)
        trials_practice.addData('key_resp.keys',key_resp.keys)
        trials_practice.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials_practice.addData('key_resp.rt', key_resp.rt)
        # the Routine "response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        feedback_msg = ''
        
        if key_resp.corr == 1:
            feedback_msg = "That was correct! \nPress SPACE to continue."
        else:
            feedback_msg = f"That was incorrect. The correct answer was {corr_ans.upper()}. \nPress SPACE to continue."
        text.setText(feedback_msg)
        key_resp_feedback.keys = []
        key_resp_feedback.rt = []
        _key_resp_feedback_allKeys = []
        # keep track of which components have finished
        feedbackComponents = [text, key_resp_feedback]
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
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_feedback* updates
            waitOnFlip = False
            if key_resp_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_feedback.frameNStart = frameN  # exact frame index
                key_resp_feedback.tStart = t  # local t and not account for scr refresh
                key_resp_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_feedback, 'tStartRefresh')  # time at next scr refresh
                key_resp_feedback.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_feedback.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_feedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_feedback.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_feedback.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_feedback_allKeys.extend(theseKeys)
                if len(_key_resp_feedback_allKeys):
                    key_resp_feedback.keys = _key_resp_feedback_allKeys[-1].name  # just the last key pressed
                    key_resp_feedback.rt = _key_resp_feedback_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
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
        total_accuracy_parallel = [0] * 6
        total_accuracy_serial = [0] * 6
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_practice'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks_practice'


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
blocks = data.TrialHandler(nReps=block_total_multiplier, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block_conds.csv'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "target_remind"-------
    continueRoutine = True
    # update component parameters for each repeat
    if (block_type == "red_square_blue_square"):
        red_square_opacity = 1
    elif (block_type == "red_square_red_circle"):
        red_square_opacity = 1
    elif (block_type == "big_circle_little_circle"):
        big_circle_opacity = 1
    elif (block_type == "red_square_red_circle_blue_square"):
        red_square_opacity = 1
    elif (block_type == "vertical_bar_horizontal_bar"):
        vertical_bar_opacity = 1
    elif (block_type == "t_l"):
        stim_t_opacity = 1
    big_circle_2.setOpacity(big_circle_opacity)
    big_circle_2.setPos((0,0))
    vertical_bar_2.setOpacity(vertical_bar_opacity)
    vertical_bar_2.setPos((0,0))
    red_square_2.setOpacity(red_square_opacity)
    red_square_2.setPos((0,0))
    stim_t_2.setOpacity(stim_t_opacity)
    stim_t_2.setPos((0,0))
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    target_remindComponents = [big_circle_2, vertical_bar_2, red_square_2, stim_t_2, key_resp_2, text_5, text_3]
    for thisComponent in target_remindComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    target_remindClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "target_remind"-------
    while continueRoutine:
        # get current time
        t = target_remindClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=target_remindClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *big_circle_2* updates
        if big_circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            big_circle_2.frameNStart = frameN  # exact frame index
            big_circle_2.tStart = t  # local t and not account for scr refresh
            big_circle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(big_circle_2, 'tStartRefresh')  # time at next scr refresh
            big_circle_2.setAutoDraw(True)
        
        # *vertical_bar_2* updates
        if vertical_bar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vertical_bar_2.frameNStart = frameN  # exact frame index
            vertical_bar_2.tStart = t  # local t and not account for scr refresh
            vertical_bar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vertical_bar_2, 'tStartRefresh')  # time at next scr refresh
            vertical_bar_2.setAutoDraw(True)
        
        # *red_square_2* updates
        if red_square_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_square_2.frameNStart = frameN  # exact frame index
            red_square_2.tStart = t  # local t and not account for scr refresh
            red_square_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_square_2, 'tStartRefresh')  # time at next scr refresh
            red_square_2.setAutoDraw(True)
        
        # *stim_t_2* updates
        if stim_t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_t_2.frameNStart = frameN  # exact frame index
            stim_t_2.tStart = t  # local t and not account for scr refresh
            stim_t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_t_2, 'tStartRefresh')  # time at next scr refresh
            stim_t_2.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in target_remindComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "target_remind"-------
    for thisComponent in target_remindComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    red_square_opacity = 0
    blue_square_opacity = 0
    red_circle_opacity = 0
    big_circle_opacity = 0
    little_circle_opacity = 0
    vertical_bar_opacity = 0
    horizontal_bar_opacity = 0
    stim_t_opacity = 0
    stim_l_opacity = 0
    
    # the Routine "target_remind" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=trial_n, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('set_conds.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fix_cross]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation"-------
        while continueRoutine:
            # get current time
            t = fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_cross* updates
            if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross.frameNStart = frameN  # exact frame index
                fix_cross.tStart = t  # local t and not account for scr refresh
                fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(True)
            if fix_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_cross.tStartRefresh + fix_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_cross.tStop = t  # not accounting for scr refresh
                    fix_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                    fix_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        if target_present == True:
            corr_ans = 'left'
        else:
            corr_ans = 'right'
        
        
        stims = []
        
        if (block_type == "red_square_blue_square") & target_present == True:
            red_square_opacity = 1
            for x in range(set_size-1):
                stim = visual.Rect(
                    win=win, name='blue_square',
                    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                    opacity=1.0, depth=-3.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "red_square_red_circle") & target_present == True:
            red_square_opacity = 1
            for x in range(set_size-1):
                stim = visual.ShapeStim(
                    win=win, name='red_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-4.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "big_circle_little_circle") & target_present == True:
            big_circle_opacity = 1
            for x in range(set_size-1):
                stim = visual.ShapeStim(
                    win=win, name='little_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-5.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "red_square_red_circle_blue_square") & target_present == True:
            red_square_opacity = 1
            for x in range(int((set_size-1) /2)):
                stim = visual.ShapeStim(
                    win=win, name='red_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-4.0, interpolate=True)
                stims.append(stim)
            for x in range(int(set_size/2)):
                stim = visual.Rect(
                    win=win, name='blue_square',
                    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                    opacity=1.0, depth=-3.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "vertical_bar_horizontal_bar") & target_present == True:
            vertical_bar_opacity = 1
            for x in range(int((set_size-1) /2)):
                stim = visual.Rect(
                    win=win, name='horizontal_bar',
                    width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                    ori=90.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                    opacity=1.0, depth=-7.0, interpolate=True)
                stims.append(stim)
            for x in range(int(set_size /2)):
                stim = visual.Rect(
                    win=win, name='red_bar',
                    width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-9.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "t_l") & target_present == True:
            stim_t_opacity = 1
            for x in range(set_size-1):
                stim = visual.TextStim(win=win, name='stim_l',
                    text='L',
                    font='Open Sans',
                    pos=(random()-0.5, random()-0.5), height=0.05, wrapWidth=None, ori=0.0, 
                    color='black', colorSpace='rgb', opacity=1.0, 
                    languageStyle='LTR',
                    depth=-11.0);
                stims.append(stim)
        elif (block_type == "red_square_blue_square") :
            for x in range(set_size):
                stim = visual.Rect(
                    win=win, name='blue_square',
                    width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                    opacity=1.0, depth=-3.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "red_square_red_circle") :
            for x in range(set_size):
                stim = visual.ShapeStim(
                    win=win, name='red_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-4.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "big_circle_little_circle") :
            for x in range(set_size):
                stim = visual.ShapeStim(
                    win=win, name='little_circle',
                    size=(0.0375, 0.05), vertices='circle',
                    ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                    opacity=1.0, depth=-5.0, interpolate=True)
                stims.append(stim)
        elif (block_type == "red_square_red_circle_blue_square") :
            if set_size == 1:
                for x in range(set_size):
                    stim = visual.ShapeStim(
                            win=win, name='red_circle',
                            size=(0.0375, 0.05), vertices='circle',
                            ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                            lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                            opacity=1.0, depth=-4.0, interpolate=True)
                    stims.append(stim)
            else:
                for x in range(int(set_size/2)):
                    stim = visual.ShapeStim(
                            win=win, name='red_circle',
                            size=(0.0375, 0.05), vertices='circle',
                            ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                            lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                            opacity=1.0, depth=-4.0, interpolate=True)
                    stims.append(stim)
                for x in range(int(set_size/2)):
                    stim = visual.Rect(
                        win=win, name='blue_square',
                        width=(0.0375, 0.05)[0], height=(0.0375, 0.05)[1],
                        ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                        lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                        opacity=1.0, depth=-3.0, interpolate=True)
                    stims.append(stim)
        elif (block_type == "vertical_bar_horizontal_bar") :
            if set_size == 1:
                for x in range(set_size):
                    stim = visual.Rect(
                        win=win, name='horizontal_bar',
                        width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                        ori=90.0, pos=(random()-0.5, random()-0.5), anchor='center',
                        lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                        opacity=1.0, depth=-7.0, interpolate=True)
                    stims.append(stim)
            else:
                for x in range(int(set_size/2)):
                    stim = visual.Rect(
                        win=win, name='horizontal_bar',
                        width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                        ori=90.0, pos=(random()-0.5, random()-0.5), anchor='center',
                        lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
                        opacity=1.0, depth=-7.0, interpolate=True)
                    stims.append(stim)
                for x in range(int(set_size/2)):
                    stim = visual.Rect(
                        win=win, name='red_bar',
                        width=(0.02, 0.1)[0], height=(0.02, 0.1)[1],
                        ori=0.0, pos=(random()-0.5, random()-0.5), anchor='center',
                        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
                        opacity=1.0, depth=-9.0, interpolate=True)
                    stims.append(stim)
        elif (block_type == "t_l") :
            for x in range(set_size):
                stim = visual.TextStim(win=win, name='stim_l',
                    text='L',
                    font='Open Sans',
                    pos=(random()-0.5, random()-0.5), height=0.05, wrapWidth=None, ori=0.0, 
                    color='black', colorSpace='rgb', opacity=1.0, 
                    languageStyle='LTR',
                    depth=-11.0);
                stims.append(stim)
        for stim in stims:
            stim.setAutoDraw(True)
        big_circle.setOpacity(big_circle_opacity)
        big_circle.setPos((random()-0.5, random()-0.5))
        vertical_bar.setOpacity(vertical_bar_opacity)
        vertical_bar.setPos((random()-0.5, random()-0.5))
        red_square.setOpacity(red_square_opacity)
        red_square.setPos((random()-0.5, random()-0.5))
        stim_t.setOpacity(stim_t_opacity)
        stim_t.setPos((random()-0.5, random()-0.5))
        # keep track of which components have finished
        trialComponents = [big_circle, vertical_bar, red_square, stim_t]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *big_circle* updates
            if big_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                big_circle.frameNStart = frameN  # exact frame index
                big_circle.tStart = t  # local t and not account for scr refresh
                big_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(big_circle, 'tStartRefresh')  # time at next scr refresh
                big_circle.setAutoDraw(True)
            if big_circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > big_circle.tStartRefresh + array_present_time-frameTolerance:
                    # keep track of stop time/frame for later
                    big_circle.tStop = t  # not accounting for scr refresh
                    big_circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(big_circle, 'tStopRefresh')  # time at next scr refresh
                    big_circle.setAutoDraw(False)
            
            # *vertical_bar* updates
            if vertical_bar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vertical_bar.frameNStart = frameN  # exact frame index
                vertical_bar.tStart = t  # local t and not account for scr refresh
                vertical_bar.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vertical_bar, 'tStartRefresh')  # time at next scr refresh
                vertical_bar.setAutoDraw(True)
            if vertical_bar.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > vertical_bar.tStartRefresh + array_present_time-frameTolerance:
                    # keep track of stop time/frame for later
                    vertical_bar.tStop = t  # not accounting for scr refresh
                    vertical_bar.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(vertical_bar, 'tStopRefresh')  # time at next scr refresh
                    vertical_bar.setAutoDraw(False)
            
            # *red_square* updates
            if red_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_square.frameNStart = frameN  # exact frame index
                red_square.tStart = t  # local t and not account for scr refresh
                red_square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_square, 'tStartRefresh')  # time at next scr refresh
                red_square.setAutoDraw(True)
            if red_square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_square.tStartRefresh + array_present_time-frameTolerance:
                    # keep track of stop time/frame for later
                    red_square.tStop = t  # not accounting for scr refresh
                    red_square.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(red_square, 'tStopRefresh')  # time at next scr refresh
                    red_square.setAutoDraw(False)
            
            # *stim_t* updates
            if stim_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_t.frameNStart = frameN  # exact frame index
                stim_t.tStart = t  # local t and not account for scr refresh
                stim_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_t, 'tStartRefresh')  # time at next scr refresh
                stim_t.setAutoDraw(True)
            if stim_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim_t.tStartRefresh + array_present_time-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_t.tStop = t  # not accounting for scr refresh
                    stim_t.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim_t, 'tStopRefresh')  # time at next scr refresh
                    stim_t.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        red_square_opacity = 0
        big_circle_opacity = 0
        vertical_bar_opacity = 0
        stim_t_opacity = 0
        
        for stim in stims:
            stim.setAutoDraw(False)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "response"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        responseComponents = [text_4, text_2, key_resp]
        for thisComponent in responseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "response"-------
        while continueRoutine:
            # get current time
            t = responseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=responseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
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
                theseKeys = key_resp.getKeys(keyList=['right', 'left'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(corr_ans)) or (key_resp.keys == corr_ans):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response"-------
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        if search_type == "parallel":
            total_accuracy_parallel[set_size_condition] += key_resp.corr
        else:
            total_accuracy_serial[set_size_condition] += key_resp.corr
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corr_ans).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp.keys',key_resp.keys)
        trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        # the Routine "response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed trial_n repeats of 'trials'
    
    
    # ------Prepare to start Routine "end_block"-------
    continueRoutine = True
    # update component parameters for each repeat
    block_msg = "You have reached the end of block " + str(block_n) + " of " + str(block_total*2*block_total_multiplier) + "." 
    
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
    
# completed block_total_multiplier repeats of 'blocks'


# ------Prepare to start Routine "final"-------
continueRoutine = True
# update component parameters for each repeat
msg_1 = 'Parallel Search Results:\n\n'
msg_2 = 'Serial Search Results:\n\n'

set_sizes = [1,2,4,8,16,32]

for i in range(6):
    msg_1 += f"{set_sizes[i]}: {round(total_accuracy_parallel[i]/(trial_n*2*block_total*block_total_multiplier), 2)}\n"
    thisExp.addData(f"parallel set size {set_sizes[i]} mean", round(total_accuracy_parallel[i]/(trial_n*2*block_total*block_total_multiplier), 2))

for i in range(6):
    msg_2 += f"{set_sizes[i]}: {round(total_accuracy_serial[i]/(trial_n*2*block_total*block_total_multiplier), 2)}\n"
    thisExp.addData(f"serial set size {set_sizes[i]} mean", round(total_accuracy_serial[i]/(trial_n*2*block_total*block_total_multiplier), 2))

    
    
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
