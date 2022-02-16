# libraries for controlling lights
import board
import neopixel
from Controller import *

class SimpleController(Controller):

    def __init__(self, num_lights, color_on, color_off):
        Controller.__init__(self, num_lights, color_on, color_off)


    def process_event(self, event):
        message, deltatime = event
        state = message[0]
        print(message, deltatime)
        if state == SimpleController.DOWN:
            self.pixels[self.next_light % self.num_lights] = self.color_on
            self.next_light+=1
        else:
            self.pixels[self.prev_light % self.num_lights] = self.color_off
            self.prev_light+=1
