from settings import *

class Rain():
    def __init__(self):
        self.x = randint(0, 800)
        self.y = randint(-1800, -500)
        self.z = randint(0, 20)
        self.length = remap(self.z, 0, 20, 10, 20)
        self.yspd = remap(self.z, 0, 20, 0.5, 15)
        self.thick = remap(self.z, 0, 20, 1, 5)
        self.trans = (102, 51, 153, remap(self.z, 0, 20, 5, 230))
        self.surface = pg.display.get_surface()

    def fall(self):
        self.y += self.yspd 
        if self.y > 600:
            self.y = randint(-1400, 0)
            #self.x = randint(0, 800)
            self.yspd = remap(self.z, 0, 20, 0.5, 15)
            
    def render(self):
        self.rect = self.x, self.y, self.thick, self.length
        rain_surf = pg.Surface(pg.Rect(self.rect).size, pg.SRCALPHA)
        pg.draw.rect(rain_surf, self.trans, rain_surf.get_rect())
        self.surface.blit(rain_surf, self.rect)
         
    def update(self):
        self.fall()


