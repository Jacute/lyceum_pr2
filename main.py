import pygame as pg


pg.init()
size = width, height = 1024, 768
screen = pg.display.set_mode(size)

pg.display.set_caption('Игра')

while pg.event.wait().type != pg.QUIT:
    pg.display.flip()

pg.quit()
