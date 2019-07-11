# Control goes here.

#Import goes here.
from machine import Pin, ADC, PWM
from time import sleep
import network

# Initial Class

R = Pin(21, Pin.OUT)
G = Pin(19, Pin.OUT)
B = Pin(18, Pin.OUT)
LDIO = ADC(Pin(32))

# 1 = Idle, 0 = Pressed
BTN = Pin(25, Pin.IN)

OBS = Pin(13, Pin.OUT)

#Servo
servo = PWM(Pin(22), freq=50, duty=70)

#Server
URL = 'https://exceed.superposition.pknn.dev/data/jitrada'
SSID = 'exceed16_9'
PWD = '12345678'
station = network.WLAN(network.STA_IF)