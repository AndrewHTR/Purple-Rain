from settings import *
from rain import *
from drops import *
from sound import *

running = True
start = int(time.time() * 1000.0)
time_limit = 2000
rains = []
drops = []
for i in range(800):
    rain = Rain()
    rains.append(rain)
    drop = Drops(rain.x, rain.z, rain.trans)
    drops.append(drop)

soundManager = Sound()

while running:
    seconds = int(time.time() * 1000.0)
    since_start = (seconds - start) + 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill('black')
    """if int(since_time) % 10 == 0:
        rain.fadeout(1)
        lightning.play()"""
    if (((int(since_start / 1000) + 1) % 10) == 0):
        soundManager.startTimer()

    for i in range(len(rains)):
        rains[i].update()
        rains[i].render()
        if rains[i].y > 580:
            drops[i].startTimer()

        drops[i].update()
        drops[i].render()

    soundManager.update()
            
    #display_fps(clock)
    draw_text("Andrew", (102, 51, 153), screen, 800/2, 600/2 - 20, alpha=40)
    pg.display.flip()

    clock.tick(60)

pg.quit()
