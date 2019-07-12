# This is your main script.
# Don't Touch

import control
from time import sleep
import network
import json
import urequests
from time import sleep
from _thread import start_new_thread as thread
from machine import PWM, Pin

def test():
    # Test LED
    R = Pin(21, Pin.OUT)
    G = Pin(19, Pin.OUT)
    B = Pin(18, Pin.OUT)
    
    # Test Button
    # 1 = Idle, 0 = Pressed
    BTN = Pin(25, Pin.IN)

    # Test Buzzer
    Buzzer = PWM(Pin(26))
    # Test Obstacle
    OBS = Pin(13, Pin.OUT)

    R.value(0)
    G.value(1)
    B.value(0)

    # Test Servo
    servo = PWM(Pin(22), freq=50, duty=40)
    
    servo.duty(30)
    sleep(0.5)
    servo.duty(70)
    sleep(0.5)
    # while True:
    #     if (BTN.value() == 0):
    #         print('Pressed: {}'.format(not bool(BTN.value())))
    #         OBS.value(1)
    #         R.value(1)
    #         G.value(0)
    #         B.value(0)
    #         servo.duty(30)
    #         sleep(0.5)
    #         servo.deinit()
    #         Buzzer.freq(300)
    #         print('BEEP!')
    #     else:
    #         R.value(0)
    #         G.value(1)
    #         B.value(0)
    #         OBS.value(0)
    #         servo.duty(70)
    #     sleep(0.5)
#test()

global lightstate
global doorstate
global alarmstate
global ledstate

doorstate = 'off'
ledstate = 'on'
alarmstate = 'off'

lightstate = True


def lightcontrol(mode):
    global lightstate
    global ledstate
    if ledstate == 'off':
        mode == 'off'
    if mode == 'red':
        control.R.value(1)
        control.G.value(0)
        control.B.value(0)
    if mode == 'green':
        control.R.value(0)
        control.G.value(1)
        control.B.value(0)
    if mode == 'blue':
        control.R.value(0)
        control.G.value(0)
        control.B.value(1)
    if mode == 'off':
        control.R.value(0)
        control.G.value(0)
        control.B.value(0)

    if mode == 'flash':
        if lightstate:
            lightcontrol('red')
            sleep(0.1)
            lightstate = False
        else:
            lightcontrol('off')
            sleep(0.1)
            lightstate = True

def doorcontrol():
    while True:
        if control.BTN.value() == 0:
            control.servo.duty(120)
            lightcontrol('blue')
            print('Door Open')
            sleep(3)
            print('Door Close')
            control.servo.duty(40)
            lightcontrol('green')
            sleep(0.2)
        sleep(0.1)

def connect():
    control.station.active(True)
    control.station.connect(control.SSID, control.PWD)
    
    while not control.station.isconnected():
        control.station.connect(control.SSID, control.PWD)
        print('Connecting ...')
        sleep(2)
    if control.station.isconnected():
        print('Connected')
    
    while control.station.isconnected():
        sleep(5)
        print('Still Connected')
    if not control.station.isconnected():
        connect()

def beep(sl_duration):
    Buzzer = PWM(Pin(26))
    Buzzer.freq(500)
    sleep(sl_duration)
    Buzzer.deinit()

def webcontrol():
    global ledstate
    global doorstate
    global alarmstate

    while True:
        # Fetch from server.
        # Get data
        data = {'door': doorstate,
                'buzzer': alarmstate,
                'light': alarmstate}

def alarmsys():
    control.OBS.value(1)
    print('Alarm System Initiated')
    while True:
        obs = control.LDIO.read()
        print(obs)
        if obs > 3000:
            print('ALERT!')
            beep(0.1)
            lightcontrol('flash')
        else:
            lightcontrol('green')
        sleep(0.1)


thread(connect, ())
thread(doorcontrol, ())
thread(alarmsys, ())