# 2.7-E-Paper-HAT
<img src= "https://github.com/sbcshop/2.7-E-Paper-HAT/blob/main/images/img2.png" />
<img src= "https://github.com/sbcshop/2.7-E-Paper-HAT/blob/main/images/img.JPG" />

### 2.7-inch e-paper display is an Active Matrix Electrophoretic Display(AMEPD) with 264*176 resolution respectively, comes with SPI interface.e-paper HAT comes in two variant with the ability to display black-and-white or black-white-red graphics. Without power, your image will persist endlessly - display it, then turn off the electricity. These e-paper display modules don't require any power after they've been updated, and they may even be turned off completely, with the content remaining on the screen indefinitely. These e-ink screen is ideal for solar or battery-powered devices

<img src= "https://github.com/sbcshop/2.7-E-Paper-HAT/blob/main/images/img4.jpg" />

## Code
### First of all, you need to enable SPI in raspberry pi, for this you need to go 
```sudo raspi-config ``` 

then go to "interface options->SPI->yes->press enter" 
There are two folder in GitHub repository
 * E_Paper_HAT (Black Color)
   * e_paper_2_7.py        -> Run this file
   * lib_2inch7_e_paper.py -> Library of 2.7 inch e-paper HAT
   * e_paper_buttons.py    -> Run this file if you want to use onboard push buttons (application)
   * e_paper_2_7_rfid.py   -> Run this file if you want to connect RFID HAT (application)
   
 * Red_Color_E_Paper_HAT (Red & Black Color)
   * e_paper_2in7_redColor.py  -> Run this file 
   * lib_2inch7_ec_paper.py    -> Library of 2.7 inch e-paper red color HAT
   * e_paper_2in7_color_air.py -> Run this file if you want to display values of Air monitoring HAT or breakout (application)
   * pms_a003.py               -> Library of air monitoring HAT or breakout
   

## Application
### RFID 
#### Display RFID data to e-paper HAT, for this you need to go "E_Paper_HAT" folder inside this folder there is a python file name "e_paper_2_7_rfid.py",run this file
<img src= "https://github.com/sbcshop/2.7-E-Paper-HAT/blob/main/images/img3.jpg" />

## Air Monitoring 
#### Display Air Monitoring hat or breakout data to e-paper HAT, for this you need to go "Red_Color_E_Paper_HAT" folder inside this folder there is a python file name "e_paper_2in7_color_air.py",run this file
<img src= "https://github.com/sbcshop/2.7-E-Paper-HAT/blob/main/images/giff.gif" />

## E-Paper video

https://www.youtube.com/watch?v=dvTVPM_a0zQ&ab_channel=SBComponentsLtd

Related Documents:
- [2.7" E-paper HAT Schematic](https://github.com/sbcshop/2.7-E-Paper-HAT/blob/main/Documents/E-paper%20HAT%20SCH.pdf)
- [2.7" E-paper Specification](https://github.com/sbcshop/2.7-E-Paper-HAT/blob/main/Documents/E-paper%202.7%20Specs.pdf)
