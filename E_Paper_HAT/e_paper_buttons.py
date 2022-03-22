#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import lib_2inch7_e_paper
import time
from PIL import Image,ImageDraw,ImageFont
import RPi.GPIO as GPIO

KEY1_PIN       = 5
KEY2_PIN       = 6
KEY3_PIN       = 13
KEY4_PIN       = 19


GPIO.setmode(GPIO.BCM) 
GPIO.setup(KEY1_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY2_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY3_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY4_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)# Input with pull-up



while True:
    
        e_paper = lib_2inch7_e_paper.E_Paper()
        e_paper.init()                   #'''2Gray(Black and white) display'''
        
        font24 = ImageFont.truetype(('images/Font.ttc'), 24)
        font18 = ImageFont.truetype(('images/Font.ttc'), 18)
        font30 = ImageFont.truetype(('images/Font.ttc'), 30)
        font40 = ImageFont.truetype(('images/Font.ttc'), 40)

        if GPIO.input(KEY1_PIN) == GPIO.LOW: # button is released
            # Drawing on the Horizontal image
            Himage = Image.open('images/img.bmp')
            e_paper.display(e_paper.buffer(Himage))
            #time.sleep(3)

        
        if GPIO.input(KEY2_PIN) == GPIO.LOW: # button is released
            Himage = Image.new('1', (e_paper.height, e_paper.width), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(Himage)
            draw.text((10, 20), 'HAPPY NEW YEAR', font = font30)
            draw.text((80, 60), '2022', font = font40, fill = 0)
            draw.text((20, 120), 'HELLO WORLD!!', font = font30, fill =0 )
            e_paper.display(e_paper.buffer(Himage))
            #time.sleep(4)
        
        # Drawing on the Vertical image
        if GPIO.input(KEY3_PIN) == GPIO.LOW: # button is released
            Himage = Image.open('images/img1.bmp')
            e_paper.display(e_paper.buffer(Himage))
            #time.sleep(3)
            
            
        if GPIO.input(KEY4_PIN) == GPIO.LOW: # button is released
            Himage = Image.open('images/img2.bmp')
            e_paper.display(e_paper.buffer(Himage))
            #time.sleep(3)
            


 
        
