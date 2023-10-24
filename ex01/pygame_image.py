import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    bg_img1 = pg.image.load("ex01-20230926/fig/3.png")
    bg_img1 = pg.transform.flip(bg_img1, True, False)
    imglist = []
    for i in range(30):
        imglist.append(pg.transform.rotozoom(bg_img1, i*0.5, 1.0))
    for j in range(30, 0, -1):
        imglist.append(pg.transform.rotozoom(bg_img1, j*0.5, 1.0))
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img2, [1600-tmr, 0])
        screen.blit(bg_img, [3200-tmr, 0])
        num = tmr%60
        screen.blit(imglist[num], [300, 200])
        pg.display.update()
        tmr += 1
        if tmr >= 3199:
            tmr = 0        
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()