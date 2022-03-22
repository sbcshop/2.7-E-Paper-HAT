import sys
import os
import serial
import lib_2inch7_e_paper
import time
from PIL import Image,ImageDraw,ImageFont

def read_rfid ():
   ser = serial.Serial ("/dev/ttyS0")                           #Open named port 
   ser.baudrate = 9600                                            #Set baud rate to 9600
   data = ser.read(12)                                            #Read 12 characters from serial port to data
   ser.close ()                                                   #Close port
   data=data.decode("utf-8")
   return data

while True:
    try:
        
        e_paper = lib_2inch7_e_paper.E_Paper()
        e_paper.init()              
        
        font24 = ImageFont.truetype(('images/Font.ttc'), 24)
        font18 = ImageFont.truetype(('images/Font.ttc'), 18)
        font30 = ImageFont.truetype(('images/Font.ttc'), 30)
        font40 = ImageFont.truetype(('images/Font.ttc'), 40)

        # Drawing on the Horizontal image
        Himage = Image.open('images/as.bmp')
        e_paper.display(e_paper.buffer(Himage))
        time.sleep(1)

        data = read_rfid()
        Himage = Image.new('1', (e_paper.height, e_paper.width), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(Himage)
        draw.text((10, 20),data, font = font30)
        e_paper.display(e_paper.buffer(Himage))
        time.sleep(2)

        e_paper.clear_screen(0xFF)
        e_paper.sleep()
            

    except KeyboardInterrupt:    
        e_paper2in7.e_paperconfig.module_exit()
        exit()
