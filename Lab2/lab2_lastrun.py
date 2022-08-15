#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Wed Aug  3 15:12:18 2022
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
expName = 'lab2'  # from the Builder filename that created this script
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
    originPath='/Users/kellycotton/Dropbox/Teaching/PSY103L/Lab2/lab2_lastrun.py',
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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
word_stims = []
i = 0
trial_n = 5
block_n = 6
block_count = 1
acc_sum = 0

positions = [(.25, 0), (-.25, 0)]

fix_time = .5
mask_duration = .2
stim_duration = 2 # frames

total_accuracy_1 = [0]
total_accuracy_4 = [0] * 8

win.mouseVisible = False


# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruct_text = visual.TextStim(win=win, name='instruct_text',
    text="Welcome to the experiment!\n\nDuring this experiment, you will see a word presented in the center of the screen. Your job is to identify the word you saw. The words will be presented very quickly and might be difficult to see. \n\nDuring the trial, you will first see a cross in the center of the screen. This is your warning that the number is about to appear and that you should get ready. Next, you may see a group of symbols before a word appears in the center of the screen. It will stay on the screen for a very short amount of time. You may then see the symbols again. Finally, you will see two words presented on the screen, one of which you just saw. If you believe that you just saw the word on the LEFT side of the screen, press the LEFT arrow key. If you believe that you just saw the word on the RIGHT side of the screen, press the RIGHT arrow key.  The trial will then start over again.\n\nLet's try a few practice trials.\n\nPress SPACE to begin the practice.",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instruct = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_stim = visual.ShapeStim(
    win=win, name='fixation_stim', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "mask_before"
mask_beforeClock = core.Clock()
text_mask_before = visual.TextStim(win=win, name='text_mask_before',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimuli_presentation = visual.TextStim(win=win, name='stimuli_presentation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=0.1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "mask_after"
mask_afterClock = core.Clock()
text_mask_after = visual.TextStim(win=win, name='text_mask_after',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "response_practice"
response_practiceClock = core.Clock()
text_target_prac = visual.TextStim(win=win, name='text_target_prac',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_lure_prac = visual.TextStim(win=win, name='text_lure_prac',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_prac = keyboard.Keyboard()

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
    text="You have finished the practice!\n\nNow it's time to begin the real experimental trials. These will be exactly the same as what you just practiced, but you will no longer receive feedback. \n\nYou will see a screen encouraging you to take a break at several times during the experiment. When you have completed all trials, you will see your accuracy results. Record these results and report them to your instructor.\n\nIf you have any questions, please ask your instructor now. \n\nPress SPACE when you are ready to begin.",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_end_prac = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_stim = visual.ShapeStim(
    win=win, name='fixation_stim', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "mask_before"
mask_beforeClock = core.Clock()
text_mask_before = visual.TextStim(win=win, name='text_mask_before',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimuli_presentation = visual.TextStim(win=win, name='stimuli_presentation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=0.1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "mask_after"
mask_afterClock = core.Clock()
text_mask_after = visual.TextStim(win=win, name='text_mask_after',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "response"
responseClock = core.Clock()
text_target = visual.TextStim(win=win, name='text_target',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_lure = visual.TextStim(win=win, name='text_lure',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
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
end_text_2 = visual.TextStim(win=win, name='end_text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
end_text_3 = visual.TextStim(win=win, name='end_text_3',
    text='Record this result.\n\nPress SPACE when you are ready to end the experiment.',
    font='Open Sans',
    pos=(0, -.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
setup_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('words_text.csv'),
    seed=None, name='setup_loop')
thisExp.addLoop(setup_loop)  # add the loop to the experiment
thisSetup_loop = setup_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSetup_loop.rgb)
if thisSetup_loop != None:
    for paramName in thisSetup_loop:
        exec('{} = thisSetup_loop[paramName]'.format(paramName))

for thisSetup_loop in setup_loop:
    currentLoop = setup_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSetup_loop.rgb)
    if thisSetup_loop != None:
        for paramName in thisSetup_loop:
            exec('{} = thisSetup_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "setup"-------
    continueRoutine = True
    # update component parameters for each repeat
    word_stims.append([word_stim])
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
# completed 1.0 repeats of 'setup_loop'


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
trials_practice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('delay_conds_prac.csv'),
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
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_stim]
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
        
        # *fixation_stim* updates
        if fixation_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_stim.frameNStart = frameN  # exact frame index
            fixation_stim.tStart = t  # local t and not account for scr refresh
            fixation_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_stim, 'tStartRefresh')  # time at next scr refresh
            fixation_stim.setAutoDraw(True)
        if fixation_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_stim.tStartRefresh + fix_time-frameTolerance:
                # keep track of stop time/frame for later
                fixation_stim.tStop = t  # not accounting for scr refresh
                fixation_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_stim, 'tStopRefresh')  # time at next scr refresh
                fixation_stim.setAutoDraw(False)
        
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
    trials_practice.addData('fixation_stim.started', fixation_stim.tStartRefresh)
    trials_practice.addData('fixation_stim.stopped', fixation_stim.tStopRefresh)
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "mask_before"-------
    continueRoutine = True
    # update component parameters for each repeat
    if mask_type == "both":
        mask_display = 1
    else:
        mask_display = 0
        
    text_mask_before.setOpacity(mask_display)
    text_mask_before.setText('#$%&@&$')
    # keep track of which components have finished
    mask_beforeComponents = [text_mask_before]
    for thisComponent in mask_beforeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mask_beforeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mask_before"-------
    while continueRoutine:
        # get current time
        t = mask_beforeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mask_beforeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_mask_before* updates
        if text_mask_before.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_mask_before.frameNStart = frameN  # exact frame index
            text_mask_before.tStart = t  # local t and not account for scr refresh
            text_mask_before.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mask_before, 'tStartRefresh')  # time at next scr refresh
            text_mask_before.setAutoDraw(True)
        if text_mask_before.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_mask_before.tStartRefresh + mask_duration-frameTolerance:
                # keep track of stop time/frame for later
                text_mask_before.tStop = t  # not accounting for scr refresh
                text_mask_before.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_mask_before, 'tStopRefresh')  # time at next scr refresh
                text_mask_before.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mask_beforeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mask_before"-------
    for thisComponent in mask_beforeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_practice.addData('text_mask_before.started', text_mask_before.tStartRefresh)
    trials_practice.addData('text_mask_before.stopped', text_mask_before.tStopRefresh)
    # the Routine "mask_before" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    target_word = word_stims[i]
    lure_word = word_stims[i+1]
    
    stimuli_presentation.setText(target_word[0])
    # keep track of which components have finished
    trialComponents = [stimuli_presentation]
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
        
        # *stimuli_presentation* updates
        if stimuli_presentation.status == NOT_STARTED and frameN >= delay_duration:
            # keep track of start time/frame for later
            stimuli_presentation.frameNStart = frameN  # exact frame index
            stimuli_presentation.tStart = t  # local t and not account for scr refresh
            stimuli_presentation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_presentation, 'tStartRefresh')  # time at next scr refresh
            stimuli_presentation.setAutoDraw(True)
        if stimuli_presentation.status == STARTED:
            if frameN >= (stimuli_presentation.frameNStart + stim_duration):
                # keep track of stop time/frame for later
                stimuli_presentation.tStop = t  # not accounting for scr refresh
                stimuli_presentation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_presentation, 'tStopRefresh')  # time at next scr refresh
                stimuli_presentation.setAutoDraw(False)
        
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
    i = i+2
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "mask_after"-------
    continueRoutine = True
    # update component parameters for each repeat
    if mask_type == "both":
        mask_display = 1
    else:
        mask_display = 0
        
    text_mask_after.setOpacity(mask_display)
    text_mask_after.setText('#$%&@&$')
    # keep track of which components have finished
    mask_afterComponents = [text_mask_after]
    for thisComponent in mask_afterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mask_afterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mask_after"-------
    while continueRoutine:
        # get current time
        t = mask_afterClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mask_afterClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_mask_after* updates
        if text_mask_after.status == NOT_STARTED and frameN >= delay_duration:
            # keep track of start time/frame for later
            text_mask_after.frameNStart = frameN  # exact frame index
            text_mask_after.tStart = t  # local t and not account for scr refresh
            text_mask_after.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mask_after, 'tStartRefresh')  # time at next scr refresh
            text_mask_after.setAutoDraw(True)
        if text_mask_after.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_mask_after.tStartRefresh + mask_duration-frameTolerance:
                # keep track of stop time/frame for later
                text_mask_after.tStop = t  # not accounting for scr refresh
                text_mask_after.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_mask_after, 'tStopRefresh')  # time at next scr refresh
                text_mask_after.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mask_afterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mask_after"-------
    for thisComponent in mask_afterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_practice.addData('text_mask_after.started', text_mask_after.tStartRefresh)
    trials_practice.addData('text_mask_after.stopped', text_mask_after.tStopRefresh)
    # the Routine "mask_after" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    shuffle(positions)
    
    position_target = positions[0]
    position_lure = positions[1]
    
    if position_target[0] > 0:
        corr_ans = "right"
    else:
        corr_ans = "left"
    text_target_prac.setPos(position_target)
    text_target_prac.setText(target_word[0])
    text_lure_prac.setPos(position_lure)
    text_lure_prac.setText(lure_word[0])
    key_resp_prac.keys = []
    key_resp_prac.rt = []
    _key_resp_prac_allKeys = []
    # keep track of which components have finished
    response_practiceComponents = [text_target_prac, text_lure_prac, key_resp_prac]
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
        
        # *text_target_prac* updates
        if text_target_prac.status == NOT_STARTED and frameN >= 42-delay_duration:
            # keep track of start time/frame for later
            text_target_prac.frameNStart = frameN  # exact frame index
            text_target_prac.tStart = t  # local t and not account for scr refresh
            text_target_prac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_target_prac, 'tStartRefresh')  # time at next scr refresh
            text_target_prac.setAutoDraw(True)
        
        # *text_lure_prac* updates
        if text_lure_prac.status == NOT_STARTED and frameN >= 42-delay_duration:
            # keep track of start time/frame for later
            text_lure_prac.frameNStart = frameN  # exact frame index
            text_lure_prac.tStart = t  # local t and not account for scr refresh
            text_lure_prac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lure_prac, 'tStartRefresh')  # time at next scr refresh
            text_lure_prac.setAutoDraw(True)
        
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
            theseKeys = key_resp_prac.getKeys(keyList=['right', 'left'], waitRelease=False)
            _key_resp_prac_allKeys.extend(theseKeys)
            if len(_key_resp_prac_allKeys):
                key_resp_prac.keys = _key_resp_prac_allKeys[-1].name  # just the last key pressed
                key_resp_prac.rt = _key_resp_prac_allKeys[-1].rt
                # was this correct?
                if (key_resp_prac.keys == str(corr_ans)) or (key_resp_prac.keys == corr_ans):
                    key_resp_prac.corr = 1
                else:
                    key_resp_prac.corr = 0
                # a response ends the routine
                continueRoutine = False
        
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
    thisExp.addData("word_presented", target_word)
    
    # check responses
    if key_resp_prac.keys in ['', [], None]:  # No response was made
        key_resp_prac.keys = None
        # was no response the correct answer?!
        if str(corr_ans).lower() == 'none':
           key_resp_prac.corr = 1;  # correct non-response
        else:
           key_resp_prac.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_practice (TrialHandler)
    trials_practice.addData('key_resp_prac.keys',key_resp_prac.keys)
    trials_practice.addData('key_resp_prac.corr', key_resp_prac.corr)
    if key_resp_prac.keys != None:  # we had a response
        trials_practice.addData('key_resp_prac.rt', key_resp_prac.rt)
    # the Routine "response_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    if key_resp_prac.corr == 1:
        feedback_msg = "That was correct!"
    else:
        feedback_msg = "That was incorrect. The correct answer was " + corr_ans.upper() + "."
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
    
# completed 1.0 repeats of 'trials_practice'


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
block = data.TrialHandler(nReps=block_n, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=trial_n, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('delay_conds.csv'),
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
        fixationComponents = [fixation_stim]
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
            
            # *fixation_stim* updates
            if fixation_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_stim.frameNStart = frameN  # exact frame index
                fixation_stim.tStart = t  # local t and not account for scr refresh
                fixation_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_stim, 'tStartRefresh')  # time at next scr refresh
                fixation_stim.setAutoDraw(True)
            if fixation_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_stim.tStartRefresh + fix_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_stim.tStop = t  # not accounting for scr refresh
                    fixation_stim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_stim, 'tStopRefresh')  # time at next scr refresh
                    fixation_stim.setAutoDraw(False)
            
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
        trials.addData('fixation_stim.started', fixation_stim.tStartRefresh)
        trials.addData('fixation_stim.stopped', fixation_stim.tStopRefresh)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "mask_before"-------
        continueRoutine = True
        # update component parameters for each repeat
        if mask_type == "both":
            mask_display = 1
        else:
            mask_display = 0
            
        text_mask_before.setOpacity(mask_display)
        text_mask_before.setText('#$%&@&$')
        # keep track of which components have finished
        mask_beforeComponents = [text_mask_before]
        for thisComponent in mask_beforeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        mask_beforeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "mask_before"-------
        while continueRoutine:
            # get current time
            t = mask_beforeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=mask_beforeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_mask_before* updates
            if text_mask_before.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_mask_before.frameNStart = frameN  # exact frame index
                text_mask_before.tStart = t  # local t and not account for scr refresh
                text_mask_before.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_mask_before, 'tStartRefresh')  # time at next scr refresh
                text_mask_before.setAutoDraw(True)
            if text_mask_before.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_mask_before.tStartRefresh + mask_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_mask_before.tStop = t  # not accounting for scr refresh
                    text_mask_before.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_mask_before, 'tStopRefresh')  # time at next scr refresh
                    text_mask_before.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mask_beforeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mask_before"-------
        for thisComponent in mask_beforeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('text_mask_before.started', text_mask_before.tStartRefresh)
        trials.addData('text_mask_before.stopped', text_mask_before.tStopRefresh)
        # the Routine "mask_before" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        target_word = word_stims[i]
        lure_word = word_stims[i+1]
        
        stimuli_presentation.setText(target_word[0])
        # keep track of which components have finished
        trialComponents = [stimuli_presentation]
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
            
            # *stimuli_presentation* updates
            if stimuli_presentation.status == NOT_STARTED and frameN >= delay_duration:
                # keep track of start time/frame for later
                stimuli_presentation.frameNStart = frameN  # exact frame index
                stimuli_presentation.tStart = t  # local t and not account for scr refresh
                stimuli_presentation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimuli_presentation, 'tStartRefresh')  # time at next scr refresh
                stimuli_presentation.setAutoDraw(True)
            if stimuli_presentation.status == STARTED:
                if frameN >= (stimuli_presentation.frameNStart + stim_duration):
                    # keep track of stop time/frame for later
                    stimuli_presentation.tStop = t  # not accounting for scr refresh
                    stimuli_presentation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimuli_presentation, 'tStopRefresh')  # time at next scr refresh
                    stimuli_presentation.setAutoDraw(False)
            
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
        i = i+2
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "mask_after"-------
        continueRoutine = True
        # update component parameters for each repeat
        if mask_type == "both":
            mask_display = 1
        else:
            mask_display = 0
            
        text_mask_after.setOpacity(mask_display)
        text_mask_after.setText('#$%&@&$')
        # keep track of which components have finished
        mask_afterComponents = [text_mask_after]
        for thisComponent in mask_afterComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        mask_afterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "mask_after"-------
        while continueRoutine:
            # get current time
            t = mask_afterClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=mask_afterClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_mask_after* updates
            if text_mask_after.status == NOT_STARTED and frameN >= delay_duration:
                # keep track of start time/frame for later
                text_mask_after.frameNStart = frameN  # exact frame index
                text_mask_after.tStart = t  # local t and not account for scr refresh
                text_mask_after.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_mask_after, 'tStartRefresh')  # time at next scr refresh
                text_mask_after.setAutoDraw(True)
            if text_mask_after.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_mask_after.tStartRefresh + mask_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_mask_after.tStop = t  # not accounting for scr refresh
                    text_mask_after.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_mask_after, 'tStopRefresh')  # time at next scr refresh
                    text_mask_after.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mask_afterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mask_after"-------
        for thisComponent in mask_afterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('text_mask_after.started', text_mask_after.tStartRefresh)
        trials.addData('text_mask_after.stopped', text_mask_after.tStopRefresh)
        # the Routine "mask_after" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "response"-------
        continueRoutine = True
        # update component parameters for each repeat
        shuffle(positions)
        
        position_target = positions[0]
        position_lure = positions[1]
        
        if position_target[0] > 0:
            corr_ans = "right"
        else:
            corr_ans = "left"
        text_target.setPos(position_target)
        text_target.setText(target_word[0])
        text_lure.setPos(position_lure)
        text_lure.setText(lure_word[0])
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        responseComponents = [text_target, text_lure, key_resp]
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
            
            # *text_target* updates
            if text_target.status == NOT_STARTED and frameN >= 42-delay_duration:
                # keep track of start time/frame for later
                text_target.frameNStart = frameN  # exact frame index
                text_target.tStart = t  # local t and not account for scr refresh
                text_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_target, 'tStartRefresh')  # time at next scr refresh
                text_target.setAutoDraw(True)
            
            # *text_lure* updates
            if text_lure.status == NOT_STARTED and frameN >= 42-delay_duration:
                # keep track of start time/frame for later
                text_lure.frameNStart = frameN  # exact frame index
                text_lure.tStart = t  # local t and not account for scr refresh
                text_lure.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lure, 'tStartRefresh')  # time at next scr refresh
                text_lure.setAutoDraw(True)
            
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
        if mask_type == "none":
            total_accuracy_1[0] += key_resp.corr
        else:
            total_accuracy_4[delay_cond-1] += key_resp.corr
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
    block_msg = "You have reached the end of block " + str(block_count) + " of " + str(block_n) + "." 
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
# completed block_n repeats of 'block'


# ------Prepare to start Routine "final"-------
continueRoutine = True
# update component parameters for each repeat
delays = [0,2,3,5,6,9,12,15]
msg = ''
msg_1 = '\nNo mask\n'
msg_2 = 'Both masks\n'
for i in range(8):
    msg_2 += f"{round((delays[i])*16.67)} ms: {round(total_accuracy_4[i]/(trial_n*block_n), 2)}\n"
    thisExp.addData(f"both mask {round((delays[i])*16.67)}ms accuracy", round(total_accuracy_4[i]/(trial_n*block_n), 2))


msg_1 += f"{round(total_accuracy_1[0]/(trial_n*block_n), 2)}\n"

msg = msg_2 + msg_1
thisExp.addData(f"no mask accuracy", round(acc_sum/8, 2))

end_text_2.setText(msg)
key_resp_end.keys = []
key_resp_end.rt = []
_key_resp_end_allKeys = []
# keep track of which components have finished
finalComponents = [end_text, end_text_2, end_text_3, key_resp_end]
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
    
    # *end_text_2* updates
    if end_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text_2.frameNStart = frameN  # exact frame index
        end_text_2.tStart = t  # local t and not account for scr refresh
        end_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text_2, 'tStartRefresh')  # time at next scr refresh
        end_text_2.setAutoDraw(True)
    
    # *end_text_3* updates
    if end_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text_3.frameNStart = frameN  # exact frame index
        end_text_3.tStart = t  # local t and not account for scr refresh
        end_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text_3, 'tStartRefresh')  # time at next scr refresh
        end_text_3.setAutoDraw(True)
    
    # *key_resp_end* updates
    waitOnFlip = False
    if key_resp_end.status == NOT_STARTED and tThisFlip >= 120-frameTolerance:
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
