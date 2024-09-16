from settings import *

class Sound():
    def __init__(self):
        self.lightningSound = pg.mixer.Sound("./src/sounds/lightning.wav")
        self.lightningSound.set_volume(0.25)

        self.rainSound = pg.mixer.Sound("./src/sounds/rain.mp3")
        self.rainSound.set_volume(0.02)

        self.channel1 = pg.mixer.Channel(0)
        self.channel2 = pg.mixer.Channel(1)

        self.time = 0
        self.time_limit = 1000
        self.since_time = 0

        self.lightning = False

        self.m = 0

    def startTimer(self):
        now_time = int(time.time() * 1000.0)
        if self.time == 0:
            self.time = now_time

    def playRain(self):
        if self.m == 0:
            self.channel1.play(self.rainSound, -1)
            self.m = 1

    def playLightning(self):
        if self.lightning == True:
            self.channel2.play(self.lightningSound)
            self.lightning = False

    def update(self):
        self.playRain()
        self.playLightning()

        now_time = int(time.time() * 1000.0)

        if (self.time > 0):
            self.since_time = now_time - self.time

            if self.since_time < self.time_limit:
                self.lightning = True

            if self.since_time > self.time_limit:
                self.time = 0
                self.since_time = 0
                self.lightning = False
                