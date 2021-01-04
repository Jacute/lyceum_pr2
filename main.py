import os
import pygame as pg
from pygame import time


def load_image(name):
    """Функция загрузки изображения из файла"""
    filename = os.path.join('data', name)
    try:
        image = pg.image.load(filename)
    except pg.error as error:
        print('Не могу загрузить изображение:', name)
        raise SystemExit(error)
    return image


class AnimaSprite(pg.sprite.Sprite):
    """Анимированный спрайт"""
    def __init__(self, sheet, x, y):
        super().__init__(all_sprites)
        # frames - атрибут класса,
        # список для хранения последовательности кадров спрайта:
        self.frames = sheet
        # Обнуляем номер текущего кадра:
        self.cur_frame = 0
        # image - атрибут класса,
        # в который помещаем текущий кадр:
        self.image = self.frames[self.cur_frame]
        # Помещаем прямоугольник с кадром в координаты (x, y):
        self.rect = self.image.get_rect().move(x, y)

    def update(self):
        """Смена кадра спрайта"""
        # Переключаемся на номер следующего кадра,
        # но так, чтобы не выйти за границы списка frames.
        # Для этого закольцовываем счёт кадров при помощи операции %:
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        # Меняем кадр - помещаем новый кадр в атрибут image:
        self.image = self.frames[self.cur_frame]

    def go_right(self):
        global x
        if walking:
            self.rect.move(self.rect.x + 30, self.rect.y)
            x += 30
            pg.time.set_timer(one_step_event, 450)

    def go_left(self):
        global x
        if walking:
            self.rect.move(self.rect.x - 30, self.rect.y)
            x -= 30
            pg.time.set_timer(one_step_event, 450)


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Игра')
    size = width, height = 300, 300
    screen = pg.display.set_mode((size), pg.RESIZABLE)
    all_sprites = pg.sprite.Group()
    # Загружаем спрайты
    jotaro_afk = [load_image('jotaro_afk1.png'), load_image('jotaro_afk2.png'),
                  load_image('jotaro_afk3.png'), load_image('jotaro_afk4.png'),
                  load_image('jotaro_afk5.png'), load_image('jotaro_afk6.png'),
                  load_image('jotaro_afk7.png'), load_image('jotaro_afk8.png')]
    one_step_event = pg.USEREVENT + 1
    pg.time.set_timer(one_step_event, 0)
    # Задаём координаты отрисовки спрайта в игровом окне:
    x, y = (0, 0)
    # Создаём экземпляр анимированного спрайта:
    sprite_jotaro = AnimaSprite(jotaro_afk, x, y)
    pg.key.set_repeat(200, 10)
    fps = 15
    running = True
    walking = False
    # Главный игровой цикл:
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            '''elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and not walking:
                    sprite_jotaro.kill()
                    sprite_walking_jotaro = AnimaSprite(walking_jotaro_right, 16, 1, x, y)
                    walking = True
                    sprite_walking_jotaro.go_right()
                elif event.key == pg.K_LEFT and not walking:
                    sprite_jotaro.kill()
                    sprite_walking_jotaro = AnimaSprite(walking_jotaro_left, 16, 1, x, y)
                    walking = True
                    sprite_walking_jotaro.go_left()
            elif event.type == one_step_event:
                sprite_walking_jotaro.kill()
                pg.time.set_timer(one_step_event, 0)
                sprite_jotaro = AnimaSprite(sheet_jotaro, 20, 1, x, y)
                walking = False'''
        screen.fill(pg.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()
        pg.display.flip()
        time.Clock().tick(fps)
    pg.quit()
