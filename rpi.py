import pigpio


class raspi:
    # gpiostate = 0
    def __init__(self):
        self.pi = pigpio.pi()
        self.pi.set_mode(12, pigpio.OUTPUT)



    def togglegpio(self, state):

        state ^= 1
        self.pi.write(12, state)
        return self.pi.read(12)

    def readgpio(self):
        return self.pi.read(12)