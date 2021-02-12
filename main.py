import os
import pygame as pg
from pygame import time
from load_sprites import *
import time as tm


flag_walking_jotaro, flag_jumping_jotaro, flag_sitting_jotaro, flag_attacking_jotaro = False, False, False, False


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
    def __init__(self, sheet, hero, x, y):
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
        global x_jotaro
        pg.time.set_timer(one_step_event, 620)
        self.rect.move(self.rect.x + 20, self.rect.y)
        x_jotaro += 20

    def go_left(self):
        global x_jotaro
        pg.time.set_timer(one_step_event, 620)
        self.rect.move(self.rect.x - 20, self.rect.y)
        x_jotaro -= 20

    def jump(self):
        pg.time.set_timer(jump_event, 1695)

    def start_sitting(self):
        pg.time.set_timer(start_sitting_event, 310)

    def stand_up(self):
        pg.time.set_timer(stand_up_event, 772)

    def attack(self):
        pg.time.set_timer(attack_event, 620)


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
    hp_and_mana_jotaro = Hp_and_Mana(sprite_hp_and_mana_jotaro, 0, 0)
    hp_and_mana_dio = Hp_and_Mana(sprite_hp_and_mana_dio, 499, 0)
    one_step_event = pg.USEREVENT + 1
    jump_event = pg.USEREVENT + 2
    start_sitting_event = pg.USEREVENT + 3
    stand_up_event = pg.USEREVENT + 4
    attack_event = pg.USEREVENT + 5
    # Задаём координаты отрисовки спрайта в игровом окне:
    x_jotaro, y_jotaro, x_dio, y_dio = (0, 380, 735, 380)
    hp_jotaro, mana_jotaro, hp_dio, mana_dio = 100, 45, 100, 45
    # Создаём экземпляр анимированного спрайта:
    sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, 'jotaro', x_jotaro, y_jotaro)
    sprite_dio = AnimaSprite(sprite_dio_afk_right_side, 'dio', x_dio, y_dio)
    pg.key.set_repeat(1, 10)
    fps = 13
    # count - переменная, которая считает, на какую ногу должен будет наступать персонаж
    # (0 - правая, 1 - левая)
    count = 0
    running = True
    # Главный игровой цикл:
    while running:
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d and not flag_walking_jotaro and x_jotaro + 97 <= width\
                        and not flag_jumping_jotaro and not flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    if count == 0:
                        sprite_jotaro = AnimaSprite(sprite_jotaro_walking_right1, 'jotaro', x_jotaro, y_jotaro)
                    elif count == 1:
                        sprite_jotaro = AnimaSprite(sprite_jotaro_walking_right2, 'jotaro', x_jotaro, y_jotaro)
                    flag_walking_jotaro = True
                    count = (count + 1) % 2
                    sprite_jotaro.go_right()
                elif event.key == pg.K_a and not flag_walking_jotaro and x_jotaro - 20 >= 0\
                        and not flag_jumping_jotaro and not flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    if count == 0:
                        sprite_jotaro = AnimaSprite(sprite_jotaro_walking_left1, 'jotaro', x_jotaro, y_jotaro)
                    elif count == 1:
                        sprite_jotaro = AnimaSprite(sprite_jotaro_walking_left2, 'jotaro', x_jotaro, y_jotaro)
                    flag_walking_jotaro = True
                    count = (count + 1) % 2
                    sprite_jotaro.go_left()
                elif event.key == pg.K_w and not flag_walking_jotaro and not flag_jumping_jotaro and not flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    flag_jumping_jotaro = True
                    sprite_jotaro = AnimaSprite(sprite_jotaro_jumping, 'jotaro', x_jotaro, y_jotaro)
                    sprite_jotaro.jump()
                elif event.key == pg.K_s and not flag_walking_jotaro and not flag_jumping_jotaro and not flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    flag_sitting_jotaro = True
                    sprite_jotaro = AnimaSprite(sprite_jotaro_start_sitting, 'jotaro', x_jotaro, y_jotaro)
                    sprite_jotaro.start_sitting()
                elif event.key == pg.K_l and not flag_walking_jotaro and not flag_jumping_jotaro and not flag_sitting_jotaro and not flag_attacking_jotaro:
                    sprite_jotaro.kill()
                    flag_attacking_jotaro = True
                    sprite_jotaro = AnimaSprite(sprite_jotaro_light_attack, 'jotaro', x_jotaro, y_jotaro)
                    sprite_jotaro.attack()
                elif event.key == pg.K_l and not flag_walking_jotaro and not flag_jumping_jotaro and not flag_attacking_jotaro and flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    flag_attacking_jotaro = True
                    sprite_jotaro = AnimaSprite(sprite_jotaro_sitting_light_attack, 'jotaro', x_jotaro, y_jotaro)
                    sprite_jotaro.attack()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_s and flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    sprite_jotaro = AnimaSprite(sprite_jotaro_end_sitting, 'jotaro', x_jotaro, y_jotaro)
                    sprite_jotaro.stand_up()
            elif event.type == one_step_event:
                sprite_jotaro.kill()
                pg.time.set_timer(one_step_event, 0)
                sprite_jotaro.kill()
                sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, 'jotaro', x_jotaro, y_jotaro)
                flag_walking_jotaro = False
            elif event.type == jump_event:
                sprite_jotaro.kill()
                pg.time.set_timer(jump_event, 0)
                sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, 'jotaro', x_jotaro, y_jotaro)
                flag_jumping_jotaro = False
            elif event.type == start_sitting_event:
                sprite_jotaro.kill()
                pg.time.set_timer(start_sitting_event, 0)
                sprite_jotaro = AnimaSprite(sprite_jotaro_sitting, 'jotaro', x_jotaro, y_jotaro)
            elif event.type == stand_up_event:
                sprite_jotaro.kill()
                pg.time.set_timer(stand_up_event, 0)
                sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, 'jotaro', x_jotaro, y_jotaro)
                flag_sitting_jotaro = False
            elif event.type == attack_event:
                sprite_jotaro.kill()
                pg.time.set_timer(attack_event, 0)
                sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, 'jotaro', x_jotaro, y_jotaro)
                flag_attacking_jotaro = False
        screen.fill(pg.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()
        hp_and_mana_sprites.draw(screen)
        # Отрисовка здоровья и маны
        pg.draw.rect(screen, pg.Color('red'), (0, 21, hp_jotaro * 3, 5))
        pg.draw.rect(screen, pg.Color('blue'), (0, 26, mana_jotaro * 3, 5))
        pg.draw.rect(screen, pg.Color('red'), (800 - hp_dio * 3, 21, 800, 5))
        pg.draw.rect(screen, pg.Color('blue'), (800 - mana_dio * 3, 26, 800, 5))
        pg.display.flip()
        time.Clock().tick(fps)
    pg.quit()
