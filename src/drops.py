from settings import *

class Drops():
    def __init__(self, x, z, trans):
        # Basic attributes
        self.x = x
        self.yy = 595
        self.z = z
        self.trans = trans
        self.surface = pg.display.get_surface()
        self.limit = 580
        
        # Timer for animation
        self.ani = False
        self.time = 0
        self.time_limit = remap(self.z, 0, 20, 50, 150)
        self.since_time = 0

    def startTimer(self):
        now_time = int(time.time() * 1000.0)
        if self.time == 0:
            self.time = now_time

    def animate(self):
        if self.ani == True:
            self.yy -= 3
            if self.z >= 15:
                self.rect = self.x, self.yy, 7, 7
                rain_surf = pg.Surface(pg.Rect(self.rect).size, pg.SRCALPHA)
                pg.draw.rect(rain_surf, self.trans, rain_surf.get_rect())
                self.surface.blit(rain_surf, self.rect)
        elif self.ani == False:
            self.yy = 600
            
    def render(self):
        self.animate()

    def update(self):
        now_time = int(time.time() * 1000.0)
        if (self.time > 0):
            self.since_time = now_time - self.time

            if self.since_time < self.time_limit and self.since_time != 0:
                self.ani = True

            if self.since_time > self.time_limit:
                self.time = 0
                self.since_time = 0
                self.ani = False