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
            x += 20

    def go_left(self):
        global x
        if walking_jotaro:
            pg.time.set_timer(one_step_event, 500)
            self.rect.move(self.rect.x - 30, self.rect.y)
            x -= 20

    def jump(self):
        global y
        if jumping_jotaro and not walking_jotaro:
            pg.time.set_timer(jump_event, 800)


class Hp_and_Mana(pg.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(hp_and_mana_sprites)
        self.image = sheet
        self.rect = self.image.get_rect().move(x, y)


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Игра')
    size = width, height = 800, 600
    screen = pg.display.set_mode((size))
    all_sprites, hp_and_mana_sprites = pg.sprite.Group(), pg.sprite.Group()
    # Загружаем спрайты:
    sprite_jotaro_afk_right_side = [load_image('jotaro_afk1.png'), load_image('jotaro_afk2.png'),
                  load_image('jotaro_afk3.png'), load_image('jotaro_afk4.png'),
                  load_image('jotaro_afk5.png'), load_image('jotaro_afk6.png'),
                  load_image('jotaro_afk7.png'), load_image('jotaro_afk8.png')]
    sprite_jotaro_afk_left_side = [load_image('jotaro_afk1_other_side.png'),
                            load_image('jotaro_afk2_other_side.png'),
                            load_image('jotaro_afk3_other_side.png'),
                            load_image('jotaro_afk4_other_side.png'),
                            load_image('jotaro_afk5_other_side.png'),
                            load_image('jotaro_afk6_other_side.png'),
                            load_image('jotaro_afk7_other_side.png'),
                            load_image('jotaro_afk8_other_side.png')]
    sprite_jotaro_walking_right1 = [load_image('jotaro_walking_right1.png'),
                            load_image('jotaro_walking_right2.png'),
                            load_image('jotaro_walking_right3.png'),
                            load_image('jotaro_walking_right4.png'),
                            load_image('jotaro_walking_right5.png'),
                            load_image('jotaro_walking_right6.png'),
                            load_image('jotaro_walking_right7.png'),
                            load_image('jotaro_walking_right8.png')]
    sprite_jotaro_walking_right2 = [load_image('jotaro_walking_right9.png'),
                            load_image('jotaro_walking_right10.png'),
                            load_image('jotaro_walking_right11.png'),
                            load_image('jotaro_walking_right12.png'),
                            load_image('jotaro_walking_right13.png'),
                            load_image('jotaro_walking_right14.png'),
                            load_image('jotaro_walking_right15.png'),
                            load_image('jotaro_walking_right16.png')]
    sprite_jotaro_walking_left1 = [load_image('jotaro_walking_left1.png'),
                            load_image('jotaro_walking_left2.png'),
                            load_image('jotaro_walking_left3.png'),
                            load_image('jotaro_walking_left4.png'),
                            load_image('jotaro_walking_left5.png'),
                            load_image('jotaro_walking_left6.png'),
                            load_image('jotaro_walking_left7.png'),
                            load_image('jotaro_walking_left8.png')]
    sprite_jotaro_walking_left2 = [load_image('jotaro_walking_left9.png'),
                            load_image('jotaro_walking_left10.png'),
                            load_image('jotaro_walking_left11.png'),
                            load_image('jotaro_walking_left12.png'),
                            load_image('jotaro_walking_left13.png'),
                            load_image('jotaro_walking_left14.png'),
                            load_image('jotaro_walking_left15.png'),
                            load_image('jotaro_walking_left16.png')]
    sprite_jotaro_jumping = [load_image('jotaro_jump1.png'), load_image('jotaro_jump2.png'),
                      load_image('jotaro_jump3.png'), load_image('jotaro_jump4.png'),
                      load_image('jotaro_jump5.png'), load_image('jotaro_jump6.png'),
                      load_image('jotaro_jump7.png'), load_image('jotaro_jump8.png'),
                      load_image('jotaro_jump9.png')]
    sprite_hp_and_mana_jotaro = load_image("hp_and_mana_jotaro.jpg")
    sprite_hp_and_mana_dio = load_image("hp_and_mana_dio.jpg")
    hp_and_mana_jotaro = Hp_and_Mana(sprite_hp_and_mana_jotaro, 0, 0)
    hp_and_mana_dio = Hp_and_Mana(sprite_hp_and_mana_dio, 499, 0)
    one_step_event, jump_event = pg.USEREVENT + 1, pg.USEREVENT + 1
    # Задаём координаты отрисовки спрайта в игровом окне:
    x, y = (0, 380)
    hp_jotaro, mana_jotaro = 100, 45
    # Создаём экземпляр анимированного спрайта:
    sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, x, y)
    pg.key.set_repeat(20, 1)
    fps = 12
    true_side = True
    # count - переменная, которая считает, на какую ногу должен будет наступать персонаж
    # (0 - правая, 1 - левая)
    count = 0
    running = True
    walking_jotaro, jumping_jotaro = False, False
    # Главный игровой цикл:
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and not walking_jotaro and x + 97 <= width:
                    sprite_jotaro.kill()
                    if count == 0:
                        walking_jotaro = AnimaSprite(sprite_jotaro_walking_right1, x, y)
                    elif count == 1:
                        walking_jotaro = AnimaSprite(sprite_jotaro_walking_right2, x, y)
                    if not true_side:
                        true_side = not true_side
                    walking_jotaro = True
                    count = (count + 1) % 2
                    walking_jotaro.go_right()
                elif event.key == pg.K_LEFT and not walking_jotaro and x - 20 >= 0:
                    sprite_jotaro.kill()
                    if count == 0:
                        walking_jotaro = AnimaSprite(sprite_jotaro_walking_left1, x, y)
                    elif count == 1:
                        walking_jotaro = AnimaSprite(sprite_jotaro_walking_left2, x, y)
                    if true_side:
                        true_side = not true_side
                    walking_jotaro = True
                    count = (count + 1) % 2
                    walking_jotaro.go_left()
                elif event.key == pg.K_UP and not walking_jotaro and not jumping_jotaro:
                    sprite_jotaro.kill()
                    jumping_jotaro = True
                    sprite_jumping_jotaro = AnimaSprite(sprite_jotaro_jumping, x, y)
                    sprite_jumping_jotaro.jump()
            elif event.type == one_step_event:
                walking_jotaro.kill()
                pg.time.set_timer(one_step_event, 0)
                if true_side:
                    sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, x, y)
                elif not true_side:
                    sprite_jotaro = AnimaSprite(sprite_jotaro_afk_left_side, x, y)
                walking_jotaro = False
            elif event.type == jump_event:
                jump_event.kill()
                pg.time.set_timer(jump_event, 0)
                if true_side:
                    sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, x, y)
                elif not true_side:
                    sprite_jotaro = AnimaSprite(sprite_jotaro_afk_left_side, x, y)
                jumping_jotaro = False
        screen.fill(pg.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()
        hp_and_mana_sprites.draw(screen)
        pg.draw.rect(screen, pg.Color('red'), (0, 21, hp_jotaro * 3, 5))
        pg.draw.rect(screen, pg.Color('blue'), (0, 26, mana_jotaro * 3, 5))
        pg.display.flip()
        time.Clock().tick(fps)
    pg.quit()
