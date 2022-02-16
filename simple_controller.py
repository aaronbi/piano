# libraries for controlling lights
from Controller import *

class SimpleController(Controller):

    def __init__(self, num_lights, color_on, color_off):
        Controller.__init__(self, num_lights, color_on, color_off)


    def process_event(self, event):
        message, deltatime = event
        state = message[0]
        print(message, deltatime)
        Controller.process_event(self, state)
