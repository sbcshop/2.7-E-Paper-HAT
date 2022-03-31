import time
# Display resolution
image_width       = 176
image_height      = 264


class epaper:
    # GPIO Pins definition
    RST_PIN         = 17
    DC_PIN          = 25
    CS_PIN          = 8
    BUSY_PIN        = 24

    def __init__(self):
        import spidev
        import RPi.GPIO

        self.GPIO = RPi.GPIO

        self.SPI = spidev.SpiDev(0, 0)

    def digitalwrite(self, pin, value):
        self.GPIO.output(pin, value)

    def digitalread(self, pin):
        return self.GPIO.input(pin)

    def delay(self, delaytime): # delay in millisecond
        time.sleep(delaytime / 1000.0)

    def spi_writebyte(self, data):
        self.SPI.writebytes(data)

    def module_init(self):
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
        self.GPIO.setup(self.RST_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.DC_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.CS_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.BUSY_PIN, self.GPIO.IN)
        self.SPI.max_speed_hz = 4000000
        self.SPI.mode = 0b00
        return 0

    def exit(self):
        self.SPI.close()
        self.GPIO.output(self.RST_PIN, 0)
        self.GPIO.output(self.DC_PIN, 0)
        self.GPIO.cleanup()
 
e_paper_config = epaper()
class E_Paper:
    def __init__(self):
        self.reset_pin = e_paper_config.RST_PIN
        self.dc_pin = e_paper_config.DC_PIN
        self.busy_pin = e_paper_config.BUSY_PIN
        self.cs_pin = e_paper_config.CS_PIN
        self.width = image_width
        self.height = image_height

    lut_vcom_dc = [0x00, 0x00,
        0x00, 0x08, 0x00, 0x00, 0x00, 0x02,
        0x60, 0x28, 0x28, 0x00, 0x00, 0x01,
        0x00, 0x14, 0x00, 0x00, 0x00, 0x01,
        0x00, 0x12, 0x12, 0x00, 0x00, 0x01,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ]
    lut_ww = [
        0x40, 0x08, 0x00, 0x00, 0x00, 0x02,
        0x90, 0x28, 0x28, 0x00, 0x00, 0x01,
        0x40, 0x14, 0x00, 0x00, 0x00, 0x01,
        0xA0, 0x12, 0x12, 0x00, 0x00, 0x01,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ]
    lut_bw = [
        0x40, 0x08, 0x00, 0x00, 0x00, 0x02,
        0x90, 0x28, 0x28, 0x00, 0x00, 0x01,
        0x40, 0x14, 0x00, 0x00, 0x00, 0x01,
        0xA0, 0x12, 0x12, 0x00, 0x00, 0x01,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ]
    lut_bb = [
        0x80, 0x08, 0x00, 0x00, 0x00, 0x02,
        0x90, 0x28, 0x28, 0x00, 0x00, 0x01,
        0x80, 0x14, 0x00, 0x00, 0x00, 0x01,
        0x50, 0x12, 0x12, 0x00, 0x00, 0x01,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ]
    lut_wb = [
        0x80, 0x08, 0x00, 0x00, 0x00, 0x02,
        0x90, 0x28, 0x28, 0x00, 0x00, 0x01,
        0x80, 0x14, 0x00, 0x00, 0x00, 0x01,
        0x50, 0x12, 0x12, 0x00, 0x00, 0x01,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ]
    # Hardware reset
    def reset(self):
        e_paper_config.digitalwrite(self.reset_pin, 1)
        e_paper_config.delay(200) 
        e_paper_config.digitalwrite(self.reset_pin, 0)
        e_paper_config.delay(10)
        e_paper_config.digitalwrite(self.reset_pin, 1)
        e_paper_config.delay(200)   

    def send_data(self, data):
        e_paper_config.digitalwrite(self.dc_pin, 1)
        e_paper_config.digitalwrite(self.cs_pin, 0)
        e_paper_config.spi_writebyte([data])
        e_paper_config.digitalwrite(self.cs_pin, 1)
        
    def send_command(self, command):
        e_paper_config.digitalwrite(self.dc_pin, 0)
        e_paper_config.digitalwrite(self.cs_pin, 0)
        e_paper_config.spi_writebyte([command])
        e_paper_config.digitalwrite(self.cs_pin, 1)


        
    def ReadBusy(self):        
        while(e_paper_config.digitalread(self.busy_pin) == 0):      #  0: idle, 1: busy
            e_paper_config.delay(200)                

    def set_lut(self):
        self.send_command(0x20) # vcom
        for count in range(0, 44):
            self.send_data(self.lut_vcom_dc[count])
        self.send_command(0x21) # ww --
        for count in range(0, 42):
            self.send_data(self.lut_ww[count])
        self.send_command(0x22) # bw r
        for count in range(0, 42):
            self.send_data(self.lut_bw[count])
        self.send_command(0x23) # wb w
        for count in range(0, 42):
            self.send_data(self.lut_bb[count])
        self.send_command(0x24) # bb b
        for count in range(0, 42):
            self.send_data(self.lut_wb[count])

    def init(self):
        if (e_paper_config.module_init() != 0):
            return -1
            
        # E_Paper hardware init start
        self.reset()
        
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
        
        # Power optimization ##############
        self.send_command(0xF8)
        self.send_data(0x60)
        self.send_data(0xA5)      

        self.send_command(0xF8)
        self.send_data(0xA1)
        self.send_data(0x00)
        ####################################

    
        self.send_command(0x16) # PARTIAL_DISPLAY_REFRESH
        self.send_data(0x00)
        self.send_command(0x04) # POWER_ON
        self.ReadBusy()

        self.send_command(0x00) # PANEL_SETTING
        self.send_data(0xAF)    # KW-BF   KWR-AF    BWROTP 0f
        
        self.send_command(0x30) # PLL_CONTROL
        self.send_data(0x3A)    # 3A 100HZ   29 150Hz 39 200HZ    31 171HZ
        
        self.send_command(0x82) # VCM_DC_SETTING_REGISTER
        self.send_data(0x12)
        self.set_lut()
        return 0

    def buffer(self, image):
        # logging.debug("bufsiz = ",int(self.width/8) * self.height)
        buf = [0xFF] * (int(self.width/8) * self.height)
        image_monocolor = image.convert('1')
        image_width, image_height = image_monocolor.size
        pixels = image_monocolor.load()
        # logging.debug("image_width = %d, image_height = %d",image_width,image_height)
        if(image_width == self.width and image_height == self.height):
            for y in range(image_height):
                for x in range(image_width):
                    # Set the bits for the column of pixels at the current position.
                    if pixels[x, y] == 0:
                        buf[int((x + y * self.width) / 8)] &= ~(0x80 >> (x % 8))
        elif(image_width == self.height and image_height == self.width):
            for y in range(image_height):
                for x in range(image_width):
                    newx = y
                    newy = self.height - x - 1
                    if pixels[x, y] == 0:
                        buf[int((newx + newy*self.width) / 8)] &= ~(0x80 >> (y % 8))
        return buf

    def display(self, image):
        self.send_command(0x10)
        for i in range(0, int(self.width * self.height / 8)):
            self.send_data(0xFF)
        self.send_command(0x13)
        for i in range(0, int(self.width * self.height / 8)):
            self.send_data(image[i])
        self.send_command(0x12) 
        self.ReadBusy()

    def clear_screen(self, color):
        self.send_command(0x10)
        for i in range(0, int(self.width * self.height / 8)):
            self.send_data(0xFF)
        self.send_command(0x13)
        for i in range(0, int(self.width * self.height / 8)):
            self.send_data(0xFF)
        self.send_command(0x12) 
        self.ReadBusy()

    def sleep(self):
        self.send_command(0X50)
        self.send_data(0xf7)
        self.send_command(0X02)
        self.send_command(0X07)
        self.send_data(0xA5)
        
    def exit(self):
        e_paper_config.exit()


