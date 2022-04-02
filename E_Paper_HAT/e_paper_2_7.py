import sys
import os
import lib_2inch7_e_paper
import time
from PIL import Image,ImageDraw,ImageFont

try:
    e_paper = lib_2inch7_e_paper.E_Paper()
    e_paper.init()              
    
    font24 = ImageFont.truetype(('images/Font.ttc'), 24)
    font18 = ImageFont.truetype(('images/Font.ttc'), 18)
    font30 = ImageFont.truetype(('images/Font.ttc'), 30)
    font40 = ImageFont.truetype(('images/Font.ttc'), 40)

    # Drawing on the Horizontal image
    Himage = Image.open('images/img.bmp')
    e_paper.display(e_paper.buffer(Himage))
    time.sleep(1)
    
    Himage = Image.new('1', (e_paper.height, e_paper.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 20), 'HAPPY NEW YEAR', font = font30)
    draw.text((80, 60), '2022', font = font40, fill = 0)
    e_paper.display(e_paper.buffer(Himage))
    time.sleep(1)
    
    # Drawing on the Vertical image
    H_image = Image.new('1', (e_paper.height, e_paper.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(H_image)
    draw.text((20, 20), 'HELLO WORLD!!', font = font30, fill =0 )
    e_paper.display(e_paper.buffer(H_image))
    time.sleep(1)

    e_paper.clear_screen(0xFF)
    e_paper.sleep()
        

except KeyboardInterrupt:    
    lib_2inch7_e_paper.e_paper_config .module_exit()
    exit()
