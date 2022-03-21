import logging
import Ec_Paperconfig

# e-paper display resolution
width       = 176
height      = 264

Ec_Paperconfig = Ec_Paperconfig.e_paper_config()

class Ec_Paper: # red color e paper
    def __init__(self):
        self.reset_pin = Ec_Paperconfig.RST_PIN
        self.dc_pin = Ec_Paperconfig.DC_PIN
        self.busy_pin = Ec_Paperconfig.BUSY_PIN
        self.cs_pin = Ec_Paperconfig.CS_PIN
        self.width = width
        self.height = height

    lut_vcom_dc = [
        0x00, 0x00,
        0x00, 0x1A, 0x1A, 0x00, 0x00, 0x01,
        0x00, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0x00, 0x0E, 0x01, 0x0E, 0x01, 0x10,
        0x00, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0x00, 0x04, 0x10, 0x00, 0x00, 0x05,
        0x00, 0x03, 0x0E, 0x00, 0x00, 0x0A,
        0x00, 0x23, 0x00, 0x00, 0x00, 0x01
    ]

    lut_ww = [
        0x90, 0x1A, 0x1A, 0x00, 0x00, 0x01,
        0x40, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0x84, 0x0E, 0x01, 0x0E, 0x01, 0x10,
        0x80, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0x00, 0x04, 0x10, 0x00, 0x00, 0x05,
        0x00, 0x03, 0x0E, 0x00, 0x00, 0x0A,
        0x00, 0x23, 0x00, 0x00, 0x00, 0x01
    ]

    lut_bw = [
        0xA0, 0x1A, 0x1A, 0x00, 0x00, 0x01,
        0x00, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0x84, 0x0E, 0x01, 0x0E, 0x01, 0x10,
        0x90, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0xB0, 0x04, 0x10, 0x00, 0x00, 0x05,
        0xB0, 0x03, 0x0E, 0x00, 0x00, 0x0A,
        0xC0, 0x23, 0x00, 0x00, 0x00, 0x01
    ]
    lut_wb = [
        0x90, 0x1A, 0x1A, 0x00, 0x00, 0x01,
        0x20, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0x84, 0x0E, 0x01, 0x0E, 0x01, 0x10,
        0x10, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0x00, 0x04, 0x10, 0x00, 0x00, 0x05,
        0x00, 0x03, 0x0E, 0x00, 0x00, 0x0A,
        0x00, 0x23, 0x00, 0x00, 0x00, 0x01
        ]
    
    lut_bb = [
        0x90, 0x1A, 0x1A, 0x00, 0x00, 0x01,
        0x40, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0x84, 0x0E, 0x01, 0x0E, 0x01, 0x10,
        0x80, 0x0A, 0x0A, 0x00, 0x00, 0x08,
        0x00, 0x04, 0x10, 0x00, 0x00, 0x05,
        0x00, 0x03, 0x0E, 0x00, 0x00, 0x0A,
        0x00, 0x23, 0x00, 0x00, 0x00, 0x01
    ]



    # Hardware reset
    def reset(self):
        Ec_Paperconfig.digitalwrite(self.reset_pin, 1)
        Ec_Paperconfig.delay_ms(200) 
        Ec_Paperconfig.digitalwrite(self.reset_pin, 0)
        Ec_Paperconfig.delay_ms(10)
        Ec_Paperconfig.digitalwrite(self.reset_pin, 1)
        Ec_Paperconfig.delay_ms(200)   

    def send_command(self, command):
        Ec_Paperconfig.digitalwrite(self.dc_pin, 0)
        Ec_Paperconfig.digitalwrite(self.cs_pin, 0)
        Ec_Paperconfig.spi_writebyte([command])
        Ec_Paperconfig.digitalwrite(self.cs_pin, 1)

    def send_data(self, data):
        Ec_Paperconfig.digitalwrite(self.dc_pin, 1)
        Ec_Paperconfig.digitalwrite(self.cs_pin, 0)
        Ec_Paperconfig.spi_writebyte([data])
        Ec_Paperconfig.digitalwrite(self.cs_pin, 1)
        
    def ReadBusy(self):
        while(Ec_Paperconfig.digitalread(self.busy_pin) == 0):      # 0: idle, 1: busy
            Ec_Paperconfig.delay_ms(100)
        
    def set_lut(self):
        self.send_command(0x20)               # vcom
        for count in range(0, 44):
            self.send_data(self.lut_vcom_dc[count])
        self.send_command(0x21)         # ww --
        for count in range(0, 42):
            self.send_data(self.lut_ww[count])
        self.send_command(0x22)         # bw r
        for count in range(0, 42):
            self.send_data(self.lut_bw[count])
        self.send_command(0x23)         # wb w
        for count in range(0, 42):
            self.send_data(self.lut_bb[count])
        self.send_command(0x24)         # bb b
        for count in range(0, 42):
            self.send_data(self.lut_wb[count])
            
    def init(self):
        if (Ec_Paperconfig.module_init() != 0):
            return -1
            
        self.reset()

        self.send_command(0x04) # POWER_ON
        self.ReadBusy()

        self.send_command(0x00) # PANEL_SETTING
        self.send_data(0xaf) #KW-BF   KWR-AF    BWROTP 0f
        
        self.send_command(0x30) # PLL_CONTROL
        self.send_data(0x3a) #3A 100HZ   29 150Hz 39 200HZ    31 171HZ

        self.send_command(0x01) # POWER_SETTING
        self.send_data(0x03) # VDS_EN, VDG_EN
        self.send_data(0x00) # VCOM_HV, VGHL_LV[1], VGHL_LV[0]
        self.send_data(0x2b) # VDH
        self.send_data(0x2b) # VDL
        self.send_data(0x09) # VDHR

        self.send_command(0x06) # BOOSTER_SOFT_START
        self.send_data(0x07)
        self.send_data(0x07)
        self.send_data(0x17)
        
        # Power optimization #######
        self.send_command(0xF8)
        self.send_data(0x60)
        self.send_data(0xA5)
        
        self.send_command(0xF8)
        self.send_data(0x73)
        self.send_data(0x41)
        ###########################

        self.send_command(0x82) # VCM_DC_SETTING_REGISTER
        self.send_data(0x12)                   
        self.send_command(0x50) # VCOM_AND_DATA_INTERVAL_SETTING
        self.send_data(0x87) # define by OTP

        self.set_lut()

        self.send_command(0x16) # PARTIAL_DISPLAY_REFRESH
        self.send_data(0x00)
        
        return 0

    def buffer(self, image):
        buf = [0xFF] * (int(self.width/8) * self.height)
        image_monocolor = image.convert('1')
        image_width, image_height = image_monocolor.size
        pixels = image_monocolor.load()
        
        if(image_width == self.width and image_height == self.height): # vertical
            for y in range(image_height):
                for x in range(image_width):
                    # Set the bits for the column of pixels at the current position.
                    if pixels[x, y] == 0:
                        buf[int((x + y * self.width) / 8)] &= ~(0x80 >> (x % 8))
                        
        elif(image_width == self.height and image_height == self.width): # horizontal
            for y in range(image_height):
                for x in range(image_width):
                    newx = y
                    newy = self.height - x - 1
                    if pixels[x, y] == 0:
                        buf[int((newx + newy*self.width) / 8)] &= ~(0x80 >> (y % 8))
        return buf

    def display(self, imageblack, imagered):
        self.send_command(0x10)
        for i in range(0, int(self.width * self.height / 8)):
            self.send_data(~imageblack[i])
        self.send_command(0x11)
        
        self.send_command(0x13)
        for i in range(0, int(self.width * self.height / 8)):
            self.send_data(~imagered[i])
        self.send_command(0x11)
        
        self.send_command(0x12) 
        self.ReadBusy()
        
    def Clear_screen(self):
        self.send_command(0x10)
        for i in range(0, int(self.width * self.height / 8)):
            self.send_data(0x00)
        self.send_command(0x11) 
        
        self.send_command(0x13)
        for i in range(0, int(self.width * self.height / 8)):
            self.send_data(0x00)
        self.send_command(0x11)
        
        self.send_command(0x12) 
        self.ReadBusy()

    def sleep(self):
        self.send_command(0X50)
        self.send_data(0xf7)
        self.send_command(0X02)
        self.send_command(0X07)
        self.send_data(0xA5)
        
    def exit(self):
        Ec_Paperconfig.module_exit()

