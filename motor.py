import machine
import utime

MOT_A = 1
MOT_B = 2
MOT_AB = 3
ain1 = machine.Pin(10, machine.Pin.OUT)
ain2 = machine.Pin(11, machine.Pin.OUT)
bin1 = machine.Pin(12, machine.Pin.OUT)
bin2 = machine.Pin(13, machine.Pin.OUT)
pwma = machine.PWM(machine.Pin(14))
pwma.freq(1000)
pwmb = machine.PWM(machine.Pin(15))
pwmb.freq(1000)

class Motor:
    def __init__(self, motor):
        
        # init main var
        self.motor = motor

        # standart Motor Werte
        self.motA = 1
        self.motB = 2
        self.motAB = 3

        # init motor pins
        self.ain1 = machine.Pin(10, machine.Pin.OUT)
        self.ain2 = machine.Pin(11, machine.Pin.OUT)
        self.bin1 = machine.Pin(12, machine.Pin.OUT)
        self.bin2 = machine.Pin(13, machine.Pin.OUT)
        
        # pwma / pwmb
        self.pwma = machine.PWM(machine.Pin(14))
        self.pwmb = machine.PWM(machine.Pin(15))
        
        self.pwma.freq(1000)
        self.pwmb.freq(1000)

    def onForward(self, V):
        '''
        lässt den Robotor mit einer gegebenen Geschindigkeit vorwärtz fahren
        '''
        
        # setzt die Geschwindigkeit ins Positive, auch wenn sie Negativ ist,
        # da der Roboter nur mit Positiven Werten zurechtkommt
        if V < 0:
            pwm_val = -V
        else:
            pwm_val = V
        
        # ?
        pwm_val = 650*pwm_val

        # setzt die Motoren auf die richtige Richtung
        if self.motor == self.motA:
            if V > 0:
                self.ain1.off()
                self.ain2.on()
            else:
                self.ain1.on()
                self.ain2.off()
            self.pwma.duty_u16(pwm_val)
            
        if self.motor == self.motB:
            if V > 0:
                self.bin1.off()
                self.bin2.on()
            else:
                self.bin1.on()
                self.bin2.off()
            self.pwmb.duty_u16(pwm_val)
            
    def onReverse(self, V):
        '''
        lässt den Roboter mit einer gegebenen Geschwindigkeit zurückfahren
        '''
        
        onForward(-V)
        
    def off(self):
        '''
        stop the motor
        '''
        
        if self.motor == self.motA:
            self.pwma.duty
        
def OnFwd(mot, V):
    if V < 0:
        pwm_val = -V
    else:
        pwm_val = V
        
    if (pwm_val>100):
        pwm_val=100
        
    pwm_val = 650*pwm_val        
        
    if mot & MOT_A:
        if V > 0:
            ain1.off()
            ain2.on()
        else:
            ain1.on()
            ain2.off() 
        pwma.duty_u16(pwm_val)
        
    if mot & MOT_B:
        if V > 0:
            bin1.off()
            bin2.on()
        else:
            bin1.on()
            bin2.off()
        pwmb.duty_u16(pwm_val)

def OnRev(mot, V):
    OnFwd(mot, -V)

def Off(mot):
    if mot & MOT_A:
        pwma.duty_u16(0)
        
    if mot & MOT_B:
        pwmb.duty_u16(0)

    
#OnFwd(MOT_AB,100)
#utime.sleep(1)
#Off(MOT_AB)
