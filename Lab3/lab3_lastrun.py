#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Wed Aug  3 11:32:42 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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
expName = 'lab3'  # from the Builder filename that created this script
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
    originPath='/Users/kellycotton/Dropbox/Teaching/PSY103L/Lab3/lab3_lastrun.py',
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
import string
import random 

fix_time = .5
stim_size_start = .005
stim_duration = 20 # frames
fix_display = 0

trial_n = 1000
block_count = 1
acc_count = 0
position = (0,0)
i = 0

win.mouseVisible = False

total_accuracy = [0] * 11
all_positions = [0] * 11



# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruct_text = visual.TextStim(win=win, name='instruct_text',
    text="Welcome to the experiment!\n\nDuring this experiment, you will see a letter presented on the screen at different positions. Your job is to identify the letter you saw. The letter will be presented very quickly and might be difficult to see. \n\nDuring the trial, you will first see a cross in the center of the screen. When you are ready to start the trial, press SPACE. Next, a letter will appear on the screen. It will stay on the screen for a very short amount of time. You will then see a question mark. When you see the question mark, press the letter key to indicate which letter you just saw. \n\nIf your response is incorrect, the letter will increase in size. When you correctly respond 3 times in a row, the position of the letter will change.\n\nDuring the trial, keep your eyes focused on the center of the screen where the cross first appears.\n\nLet's try a few practice trials.\n\nPress SPACE to begin the practice.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instruct = keyboard.Keyboard()

# Initialize components for Routine "loop_start"
loop_startClock = core.Clock()

# Initialize components for Routine "get_ready"
get_readyClock = core.Clock()
key_resp_start_2 = keyboard.Keyboard()
fix_cross_2 = visual.TextStim(win=win, name='fix_cross_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press SPACE when ready.',
    font='Open Sans',
    pos=(0, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "presentation"
presentationClock = core.Clock()
fix_cross = visual.TextStim(win=win, name='fix_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
presented_letter = visual.TextStim(win=win, name='presented_letter',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "response_practice"
response_practiceClock = core.Clock()
key_resp_prac = keyboard.Keyboard()
response_q_prac = visual.TextStim(win=win, name='response_q_prac',
    text='?',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text1 = visual.TextStim(win=win, name='feedback_text1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
feedback_text2 = visual.TextStim(win=win, name='feedback_text2',
    text='Press SPACE to continue.',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_feedback = keyboard.Keyboard()

# Initialize components for Routine "end_practice"
end_practiceClock = core.Clock()
end_practice_text = visual.TextStim(win=win, name='end_practice_text',
    text="You have finished the practice!\n\nNow it's time to begin the real experimental trials. These will be exactly the same as what you just practiced, but you will no longer receive feedback. \n\nYou will see a screen encouraging you to take a break at several times during the experiment. When you have completed all trials, you will see your results. Record these results and report them to your instructor.\n\nIf you have any questions, please ask your instructor now. \n\nPress SPACE when you are ready to begin.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_end_prac = keyboard.Keyboard()

# Initialize components for Routine "loop_start"
loop_startClock = core.Clock()

# Initialize components for Routine "get_ready"
get_readyClock = core.Clock()
key_resp_start_2 = keyboard.Keyboard()
fix_cross_2 = visual.TextStim(win=win, name='fix_cross_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press SPACE when ready.',
    font='Open Sans',
    pos=(0, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "presentation"
presentationClock = core.Clock()
fix_cross = visual.TextStim(win=win, name='fix_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
presented_letter = visual.TextStim(win=win, name='presented_letter',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "response"
responseClock = core.Clock()
response_q = visual.TextStim(win=win, name='response_q',
    text='?',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "end_block"
end_blockClock = core.Clock()
block_message1 = visual.TextStim(win=win, name='block_message1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block_message2 = visual.TextStim(win=win, name='block_message2',
    text='Please take a short break.\n\nPress SPACE when you are ready to continue.',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_block_cont = keyboard.Keyboard()

# Initialize components for Routine "final"
finalClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Results:',
    font='Open Sans',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
end_text1 = visual.TextStim(win=win, name='end_text1',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
end_text2 = visual.TextStim(win=win, name='end_text2',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
end_text3 = visual.TextStim(win=win, name='end_text3',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
end_text4 = visual.TextStim(win=win, name='end_text4',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
end_text5 = visual.TextStim(win=win, name='end_text5',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
end_text6 = visual.TextStim(win=win, name='end_text6',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
end_text7 = visual.TextStim(win=win, name='end_text7',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
end_text8 = visual.TextStim(win=win, name='end_text8',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
end_text9 = visual.TextStim(win=win, name='end_text9',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
end_text10 = visual.TextStim(win=win, name='end_text10',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
end_text11 = visual.TextStim(win=win, name='end_text11',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
end_text12 = visual.TextStim(win=win, name='end_text12',
    text='Record this result.\n\nPress SPACE when you are ready to end the experiment.',
    font='Open Sans',
    pos=(0, -.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
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
    if key_resp_instruct.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
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
# check responses
if key_resp_instruct.keys in ['', [], None]:  # No response was made
    key_resp_instruct.keys = None
thisExp.addData('key_resp_instruct.keys',key_resp_instruct.keys)
if key_resp_instruct.keys != None:  # we had a response
    thisExp.addData('key_resp_instruct.rt', key_resp_instruct.rt)
thisExp.addData('key_resp_instruct.started', key_resp_instruct.tStartRefresh)
thisExp.addData('key_resp_instruct.stopped', key_resp_instruct.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('coord_cond_practice.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "loop_start"-------
    continueRoutine = True
    # update component parameters for each repeat
    acc_count = 0
    stim_size = stim_size_start
    # keep track of which components have finished
    loop_startComponents = []
    for thisComponent in loop_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    loop_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "loop_start"-------
    while continueRoutine:
        # get current time
        t = loop_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=loop_startClock)
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
        for thisComponent in loop_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loop_start"-------
    for thisComponent in loop_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "loop_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=trial_n, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "get_ready"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_start_2.keys = []
        key_resp_start_2.rt = []
        _key_resp_start_2_allKeys = []
        # keep track of which components have finished
        get_readyComponents = [key_resp_start_2, fix_cross_2, text_2]
        for thisComponent in get_readyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        get_readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "get_ready"-------
        while continueRoutine:
            # get current time
            t = get_readyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=get_readyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_start_2* updates
            waitOnFlip = False
            if key_resp_start_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_start_2.frameNStart = frameN  # exact frame index
                key_resp_start_2.tStart = t  # local t and not account for scr refresh
                key_resp_start_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_start_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_start_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_start_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_start_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_start_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_start_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_start_2_allKeys.extend(theseKeys)
                if len(_key_resp_start_2_allKeys):
                    key_resp_start_2.keys = _key_resp_start_2_allKeys[-1].name  # just the last key pressed
                    key_resp_start_2.rt = _key_resp_start_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *fix_cross_2* updates
            if fix_cross_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross_2.frameNStart = frameN  # exact frame index
                fix_cross_2.tStart = t  # local t and not account for scr refresh
                fix_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross_2, 'tStartRefresh')  # time at next scr refresh
                fix_cross_2.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in get_readyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "get_ready"-------
        for thisComponent in get_readyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_3.addData('text_2.started', text_2.tStartRefresh)
        trials_3.addData('text_2.stopped', text_2.tStopRefresh)
        # the Routine "get_ready" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "presentation"-------
        continueRoutine = True
        # update component parameters for each repeat
        stim_letter = random.choice(string.ascii_uppercase)
        
        position = (x_val, 0)
        
        if x_val == 0:
            fix_display = 0
        else:
            fix_display = 1
        fix_cross.setOpacity(fix_display)
        presented_letter.setPos(position)
        presented_letter.setText(stim_letter)
        presented_letter.setHeight(stim_size)
        # keep track of which components have finished
        presentationComponents = [fix_cross, presented_letter]
        for thisComponent in presentationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        presentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "presentation"-------
        while continueRoutine:
            # get current time
            t = presentationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=presentationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_cross* updates
            if fix_cross.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
                # keep track of start time/frame for later
                fix_cross.frameNStart = frameN  # exact frame index
                fix_cross.tStart = t  # local t and not account for scr refresh
                fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(True)
            if fix_cross.status == STARTED:
                if frameN >= (fix_cross.frameNStart + 20):
                    # keep track of stop time/frame for later
                    fix_cross.tStop = t  # not accounting for scr refresh
                    fix_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                    fix_cross.setAutoDraw(False)
            
            # *presented_letter* updates
            if presented_letter.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
                # keep track of start time/frame for later
                presented_letter.frameNStart = frameN  # exact frame index
                presented_letter.tStart = t  # local t and not account for scr refresh
                presented_letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presented_letter, 'tStartRefresh')  # time at next scr refresh
                presented_letter.setAutoDraw(True)
            if presented_letter.status == STARTED:
                if frameN >= (presented_letter.frameNStart + stim_duration):
                    # keep track of stop time/frame for later
                    presented_letter.tStop = t  # not accounting for scr refresh
                    presented_letter.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(presented_letter, 'tStopRefresh')  # time at next scr refresh
                    presented_letter.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in presentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "presentation"-------
        for thisComponent in presentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "presentation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "response_practice"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_prac.keys = []
        key_resp_prac.rt = []
        _key_resp_prac_allKeys = []
        # keep track of which components have finished
        response_practiceComponents = [key_resp_prac, response_q_prac]
        for thisComponent in response_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        response_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "response_practice"-------
        while continueRoutine:
            # get current time
            t = response_practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=response_practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_prac* updates
            waitOnFlip = False
            if key_resp_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_prac.frameNStart = frameN  # exact frame index
                key_resp_prac.tStart = t  # local t and not account for scr refresh
                key_resp_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_prac, 'tStartRefresh')  # time at next scr refresh
                key_resp_prac.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_prac.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_prac.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_prac.getKeys(keyList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], waitRelease=False)
                _key_resp_prac_allKeys.extend(theseKeys)
                if len(_key_resp_prac_allKeys):
                    key_resp_prac.keys = _key_resp_prac_allKeys[-1].name  # just the last key pressed
                    key_resp_prac.rt = _key_resp_prac_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_prac.keys == str(stim_letter.lower())) or (key_resp_prac.keys == stim_letter.lower()):
                        key_resp_prac.corr = 1
                    else:
                        key_resp_prac.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *response_q_prac* updates
            if response_q_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_q_prac.frameNStart = frameN  # exact frame index
                response_q_prac.tStart = t  # local t and not account for scr refresh
                response_q_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_q_prac, 'tStartRefresh')  # time at next scr refresh
                response_q_prac.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response_practice"-------
        for thisComponent in response_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        if key_resp_prac.corr == 1:
            acc_count += 1
        else:
            stim_size += .005
            acc_count = 0
            
        if acc_count == 3:
            trials_3.finished = True
        # check responses
        if key_resp_prac.keys in ['', [], None]:  # No response was made
            key_resp_prac.keys = None
            # was no response the correct answer?!
            if str(stim_letter.lower()).lower() == 'none':
               key_resp_prac.corr = 1;  # correct non-response
            else:
               key_resp_prac.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_3 (TrialHandler)
        trials_3.addData('key_resp_prac.keys',key_resp_prac.keys)
        trials_3.addData('key_resp_prac.corr', key_resp_prac.corr)
        if key_resp_prac.keys != None:  # we had a response
            trials_3.addData('key_resp_prac.rt', key_resp_prac.rt)
        trials_3.addData('response_q_prac.started', response_q_prac.tStartRefresh)
        trials_3.addData('response_q_prac.stopped', response_q_prac.tStopRefresh)
        # the Routine "response_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        if key_resp_prac.corr == 1:
            feedback_msg = "That was correct!"
        else:
            feedback_msg = "That was incorrect. The correct answer was " + stim_letter + "."
        feedback_text1.setText(feedback_msg)
        key_resp_feedback.keys = []
        key_resp_feedback.rt = []
        _key_resp_feedback_allKeys = []
        # keep track of which components have finished
        feedbackComponents = [feedback_text1, feedback_text2, key_resp_feedback]
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
            
            # *feedback_text1* updates
            if feedback_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text1.frameNStart = frameN  # exact frame index
                feedback_text1.tStart = t  # local t and not account for scr refresh
                feedback_text1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text1, 'tStartRefresh')  # time at next scr refresh
                feedback_text1.setAutoDraw(True)
            
            # *feedback_text2* updates
            if feedback_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text2.frameNStart = frameN  # exact frame index
                feedback_text2.tStart = t  # local t and not account for scr refresh
                feedback_text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text2, 'tStartRefresh')  # time at next scr refresh
                feedback_text2.setAutoDraw(True)
            
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
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed trial_n repeats of 'trials_3'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'


# ------Prepare to start Routine "end_practice"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_end_prac.keys = []
key_resp_end_prac.rt = []
_key_resp_end_prac_allKeys = []
# keep track of which components have finished
end_practiceComponents = [end_practice_text, key_resp_end_prac]
for thisComponent in end_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_practice"-------
while continueRoutine:
    # get current time
    t = end_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_practiceClock)
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
    
    # *key_resp_end_prac* updates
    waitOnFlip = False
    if key_resp_end_prac.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_end_prac.frameNStart = frameN  # exact frame index
        key_resp_end_prac.tStart = t  # local t and not account for scr refresh
        key_resp_end_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_end_prac, 'tStartRefresh')  # time at next scr refresh
        key_resp_end_prac.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_end_prac.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_end_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_end_prac.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_end_prac.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_end_prac_allKeys.extend(theseKeys)
        if len(_key_resp_end_prac_allKeys):
            key_resp_end_prac.keys = _key_resp_end_prac_allKeys[-1].name  # just the last key pressed
            key_resp_end_prac.rt = _key_resp_end_prac_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_practice"-------
for thisComponent in end_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('coord_cond.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "loop_start"-------
    continueRoutine = True
    # update component parameters for each repeat
    acc_count = 0
    stim_size = stim_size_start
    # keep track of which components have finished
    loop_startComponents = []
    for thisComponent in loop_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    loop_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "loop_start"-------
    while continueRoutine:
        # get current time
        t = loop_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=loop_startClock)
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
        for thisComponent in loop_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loop_start"-------
    for thisComponent in loop_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "loop_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=trial_n, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
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
        
        # ------Prepare to start Routine "get_ready"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_start_2.keys = []
        key_resp_start_2.rt = []
        _key_resp_start_2_allKeys = []
        # keep track of which components have finished
        get_readyComponents = [key_resp_start_2, fix_cross_2, text_2]
        for thisComponent in get_readyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        get_readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "get_ready"-------
        while continueRoutine:
            # get current time
            t = get_readyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=get_readyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_start_2* updates
            waitOnFlip = False
            if key_resp_start_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_start_2.frameNStart = frameN  # exact frame index
                key_resp_start_2.tStart = t  # local t and not account for scr refresh
                key_resp_start_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_start_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_start_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_start_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_start_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_start_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_start_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_start_2_allKeys.extend(theseKeys)
                if len(_key_resp_start_2_allKeys):
                    key_resp_start_2.keys = _key_resp_start_2_allKeys[-1].name  # just the last key pressed
                    key_resp_start_2.rt = _key_resp_start_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *fix_cross_2* updates
            if fix_cross_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross_2.frameNStart = frameN  # exact frame index
                fix_cross_2.tStart = t  # local t and not account for scr refresh
                fix_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross_2, 'tStartRefresh')  # time at next scr refresh
                fix_cross_2.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in get_readyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "get_ready"-------
        for thisComponent in get_readyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('text_2.started', text_2.tStartRefresh)
        trials.addData('text_2.stopped', text_2.tStopRefresh)
        # the Routine "get_ready" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "presentation"-------
        continueRoutine = True
        # update component parameters for each repeat
        stim_letter = random.choice(string.ascii_uppercase)
        
        position = (x_val, 0)
        
        if x_val == 0:
            fix_display = 0
        else:
            fix_display = 1
        fix_cross.setOpacity(fix_display)
        presented_letter.setPos(position)
        presented_letter.setText(stim_letter)
        presented_letter.setHeight(stim_size)
        # keep track of which components have finished
        presentationComponents = [fix_cross, presented_letter]
        for thisComponent in presentationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        presentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "presentation"-------
        while continueRoutine:
            # get current time
            t = presentationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=presentationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_cross* updates
            if fix_cross.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
                # keep track of start time/frame for later
                fix_cross.frameNStart = frameN  # exact frame index
                fix_cross.tStart = t  # local t and not account for scr refresh
                fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(True)
            if fix_cross.status == STARTED:
                if frameN >= (fix_cross.frameNStart + 20):
                    # keep track of stop time/frame for later
                    fix_cross.tStop = t  # not accounting for scr refresh
                    fix_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                    fix_cross.setAutoDraw(False)
            
            # *presented_letter* updates
            if presented_letter.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
                # keep track of start time/frame for later
                presented_letter.frameNStart = frameN  # exact frame index
                presented_letter.tStart = t  # local t and not account for scr refresh
                presented_letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presented_letter, 'tStartRefresh')  # time at next scr refresh
                presented_letter.setAutoDraw(True)
            if presented_letter.status == STARTED:
                if frameN >= (presented_letter.frameNStart + stim_duration):
                    # keep track of stop time/frame for later
                    presented_letter.tStop = t  # not accounting for scr refresh
                    presented_letter.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(presented_letter, 'tStopRefresh')  # time at next scr refresh
                    presented_letter.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in presentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "presentation"-------
        for thisComponent in presentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "presentation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "response"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        responseComponents = [response_q, key_resp]
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
            
            # *response_q* updates
            if response_q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_q.frameNStart = frameN  # exact frame index
                response_q.tStart = t  # local t and not account for scr refresh
                response_q.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_q, 'tStartRefresh')  # time at next scr refresh
                response_q.setAutoDraw(True)
            
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
                theseKeys = key_resp.getKeys(keyList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(stim_letter.lower())) or (key_resp.keys == stim_letter.lower()):
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
        
        if key_resp.corr == 1:
            acc_count += 1
        else:
            stim_size += .005
            acc_count = 0
            
        if acc_count == 3:
            trials.finished = True
            total_accuracy[i] = [x_val, round(stim_size, 3)]
            i += 1
        trials.addData('response_q.started', response_q.tStartRefresh)
        trials.addData('response_q.stopped', response_q.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(stim_letter.lower()).lower() == 'none':
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
    block_msg = "You have reached the end of block " + str(block_count) + " of 11." 
    block_message1.setText(block_msg)
    key_resp_block_cont.keys = []
    key_resp_block_cont.rt = []
    _key_resp_block_cont_allKeys = []
    # keep track of which components have finished
    end_blockComponents = [block_message1, block_message2, key_resp_block_cont]
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
        
        # *block_message1* updates
        if block_message1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_message1.frameNStart = frameN  # exact frame index
            block_message1.tStart = t  # local t and not account for scr refresh
            block_message1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_message1, 'tStartRefresh')  # time at next scr refresh
            block_message1.setAutoDraw(True)
        
        # *block_message2* updates
        if block_message2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_message2.frameNStart = frameN  # exact frame index
            block_message2.tStart = t  # local t and not account for scr refresh
            block_message2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_message2, 'tStartRefresh')  # time at next scr refresh
            block_message2.setAutoDraw(True)
        
        # *key_resp_block_cont* updates
        waitOnFlip = False
        if key_resp_block_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_block_cont.frameNStart = frameN  # exact frame index
            key_resp_block_cont.tStart = t  # local t and not account for scr refresh
            key_resp_block_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_block_cont, 'tStartRefresh')  # time at next scr refresh
            key_resp_block_cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_block_cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_block_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_block_cont.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_block_cont.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_block_cont_allKeys.extend(theseKeys)
            if len(_key_resp_block_cont_allKeys):
                key_resp_block_cont.keys = _key_resp_block_cont_allKeys[-1].name  # just the last key pressed
                key_resp_block_cont.rt = _key_resp_block_cont_allKeys[-1].rt
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
    block_count = block_count + 1
    # the Routine "end_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "final"-------
continueRoutine = True
# update component parameters for each repeat
for i in range(11):
    thisExp.addData(f"{total_accuracy[i][0]} position font size", total_accuracy[i][1])
end_text1.setPos((total_accuracy[0][0], 0))
end_text1.setText(total_accuracy[0][1])
end_text1.setHeight(total_accuracy[0][1])
end_text2.setPos((total_accuracy[1][0], 0))
end_text2.setText(total_accuracy[1][1])
end_text2.setHeight(total_accuracy[1][1])
end_text3.setPos((total_accuracy[2][0], 0))
end_text3.setText(total_accuracy[2][1])
end_text3.setHeight(total_accuracy[2][1])
end_text4.setPos((total_accuracy[3][0], 0))
end_text4.setText(total_accuracy[3][1])
end_text4.setHeight(total_accuracy[3][1])
end_text5.setPos((total_accuracy[4][0], 0))
end_text5.setText(total_accuracy[4][1])
end_text5.setHeight(total_accuracy[4][1])
end_text6.setPos((total_accuracy[5][0], 0))
end_text6.setText(total_accuracy[5][1])
end_text6.setHeight(total_accuracy[5][1])
end_text7.setPos((total_accuracy[6][0], 0))
end_text7.setText(total_accuracy[6][1])
end_text7.setHeight(total_accuracy[6][1])
end_text8.setPos((total_accuracy[7][0], 0))
end_text8.setText(total_accuracy[7][1])
end_text8.setHeight(total_accuracy[7][1])
end_text9.setPos((total_accuracy[8][0], 0))
end_text9.setText(total_accuracy[8][1])
end_text9.setHeight(total_accuracy[8][1])
end_text10.setPos((total_accuracy[9][0], 0))
end_text10.setText(total_accuracy[9][1])
end_text10.setHeight(total_accuracy[9][1])
end_text11.setPos((total_accuracy[10][0], 0))
end_text11.setText(total_accuracy[10][1])
end_text11.setHeight(total_accuracy[10][1])
key_resp_end.keys = []
key_resp_end.rt = []
_key_resp_end_allKeys = []
# keep track of which components have finished
finalComponents = [end_text, end_text1, end_text2, end_text3, end_text4, end_text5, end_text6, end_text7, end_text8, end_text9, end_text10, end_text11, end_text12, key_resp_end]
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
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
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
    
    # *end_text5* updates
    if end_text5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text5.frameNStart = frameN  # exact frame index
        end_text5.tStart = t  # local t and not account for scr refresh
        end_text5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text5, 'tStartRefresh')  # time at next scr refresh
        end_text5.setAutoDraw(True)
    
    # *end_text6* updates
    if end_text6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text6.frameNStart = frameN  # exact frame index
        end_text6.tStart = t  # local t and not account for scr refresh
        end_text6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text6, 'tStartRefresh')  # time at next scr refresh
        end_text6.setAutoDraw(True)
    
    # *end_text7* updates
    if end_text7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text7.frameNStart = frameN  # exact frame index
        end_text7.tStart = t  # local t and not account for scr refresh
        end_text7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text7, 'tStartRefresh')  # time at next scr refresh
        end_text7.setAutoDraw(True)
    
    # *end_text8* updates
    if end_text8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text8.frameNStart = frameN  # exact frame index
        end_text8.tStart = t  # local t and not account for scr refresh
        end_text8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text8, 'tStartRefresh')  # time at next scr refresh
        end_text8.setAutoDraw(True)
    
    # *end_text9* updates
    if end_text9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text9.frameNStart = frameN  # exact frame index
        end_text9.tStart = t  # local t and not account for scr refresh
        end_text9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text9, 'tStartRefresh')  # time at next scr refresh
        end_text9.setAutoDraw(True)
    
    # *end_text10* updates
    if end_text10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text10.frameNStart = frameN  # exact frame index
        end_text10.tStart = t  # local t and not account for scr refresh
        end_text10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text10, 'tStartRefresh')  # time at next scr refresh
        end_text10.setAutoDraw(True)
    
    # *end_text11* updates
    if end_text11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text11.frameNStart = frameN  # exact frame index
        end_text11.tStart = t  # local t and not account for scr refresh
        end_text11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text11, 'tStartRefresh')  # time at next scr refresh
        end_text11.setAutoDraw(True)
    
    # *end_text12* updates
    if end_text12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text12.frameNStart = frameN  # exact frame index
        end_text12.tStart = t  # local t and not account for scr refresh
        end_text12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text12, 'tStartRefresh')  # time at next scr refresh
        end_text12.setAutoDraw(True)
    
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
