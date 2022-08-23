#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Mon Aug 22 20:42:12 2022
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
expName = 'lab8'  # from the Builder filename that created this script
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
    originPath='/Users/kellycotton/Dropbox/Teaching/PSY103L/Lab9/lab9_lastrun.py',
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
import random

tone_time = .3
fix_time = .5

trial_n = 1
block_n = 1
block_count = 1

sound_tones = {1: "C", 
               2: "D",
               3: "E",
               4: "F",
               5: "G",
               6: "A",
               7: "B"}
               
win.mouseVisible = False

total_accuracy_same = 0
total_accuracy_contour = 0
total_accuracy_interval = 0
trial_count_same = 0
trial_count_contour = 0
trial_count_interval = 0

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruct_text = visual.TextStim(win=win, name='instruct_text',
    text="Welcome to the experiment!\n\nDuring this experiment, you will hear two melodies consisting of five tones. Your job is to identify if the melodies are the same or different. Please make sure that you have the sound on your computer turned on.\n\nYou will first start the trial by pressing the spacebar. During the trial, you will first see a cross in the center of the screen. This is your warning that the melodies are about to appear and that you should get ready. Then, you will hear the first melody. There will be a brief delay and you will then hear the second melody. Finally, you will see the response screen. When you see the response screen, press the LEFT arrow if the melodies are the SAME and the RIGHT arrow if the melodies are different. \n\nLet's try a few practice trials.\n\nPress SPACE to begin the practice.",
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
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_1"
trial_1Clock = core.Clock()
sound_0 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_0')
sound_0.setVolume(1.0)
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
sound_3 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)
sound_4 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='Melody 1',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "delay"
delayClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
sound_5 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_5')
sound_5.setVolume(1.0)
sound_6 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_6')
sound_6.setVolume(1.0)
sound_7 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1.0)
sound_8 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1.0)
sound_9 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_9')
sound_9.setVolume(1.0)
text_6 = visual.TextStim(win=win, name='text_6',
    text='Melody 2',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "response"
responseClock = core.Clock()
key_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='>\nDIFFERENT',
    font='Open Sans',
    pos=(.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='<\nSAME',
    font='Open Sans',
    pos=(-.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text1 = visual.TextStim(win=win, name='feedback_text1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feedback_text2 = visual.TextStim(win=win, name='feedback_text2',
    text='Press SPACE to continue.',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
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
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_1"
trial_1Clock = core.Clock()
sound_0 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_0')
sound_0.setVolume(1.0)
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
sound_3 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)
sound_4 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='Melody 1',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "delay"
delayClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
sound_5 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_5')
sound_5.setVolume(1.0)
sound_6 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_6')
sound_6.setVolume(1.0)
sound_7 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1.0)
sound_8 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1.0)
sound_9 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_9')
sound_9.setVolume(1.0)
text_6 = visual.TextStim(win=win, name='text_6',
    text='Melody 2',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "response"
responseClock = core.Clock()
key_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='>\nDIFFERENT',
    font='Open Sans',
    pos=(.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='<\nSAME',
    font='Open Sans',
    pos=(-.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

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
end_text_1 = visual.TextStim(win=win, name='end_text_1',
    text='',
    font='Open Sans',
    pos=(-.3, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
end_text_2 = visual.TextStim(win=win, name='end_text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
end_text_3 = visual.TextStim(win=win, name='end_text_3',
    text='',
    font='Open Sans',
    pos=(0.3, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
end_text_6 = visual.TextStim(win=win, name='end_text_6',
    text='Record this result.\n\nPress SPACE when you are ready to end the experiment.',
    font='Open Sans',
    pos=(0, -.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
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
trials_practice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('tone_conds.csv'),
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
    stim_tone_1 = []
    stim_ints = []
    stim_tone_2 = []
    
    
    for i in range(5):
        stim_int = random.randint(1,7)
        while [stim_int] == stim_ints[-1:]:
            stim_int = random.randint(1,7)
        stim_ints.append(stim_int)
        stim_tone_1.append(sound_tones[stim_int])
                
    stim_tone_2 = stim_tone_1.copy()
    
    tone_change = random.randint(1,4)
    
    if (change == "yes") and (change_condition == "contour"):
        contour_change = random.choice(["1", "-1"])
        new_tone = stim_ints[tone_change] + int(contour_change)
        while (new_tone == 8) or (new_tone == 0):
            tone_change = random.randint(1,4)
            new_tone = stim_ints[tone_change] + int(contour_change)
        stim_tone_2[tone_change] = sound_tones[new_tone]
    elif(change == "yes") and (change_condition == "interval"):
        note_1 = stim_ints[tone_change]
        note_2 = stim_ints[tone_change-1]
        if note_1 > note_2:
            note_3 = stim_ints[tone_change] + 1
        elif note_1 < note_2:
            note_3 = stim_ints[tone_change] - 1
        while (note_3 == 8) or (note_3 == 0):
            tone_change = random.randint(1,4)
            note_1 = stim_ints[tone_change]
            note_2 = stim_ints[tone_change-1]
            if note_1 > note_2:
                note_3 = stim_ints[tone_change] + 1
            elif note_1 < note_2:
                note_3 = stim_ints[tone_change] - 1
        stim_tone_2[tone_change] = sound_tones[note_3]
    
    
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
    
    # ------Prepare to start Routine "trial_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_0.setSound(stim_tone_1[0], secs=tone_time, hamming=True)
    sound_0.setVolume(1.0, log=False)
    sound_1.setSound(stim_tone_1[1], secs=tone_time, hamming=True)
    sound_1.setVolume(1.0, log=False)
    sound_2.setSound(stim_tone_1[2], secs=tone_time, hamming=True)
    sound_2.setVolume(1.0, log=False)
    sound_3.setSound(stim_tone_1[3], secs=tone_time, hamming=True)
    sound_3.setVolume(1.0, log=False)
    sound_4.setSound(stim_tone_1[4], secs=tone_time, hamming=True)
    sound_4.setVolume(1.0, log=False)
    # keep track of which components have finished
    trial_1Components = [sound_0, sound_1, sound_2, sound_3, sound_4, text_8]
    for thisComponent in trial_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_1"-------
    while continueRoutine:
        # get current time
        t = trial_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_0
        if sound_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_0.frameNStart = frameN  # exact frame index
            sound_0.tStart = t  # local t and not account for scr refresh
            sound_0.tStartRefresh = tThisFlipGlobal  # on global time
            sound_0.play(when=win)  # sync with win flip
        if sound_0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_0.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_0.tStop = t  # not accounting for scr refresh
                sound_0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_0, 'tStopRefresh')  # time at next scr refresh
                sound_0.stop()
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and sound_0.status==FINISHED:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and sound_1.status==FINISHED:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play()  # start the sound (it finishes automatically)
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and sound_2.status==FINISHED:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3.play()  # start the sound (it finishes automatically)
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
                sound_3.stop()
        # start/stop sound_4
        if sound_4.status == NOT_STARTED and sound_3.status==FINISHED:
            # keep track of start time/frame for later
            sound_4.frameNStart = frameN  # exact frame index
            sound_4.tStart = t  # local t and not account for scr refresh
            sound_4.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4.play()  # start the sound (it finishes automatically)
        if sound_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_4.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_4.tStop = t  # not accounting for scr refresh
                sound_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_4, 'tStopRefresh')  # time at next scr refresh
                sound_4.stop()
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            if bool(sound_4.status==FINISHED):
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_1"-------
    for thisComponent in trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_0.stop()  # ensure sound has stopped at end of routine
    sound_1.stop()  # ensure sound has stopped at end of routine
    sound_2.stop()  # ensure sound has stopped at end of routine
    sound_3.stop()  # ensure sound has stopped at end of routine
    sound_4.stop()  # ensure sound has stopped at end of routine
    # the Routine "trial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "delay"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    delayComponents = [text_7]
    for thisComponent in delayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    delayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "delay"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = delayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=delayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "delay"-------
    for thisComponent in delayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_practice.addData('text_7.started', text_7.tStartRefresh)
    trials_practice.addData('text_7.stopped', text_7.tStopRefresh)
    
    # ------Prepare to start Routine "trial_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_5.setSound(stim_tone_2[0], secs=tone_time, hamming=True)
    sound_5.setVolume(1.0, log=False)
    sound_6.setSound(stim_tone_2[1], secs=tone_time, hamming=True)
    sound_6.setVolume(1.0, log=False)
    sound_7.setSound(stim_tone_2[2], secs=tone_time, hamming=True)
    sound_7.setVolume(1.0, log=False)
    sound_8.setSound(stim_tone_2[3], secs=tone_time, hamming=True)
    sound_8.setVolume(1.0, log=False)
    sound_9.setSound(stim_tone_2[4], secs=tone_time, hamming=True)
    sound_9.setVolume(1.0, log=False)
    # keep track of which components have finished
    trial_2Components = [sound_5, sound_6, sound_7, sound_8, sound_9, text_6]
    for thisComponent in trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_2"-------
    while continueRoutine:
        # get current time
        t = trial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_5
        if sound_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_5.frameNStart = frameN  # exact frame index
            sound_5.tStart = t  # local t and not account for scr refresh
            sound_5.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5.play(when=win)  # sync with win flip
        if sound_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_5.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_5.tStop = t  # not accounting for scr refresh
                sound_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_5, 'tStopRefresh')  # time at next scr refresh
                sound_5.stop()
        # start/stop sound_6
        if sound_6.status == NOT_STARTED and sound_5.status==FINISHED:
            # keep track of start time/frame for later
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.tStart = t  # local t and not account for scr refresh
            sound_6.tStartRefresh = tThisFlipGlobal  # on global time
            sound_6.play()  # start the sound (it finishes automatically)
        if sound_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_6.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_6.tStop = t  # not accounting for scr refresh
                sound_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_6, 'tStopRefresh')  # time at next scr refresh
                sound_6.stop()
        # start/stop sound_7
        if sound_7.status == NOT_STARTED and sound_6.status==FINISHED:
            # keep track of start time/frame for later
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.tStart = t  # local t and not account for scr refresh
            sound_7.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7.play()  # start the sound (it finishes automatically)
        if sound_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_7.tStop = t  # not accounting for scr refresh
                sound_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7, 'tStopRefresh')  # time at next scr refresh
                sound_7.stop()
        # start/stop sound_8
        if sound_8.status == NOT_STARTED and sound_7.status==FINISHED:
            # keep track of start time/frame for later
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.tStart = t  # local t and not account for scr refresh
            sound_8.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8.play()  # start the sound (it finishes automatically)
        if sound_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_8.tStop = t  # not accounting for scr refresh
                sound_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
                sound_8.stop()
        # start/stop sound_9
        if sound_9.status == NOT_STARTED and sound_8.status==FINISHED:
            # keep track of start time/frame for later
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.tStart = t  # local t and not account for scr refresh
            sound_9.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9.play()  # start the sound (it finishes automatically)
        if sound_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_9.tStop = t  # not accounting for scr refresh
                sound_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9, 'tStopRefresh')  # time at next scr refresh
                sound_9.stop()
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            if bool(sound_9.status==FINISHED):
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_2"-------
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_5.stop()  # ensure sound has stopped at end of routine
    sound_6.stop()  # ensure sound has stopped at end of routine
    sound_7.stop()  # ensure sound has stopped at end of routine
    sound_8.stop()  # ensure sound has stopped at end of routine
    sound_9.stop()  # ensure sound has stopped at end of routine
    # the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response"-------
    continueRoutine = True
    # update component parameters for each repeat
    if change == "yes":
        corr_ans = "right"
        corr_resp = "different"
    elif change == "no":
        corr_ans = "left"
        corr_resp = "same"
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    responseComponents = [key_resp, text, text_3, text_5]
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
            theseKeys = key_resp.getKeys(keyList=['right','left'], waitRelease=False)
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
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
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
    feedback_msg = ''
    if key_resp.corr == 1:
        feedback_msg = f"Correct! The melodies were {corr_resp.upper()}."
    else:
        feedback_msg = f"Incorrect. The melodies were {corr_resp.upper()}. The correct answer was {corr_ans.upper()}."
        
    
    if change == "no":
        total_accuracy_same += key_resp.corr
        trial_count_same += 1
    elif change_condition == "contour":
        total_accuracy_contour += key_resp.corr
        trial_count_contour += 1
    elif change_condition == "interval":
        total_accuracy_interval += key_resp.corr
        trial_count_interval += 1
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

total_accuracy_same = 0
total_accuracy_contour = 0
total_accuracy_interval = 0

trial_count_same = 0
trial_count_contour = 0
trial_count_interval = 0
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
trials = data.TrialHandler(nReps=trial_n, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('tone_conds.csv'),
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
    stim_tone_1 = []
    stim_ints = []
    stim_tone_2 = []
    
    
    for i in range(5):
        stim_int = random.randint(1,7)
        while [stim_int] == stim_ints[-1:]:
            stim_int = random.randint(1,7)
        stim_ints.append(stim_int)
        stim_tone_1.append(sound_tones[stim_int])
                
    stim_tone_2 = stim_tone_1.copy()
    
    tone_change = random.randint(1,4)
    
    if (change == "yes") and (change_condition == "contour"):
        contour_change = random.choice(["1", "-1"])
        new_tone = stim_ints[tone_change] + int(contour_change)
        while (new_tone == 8) or (new_tone == 0):
            tone_change = random.randint(1,4)
            new_tone = stim_ints[tone_change] + int(contour_change)
        stim_tone_2[tone_change] = sound_tones[new_tone]
    elif(change == "yes") and (change_condition == "interval"):
        note_1 = stim_ints[tone_change]
        note_2 = stim_ints[tone_change-1]
        if note_1 > note_2:
            note_3 = stim_ints[tone_change] + 1
        elif note_1 < note_2:
            note_3 = stim_ints[tone_change] - 1
        while (note_3 == 8) or (note_3 == 0):
            tone_change = random.randint(1,4)
            note_1 = stim_ints[tone_change]
            note_2 = stim_ints[tone_change-1]
            if note_1 > note_2:
                note_3 = stim_ints[tone_change] + 1
            elif note_1 < note_2:
                note_3 = stim_ints[tone_change] - 1
        stim_tone_2[tone_change] = sound_tones[note_3]
    
    
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
    
    # ------Prepare to start Routine "trial_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_0.setSound(stim_tone_1[0], secs=tone_time, hamming=True)
    sound_0.setVolume(1.0, log=False)
    sound_1.setSound(stim_tone_1[1], secs=tone_time, hamming=True)
    sound_1.setVolume(1.0, log=False)
    sound_2.setSound(stim_tone_1[2], secs=tone_time, hamming=True)
    sound_2.setVolume(1.0, log=False)
    sound_3.setSound(stim_tone_1[3], secs=tone_time, hamming=True)
    sound_3.setVolume(1.0, log=False)
    sound_4.setSound(stim_tone_1[4], secs=tone_time, hamming=True)
    sound_4.setVolume(1.0, log=False)
    # keep track of which components have finished
    trial_1Components = [sound_0, sound_1, sound_2, sound_3, sound_4, text_8]
    for thisComponent in trial_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_1"-------
    while continueRoutine:
        # get current time
        t = trial_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_0
        if sound_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_0.frameNStart = frameN  # exact frame index
            sound_0.tStart = t  # local t and not account for scr refresh
            sound_0.tStartRefresh = tThisFlipGlobal  # on global time
            sound_0.play(when=win)  # sync with win flip
        if sound_0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_0.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_0.tStop = t  # not accounting for scr refresh
                sound_0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_0, 'tStopRefresh')  # time at next scr refresh
                sound_0.stop()
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and sound_0.status==FINISHED:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and sound_1.status==FINISHED:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play()  # start the sound (it finishes automatically)
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and sound_2.status==FINISHED:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3.play()  # start the sound (it finishes automatically)
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
                sound_3.stop()
        # start/stop sound_4
        if sound_4.status == NOT_STARTED and sound_3.status==FINISHED:
            # keep track of start time/frame for later
            sound_4.frameNStart = frameN  # exact frame index
            sound_4.tStart = t  # local t and not account for scr refresh
            sound_4.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4.play()  # start the sound (it finishes automatically)
        if sound_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_4.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_4.tStop = t  # not accounting for scr refresh
                sound_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_4, 'tStopRefresh')  # time at next scr refresh
                sound_4.stop()
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            if bool(sound_4.status==FINISHED):
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_1"-------
    for thisComponent in trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_0.stop()  # ensure sound has stopped at end of routine
    sound_1.stop()  # ensure sound has stopped at end of routine
    sound_2.stop()  # ensure sound has stopped at end of routine
    sound_3.stop()  # ensure sound has stopped at end of routine
    sound_4.stop()  # ensure sound has stopped at end of routine
    # the Routine "trial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "delay"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    delayComponents = [text_7]
    for thisComponent in delayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    delayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "delay"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = delayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=delayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "delay"-------
    for thisComponent in delayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_7.started', text_7.tStartRefresh)
    trials.addData('text_7.stopped', text_7.tStopRefresh)
    
    # ------Prepare to start Routine "trial_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_5.setSound(stim_tone_2[0], secs=tone_time, hamming=True)
    sound_5.setVolume(1.0, log=False)
    sound_6.setSound(stim_tone_2[1], secs=tone_time, hamming=True)
    sound_6.setVolume(1.0, log=False)
    sound_7.setSound(stim_tone_2[2], secs=tone_time, hamming=True)
    sound_7.setVolume(1.0, log=False)
    sound_8.setSound(stim_tone_2[3], secs=tone_time, hamming=True)
    sound_8.setVolume(1.0, log=False)
    sound_9.setSound(stim_tone_2[4], secs=tone_time, hamming=True)
    sound_9.setVolume(1.0, log=False)
    # keep track of which components have finished
    trial_2Components = [sound_5, sound_6, sound_7, sound_8, sound_9, text_6]
    for thisComponent in trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_2"-------
    while continueRoutine:
        # get current time
        t = trial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_5
        if sound_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_5.frameNStart = frameN  # exact frame index
            sound_5.tStart = t  # local t and not account for scr refresh
            sound_5.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5.play(when=win)  # sync with win flip
        if sound_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_5.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_5.tStop = t  # not accounting for scr refresh
                sound_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_5, 'tStopRefresh')  # time at next scr refresh
                sound_5.stop()
        # start/stop sound_6
        if sound_6.status == NOT_STARTED and sound_5.status==FINISHED:
            # keep track of start time/frame for later
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.tStart = t  # local t and not account for scr refresh
            sound_6.tStartRefresh = tThisFlipGlobal  # on global time
            sound_6.play()  # start the sound (it finishes automatically)
        if sound_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_6.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_6.tStop = t  # not accounting for scr refresh
                sound_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_6, 'tStopRefresh')  # time at next scr refresh
                sound_6.stop()
        # start/stop sound_7
        if sound_7.status == NOT_STARTED and sound_6.status==FINISHED:
            # keep track of start time/frame for later
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.tStart = t  # local t and not account for scr refresh
            sound_7.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7.play()  # start the sound (it finishes automatically)
        if sound_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_7.tStop = t  # not accounting for scr refresh
                sound_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7, 'tStopRefresh')  # time at next scr refresh
                sound_7.stop()
        # start/stop sound_8
        if sound_8.status == NOT_STARTED and sound_7.status==FINISHED:
            # keep track of start time/frame for later
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.tStart = t  # local t and not account for scr refresh
            sound_8.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8.play()  # start the sound (it finishes automatically)
        if sound_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_8.tStop = t  # not accounting for scr refresh
                sound_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
                sound_8.stop()
        # start/stop sound_9
        if sound_9.status == NOT_STARTED and sound_8.status==FINISHED:
            # keep track of start time/frame for later
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.tStart = t  # local t and not account for scr refresh
            sound_9.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9.play()  # start the sound (it finishes automatically)
        if sound_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9.tStartRefresh + tone_time-frameTolerance:
                # keep track of stop time/frame for later
                sound_9.tStop = t  # not accounting for scr refresh
                sound_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9, 'tStopRefresh')  # time at next scr refresh
                sound_9.stop()
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            if bool(sound_9.status==FINISHED):
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_2"-------
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_5.stop()  # ensure sound has stopped at end of routine
    sound_6.stop()  # ensure sound has stopped at end of routine
    sound_7.stop()  # ensure sound has stopped at end of routine
    sound_8.stop()  # ensure sound has stopped at end of routine
    sound_9.stop()  # ensure sound has stopped at end of routine
    # the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response"-------
    continueRoutine = True
    # update component parameters for each repeat
    if change == "yes":
        corr_ans = "right"
        corr_resp = "different"
    elif change == "no":
        corr_ans = "left"
        corr_resp = "same"
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    responseComponents = [key_resp, text, text_3, text_5]
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
            theseKeys = key_resp.getKeys(keyList=['right','left'], waitRelease=False)
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
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
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
    feedback_msg = ''
    if key_resp.corr == 1:
        feedback_msg = f"Correct! The melodies were {corr_resp.upper()}."
    else:
        feedback_msg = f"Incorrect. The melodies were {corr_resp.upper()}. The correct answer was {corr_ans.upper()}."
        
    
    if change == "no":
        total_accuracy_same += key_resp.corr
        trial_count_same += 1
    elif change_condition == "contour":
        total_accuracy_contour += key_resp.corr
        trial_count_contour += 1
    elif change_condition == "interval":
        total_accuracy_interval += key_resp.corr
        trial_count_interval += 1
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
block_count += 1
# the Routine "end_block" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "final"-------
continueRoutine = True
# update component parameters for each repeat
msg_1 = f'Same\n {round((total_accuracy_same)/(trial_count_same), 2)}'
msg_2 = f'Different (Contour)\n {round((total_accuracy_contour)/(trial_count_contour), 2)}'
msg_3 = f'Different (Interval)\n {round((total_accuracy_interval)/(trial_count_interval), 2)}'

thisExp.addData(f"total_accuracy_same", round((total_accuracy_same)/(trial_count_same), 2))
thisExp.addData(f"total_accuracy_contour", round((total_accuracy_contour)/(trial_count_contour), 2))
thisExp.addData(f"total_accuracy_interval", round((total_accuracy_interval)/(trial_count_interval), 2))
end_text_1.setText(msg_1)
end_text_2.setText(msg_2)
end_text_3.setText(msg_3)
key_resp_end.keys = []
key_resp_end.rt = []
_key_resp_end_allKeys = []
# keep track of which components have finished
finalComponents = [end_text, end_text_1, end_text_2, end_text_3, end_text_6, key_resp_end]
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
    
    # *end_text_1* updates
    if end_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text_1.frameNStart = frameN  # exact frame index
        end_text_1.tStart = t  # local t and not account for scr refresh
        end_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text_1, 'tStartRefresh')  # time at next scr refresh
        end_text_1.setAutoDraw(True)
    
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
    
    # *end_text_6* updates
    if end_text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text_6.frameNStart = frameN  # exact frame index
        end_text_6.tStart = t  # local t and not account for scr refresh
        end_text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text_6, 'tStartRefresh')  # time at next scr refresh
        end_text_6.setAutoDraw(True)
    
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
