# Red color e-paper

import sys
import os
import lib_2inch7_ec_paper
import time
from PIL import Image,ImageDraw,ImageFont


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
    
    drawblack = ImageDraw.Draw(horizontal_black_image)
    drawred = ImageDraw.Draw(horizontal_red_image)
    drawred.text((10, 0), 'Hello World', font = font28, fill = 0)
    e_paper.display(e_paper.buffer(horizontal_black_image),e_paper.buffer(horizontal_red_image))
    time.sleep(1)
    
    
    # Drawing on the Vertical image
    vertical_black_image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 126*298
    vertical_red_image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 126*298
    drawblack = ImageDraw.Draw(vertical_black_image)
    drawred = ImageDraw.Draw(vertical_red_image)
    
    drawblack.text((2, 0), 'Hello World', font = font28, fill = 0)
    e_paper.display(e_paper.buffer(vertical_black_image), e_paper.buffer(vertical_red_image))
    time.sleep(1)
    
    horizontal_black_image = Image.open('images/img2.bmp')
    #horizontal_red_image = Image.open('images/as.bmp')
    e_paper.display(e_paper.buffer(horizontal_black_image), e_paper.buffer(horizontal_red_image))
    time.sleep(2)

    e_paper.Clear_screen()
    
    e_paper.sleep()
    e_paper.exit()
    
except KeyboardInterrupt:    
    e_paper2in7b.e_paperconfig.module_exit()
    exit()
