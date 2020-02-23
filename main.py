import RPi.GPIO as GPIO
import pyaudio
from scipy import signal
import numpy as np
import string
from time import sleep
import sys
import Tkinter
import tkSnack
import serial

#PyAudio = pyaudio.PyAudio

fs=4000;

ser=serial.Serial('/dev/ttyACM0',4800)
ser.flush()

GPIO.setmode(GPIO.BOARD)

button1 = 11
button2 = 12
button3 = 13
button4 = 15
button5 = 16
button6 = 18
button7 = 22
button8 = 29
button9 = 31
button10 = 32
button11 = 33
button12 = 35
button13 = 36
button14 = 37



GPIO.setup(7,GPIO.OUT)
GPIO.setup(button1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button6, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button7, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button8, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button9, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button10, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button11, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button12, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button13, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button14, GPIO.IN, GPIO.PUD_DOWN)


keys=[[0 for x in range(13)] for x in range(13)]

keys[1][1] = 130.813
keys[1][2] = 138.591
keys[1][3] = 146.832
keys[1][4] = 155.563
keys[1][5] = 164.814
keys[1][6] = 174.614
keys[1][7] = 184.997
keys[1][8] = 195.998
keys[1][9] = 207.652
keys[1][10] = 220
keys[1][11] = 233.082
keys[1][12] = 246.942

keys[2][1] = 261.626
keys[2][2] = 277.183
keys[2][3] = 293.665
keys[2][4] = 311.127
keys[2][5] = 329.628
keys[2][6] = 349.228
keys[2][7] = 369.994
keys[2][8] = 391.995
keys[2][9] = 415.305
keys[2][10] = 440
keys[2][11] = 466.164
keys[2][12] = 493.883

keys[3][1] = 523.251
keys[3][2] = 554.365
keys[3][3] = 587.330
keys[3][4] = 622.254
keys[3][5] = 659.255
keys[3][6] = 698.456
keys[3][7] = 739.989
keys[3][8] = 783.991
keys[3][9] = 830.609
keys[3][10] = 880
keys[3][11] = 932.328
keys[3][12] = 987.767


bsound=1
delay=1
delay2=0.25


def playNote(freq, duration, base):
    """play a note of freq (hertz) for duration (seconds)"""
    snd = tkSnack.Sound()
    if bsound ==1:
        filt = tkSnack.Filter('generator', freq, 44100, 0.0, 'sine', int(11500*duration))
    elif bsound==2:
        filt = tkSnack.Filter('generator', freq, 44100, 0.5, 'rectangle', int(11500*duration))
    elif bsound==3:
        filt = tkSnack.Filter('generator', freq, 44100, 0.0, 'triangle', int(11500*duration))
    
    snd.stop()
    for i in range(delay) :
        snd.play(filter=filt, blocking=1)
        sleep(delay2)
    
def soundStop():
    """stop the sound the hard way"""
    try:
        root = root.destroy()
        filt = None
    except:
        pass
root = Tkinter.Tk()
# have to initialize the sound system, required!!
tkSnack.initializeSnack(root)
# set the volume of the sound system (0 to 100%)

# play a note of requency 440 hertz (A4) for a duration of 5 seconds
#playNote(440, 5 , 1)
# play a note of requency 261.6 hertz (C4) for a duration of 5 seconds
#playNote(440, 5 , 2)

playNote(440, 1 , 3)


# optional
soundStop()
root.withdraw()



#print
print ("Begin")

#print
GPIO.setwarnings(False)
duration = .5
octave = 1
bsound = 1

while True:

    line=(ser.read())
        
    
    while GPIO.input(button13) == True:
	    octave=octave+1
	    sleep(1)
	    if octave >= 4:
		    octave = 1

    while GPIO.input(button14) == True:
	    bsound=bsound+1
	    sleep(1)
	    if bsound >= 4:
		    bsound = 1
	    
    
    volume=15
    
    while GPIO.input(delay) == True:
        delay=delay+1
        sleep(1)
        if delay >=5:
            delay = 1

    while GPIO.input(delay2) == True:
        delay2=delay2+0.25
        sleep(1)
        if delay2 >=1.25:
            delay2 = 0.25

    if line=='1':
        GPIO.output(7,True)
        f=keys[octave][11]               
        playNote(f, duration, bsound)
        sleep(0.2)
    
    if line=='2':
        GPIO.output(7,True)
        f=keys[octave][9]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    if line=='3':
        GPIO.output(7,True)
        f=keys[octave][7]
        playNote(f, duration, bsound)
        sleep(0.2)

    if line=='4':
        GPIO.output(7,True)
        f=keys[octave][4]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    if line=='5':
        GPIO.output(7,True)
        f=keys[octave][2]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    if line=='6':
        GPIO.output(7,True)
        f=keys[octave][1]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    if line=='7':
        GPIO.output(7,True)
        f=keys[octave][3]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    if line=='8':
        GPIO.output(7,True)
        f=keys[octave][5]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    if line=='9':
        GPIO.output(7,True)
        f=keys[octave][6]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    if line=='10':
        GPIO.output(7,True)
        f=keys[octave][8]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    if line=='11':
        GPIO.output(7,True)
        f=keys[octave][10]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    if line=='12':
        GPIO.output(7,True)
        f=keys[octave][12]
        playNote(f, duration, bsound)
        sleep(0.2)
        
    GPIO.output(7,False)
    
    

    	
GPIO.cleanup();


        
