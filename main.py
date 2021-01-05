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
        if walking_jotaro:
            pg.time.set_timer(one_step_event, 500)
            self.rect.move(self.rect.x + 30, self.rect.y)
            x += 30

    def go_left(self):
        global x
        if walking_jotaro:
            pg.time.set_timer(one_step_event, 500)
            self.rect.move(self.rect.x - 30, self.rect.y)
            x -= 30


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Игра')
    size = width, height = 800, 600
    screen = pg.display.set_mode((size), pg.RESIZABLE)
    all_sprites = pg.sprite.Group()
    # Загружаем спрайты:
    jotaro_afk_right_side = [load_image('jotaro_afk1.png'), load_image('jotaro_afk2.png'),
                  load_image('jotaro_afk3.png'), load_image('jotaro_afk4.png'),
                  load_image('jotaro_afk5.png'), load_image('jotaro_afk6.png'),
                  load_image('jotaro_afk7.png'), load_image('jotaro_afk8.png')]
    jotaro_afk_left_side = [load_image('jotaro_afk1_other_side.png'),
                            load_image('jotaro_afk2_other_side.png'),
                            load_image('jotaro_afk3_other_side.png'),
                            load_image('jotaro_afk4_other_side.png'),
                            load_image('jotaro_afk5_other_side.png'),
                            load_image('jotaro_afk6_other_side.png'),
                            load_image('jotaro_afk7_other_side.png'),
                            load_image('jotaro_afk8_other_side.png')]
    jotaro_walking_right1 = [load_image('jotaro_walking_right1.png'),
                            load_image('jotaro_walking_right2.png'),
                            load_image('jotaro_walking_right3.png'),
                            load_image('jotaro_walking_right4.png'),
                            load_image('jotaro_walking_right5.png'),
                            load_image('jotaro_walking_right6.png'),
                            load_image('jotaro_walking_right7.png'),
                            load_image('jotaro_walking_right8.png')]
    jotaro_walking_right2 = [load_image('jotaro_walking_right9.png'),
                            load_image('jotaro_walking_right10.png'),
                            load_image('jotaro_walking_right11.png'),
                            load_image('jotaro_walking_right12.png'),
                            load_image('jotaro_walking_right13.png'),
                            load_image('jotaro_walking_right14.png'),
                            load_image('jotaro_walking_right15.png'),
                            load_image('jotaro_walking_right16.png')]
    jotaro_walking_left1 = [load_image('jotaro_walking_left1.png'),
                            load_image('jotaro_walking_left2.png'),
                            load_image('jotaro_walking_left3.png'),
                            load_image('jotaro_walking_left4.png'),
                            load_image('jotaro_walking_left5.png'),
                            load_image('jotaro_walking_left6.png'),
                            load_image('jotaro_walking_left7.png'),
                            load_image('jotaro_walking_left8.png')]
    jotaro_walking_left2 = [load_image('jotaro_walking_left9.png'),
                            load_image('jotaro_walking_left10.png'),
                            load_image('jotaro_walking_left11.png'),
                            load_image('jotaro_walking_left12.png'),
                            load_image('jotaro_walking_left13.png'),
                            load_image('jotaro_walking_left14.png'),
                            load_image('jotaro_walking_left15.png'),
                            load_image('jotaro_walking_left16.png')]
    one_step_event = pg.USEREVENT + 1
    pg.time.set_timer(one_step_event, 0)
    # Задаём координаты отрисовки спрайта в игровом окне:
    x, y = (0, 480)
    # Создаём экземпляр анимированного спрайта:
    sprite_jotaro = AnimaSprite(jotaro_afk_right_side, x, y)
    pg.key.set_repeat(20, 1)
    fps = 15
    true_side = True
    # count - переменная, которая считает, на какую ногу должен будет наступать персонаж
    # (0 - правая, 1 - левая)
    count = 0
    running = True
    walking_jotaro = False
    # Главный игровой цикл:
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and not walking_jotaro and x + 107 <= width:
                    sprite_jotaro.kill()
                    if count == 0:
                        sprite_walking_jotaro = AnimaSprite(jotaro_walking_right1, x, y)
                    elif count == 1:
                        sprite_walking_jotaro = AnimaSprite(jotaro_walking_right2, x, y)
                    if not true_side:
                        true_side = not true_side
                    walking_jotaro = True
                    count = (count + 1) % 2
                    sprite_walking_jotaro.go_right()
                elif event.key == pg.K_LEFT and not walking_jotaro and x - 30 >= 0:
                    sprite_jotaro.kill()
                    if count == 0:
                        sprite_walking_jotaro = AnimaSprite(jotaro_walking_left1, x, y)
                    elif count == 1:
                        sprite_walking_jotaro = AnimaSprite(jotaro_walking_left2, x, y)
                    if true_side:
                        true_side = not true_side
                    walking_jotaro = True
                    count = (count + 1) % 2
                    sprite_walking_jotaro.go_left()
            elif event.type == one_step_event:
                sprite_walking_jotaro.kill()
                pg.time.set_timer(one_step_event, 0)
                if true_side:
                    sprite_jotaro = AnimaSprite(jotaro_afk_right_side, x, y)
                elif not true_side:
                    sprite_jotaro = AnimaSprite(jotaro_afk_left_side, x, y)
                walking_jotaro = False
        screen.fill(pg.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()
        pg.display.flip()
        time.Clock().tick(fps)
    pg.quit()
