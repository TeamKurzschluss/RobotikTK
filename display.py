from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime


def wirteTextToDisplay(text, debug = 0):
    """
    Write a text to an E2C display.
    """
    
    textSplit = text.split()
    print(textSplit)
    
    i2c = I2C(0, scl=Pin(5), sda=Pin(4),  freq=200000)
    
    if debug == 1:
        print("debug : I2C Address      : "+hex(i2c.scan()[0]).upper()) 
        print("debug : I2C Configuration: "+str(i2c))
        
    oled = SSD1306_I2C(128, 64, i2c)
    oled.text(text,5,8)
    # oled.text(text, 10, 8)
    oled.show()
