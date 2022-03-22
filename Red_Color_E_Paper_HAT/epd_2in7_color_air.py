# Red color e-paper

import sys
import os
import lib_2inch7_ec_paper
import time
from PIL import Image,ImageDraw,ImageFont
from pms_a003 import Sensor


air_mon = Sensor()
air_mon.connect_hat(port="/dev/ttyS0", baudrate=9600)

while True:
    try:    
        e_paper = lib_2inch7_ec_paper.Ec_Paper()
        e_paper.init()
        
        # Drawing on the image
        black_image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
        red_image = Image.new('1', (e_paper.width, e_paper.height), 255)  #
        
        font28 = ImageFont.truetype(('images/Font.ttc'), 28)
        font18 = ImageFont.truetype(('images/Font.ttc'), 18)
        

        # Drawing on the Horizontal image
        horizontal_black_image = Image.new('1', (e_paper.height, e_paper.width), 255)  # 298*126
        horizontal_red_image = Image.new('1', (e_paper.height, e_paper.width), 255)  # 298*126
        
        values = air_mon.read()
        print("PMS 1 value is {}".format(values.pm10_cf1))
        print("PMS 2.5 value is {}".format(values.pm25_cf1))
        print("PMS 10 value is {}".format(values.pm100_cf1))
        
        drawblack = ImageDraw.Draw(horizontal_black_image)
        drawred = ImageDraw.Draw(horizontal_red_image)
        
        drawred.text((10, 0), 'AIR MONITORING', font = font28, fill = 0)
        drawblack.text((10, 40), 'PMS 1 value    = ', font = font28, fill = 0)
        drawblack.text((10, 80), 'PMS 2.5 value = ', font = font28, fill = 0)
        drawblack.text((10, 120), 'PMS 10 value  =', font = font28, fill = 0)

        drawred.text((210, 40), str(values.pm10_cf1), font = font28, fill = 0)
        drawred.text((210, 80), str(values.pm25_cf1), font = font28, fill = 0)
        drawred.text((210, 120),str(values.pm100_cf1), font = font28, fill = 0)
        e_paper.display(e_paper.buffer(horizontal_black_image),e_paper.buffer(horizontal_red_image))
        time.sleep(4)

        e_paper.Clear_screen()
        
        #e_paper.exit()
        
    except KeyboardInterrupt:    
        epd_2in7_color_air.e_paperconfig.module_exit()
        exit()
