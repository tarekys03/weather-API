import numpy as np
import pandas as pd
from scipy.stats import pearsonr
pd.set_option('display.max_columns' , None)




def classify_temperature(temp):
    if temp < 10:
        return "low temperature, Turn on the heating system"
    elif temp > 20:
        return "High temperature, Turn on the air conditioning system"
    else:
        return "Normal"

def classify_humidity(hum):
    if hum < 20:
        return "Low humidity, Open the window slightly for a short while."
    elif hum > 45:
        return "High humidity, Turn on steam removal mode."
    else:
        return "Normal"

def classify_barometer(pressure):
    if pressure < 23:
        return "Low pressure, Open the window slightly for a short while."
    elif pressure > 30:
        return "High pressure, Open the window slightly for a short while."
    else:
        return "Normal"

def classify_windspeed(ws):
    if ws > 15:
        return "Fast winds, Drive carefully and slow down."
    else:
        return "Calm"

def classify_Rain(rain):
    if rain > 1:
        return "Beware of rain and use wipers."
    else:
        return "No Rain"

def classify_Light(light):
    if light < 250:
        return "The lighting is dimmed, turn on the lights"
    elif light > 600:
        return "Bright sun, use sunglasses"
    else:
        return "Normal"