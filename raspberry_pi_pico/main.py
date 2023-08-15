# Raspberry Pico plant watering controller
# Copyright (c) Kjeld Jensen <kjen@sdu.dk> <kj@kjen.dk>
# 2023-04-19, KJ, First version

from machine import Pin, ADC, UART
import utime
from sys import stdin
import uselect

import time
from senors import Moisture
pump_control = Pin(16, Pin.OUT)
pump_water_alarm_pin = Pin(9, mode=Pin.IN)
plant_water_alarm_pin = Pin(13, mode=Pin.IN)

moisture_sensor_pin = Pin(26, mode=Pin.IN)
moisture_sensor = ADC(moisture_sensor_pin)
photo_resistor_pin = Pin(27, mode=Pin.IN)
light_sensor = ADC(photo_resistor_pin)
led_builtin = Pin(25, Pin.OUT)
uart = machine.UART(0, 115200)
WATER_PUMP_PIN = 10
water_pump = machine.Pin(WATER_PUMP_PIN, machine.Pin.OUT)

def turn_on_water_pump():
    water_pump.value(1)

# water pump off
def turn_off_water_pump():
    water_pump.value(0)


#run water pump in intervals
def run_water():    
 turn_on_water_pump()
 time.sleep(2)  # Adjust
 turn_off_water_pump()
 print("Pump request completed.")
 
 
def moisture():
    return moisture_sensor.read_u16() / 655.36

def plant_alarm():
    return light_sensor.read_u16() / 655.36
def pump_alarm():
    return moisture_sensor.read_u16() / 655.36

def light():
    return light_sensor.read_u16() / 655.36

def pump_request():
    result = False
    select_result = uselect.select([stdin], [], [], 0)
    while select_result[0]:
        ch = stdin.read(1)
        if ch == 'p':
            result = True
        select_result = uselect.select([stdin], [], [], 0)
    return result

def read_sync_flag():
    try:
        with open("sync_flag.txt", "r") as file:
            return file.read().strip() == "True"
    except FileNotFoundError:
        return False  


pump_a = False
while True:
  time.sleep(0.1)
  moisture = Moisture()
  pumpwater = pump_water_alarm_pin.value()
  plantwater = plant_water_alarm_pin.value()
 
  if pump_request() and not pump_a:  # make sure it's turned off after inital activation
     run_water()
     pump_a = True
     time.sleep(3)
  else: 
   pump_a = False
   readings = [moisture, pumpwater,plantwater, light()] #Data set of meassurements
   print(readings)

