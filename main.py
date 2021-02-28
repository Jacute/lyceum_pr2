import os
import pygame as pg
from pygame import time
from load_sprites import *


def load_image(name):
    """Функция загрузки изображения из файла"""
    filename = os.path.join('data', name)
    try:
        image = pg.image.load(filename)
    except pg.error as error:
        print('Не могу загрузить изображение:', name)
        raise SystemExit(error)
    return image


'''class AnimaSprite(pg.sprite.Sprite):
    """Анимированный спрайт"""
    def __init__(self, sheet, hero, x, y):
        super().__init__(all_sprites)
        self.hero = hero
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
        global x_dio, x_jotaro, flag_stop_jotaro
        if self.hero == 'jotaro':
            if x_dio > x_jotaro:
                pg.time.set_timer(jotaro_one_step_event, 630)
                self.rect.move(self.rect.x + 20, self.rect.y)
                x_jotaro += 20
            else:
                pg.time.set_timer(jotaro_one_step_event, 630)
                flag_stop_jotaro = True
        else:
            pg.time.set_timer(dio_one_step_event, 630)
            self.rect.move(self.rect.x + 20, self.rect.y)
            x_dio += 20

    def go_left(self):
        global x_dio, x_jotaro, flag_stop_dio
        if self.hero == 'jotaro':
            pg.time.set_timer(jotaro_one_step_event, 630)
            self.rect.move(self.rect.x - 20, self.rect.y)
            x_jotaro -= 20
        else:
            if x_jotaro < x_dio:
                pg.time.set_timer(dio_one_step_event, 630)
                self.rect.move(self.rect.x - 20, self.rect.y)
                x_dio -= 20
            else:
                pg.time.set_timer(dio_one_step_event, 630)
                flag_stop_dio = True

    def jump(self):
        if self.hero == 'jotaro':
            pg.time.set_timer(jotaro_jump_event, 1695)
        else:
            pg.time.set_timer(dio_jump_event, 930)

    def start_sitting(self):
        if self.hero == 'jotaro':
            pg.time.set_timer(jotaro_start_sitting_event, 310)
        else:
            pg.time.set_timer(dio_start_sitting_event, 235)

    def stand_up(self):
        if self.hero == 'jotaro':
            pg.time.set_timer(jotaro_stand_up_event, 772)
        else:
            pg.time.set_timer(dio_stand_up_event, 235)

    def light_attack(self):
        # Все лёгкие атаки Джотаро должны быть в 8 спрайтов
        if self.hero == 'jotaro':

        # Все лёгкие атаки Дио должны быть в 5 спрайтов
        else:
            pg.time.set_timer(dio_light_attack_event, 400)

    def block(self):
        if self.hero == 'jotaro':
            pg.time.set_timer(jotaro_start_blocking_event, 230)
        else:
            pg.time.set_timer(dio_start_blocking_event, 230)

    def end_blocking(self):
        if self.hero == 'jotaro':
            pg.time.set_timer(jotaro_end_blocking_event, 700)
        else:
            pass'''


class HpandMana(pg.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(hp_and_mana_sprites)
        self.image = sheet
        self.rect = self.image.get_rect().move(x, y)


class Dio(pg.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(all_sprites)
        ''' Ивенты Дио '''
        self.one_step_event, self.jump_event, self.start_sitting_event, self.stand_up_event, \
        self.light_attack_event, self.start_blocking_event, self.end_blocking_event = pg.USEREVENT + 9, \
                                                                                      pg.USEREVENT + 10, pg.USEREVENT + 11, pg.USEREVENT + 12, pg.USEREVENT + 13, pg.USEREVENT + 14, pg.USEREVENT + 15
        ''' Конец Ивентов '''
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
        global x_dio
        pg.time.set_timer(self.one_step_event, 630)
        self.rect.move(self.rect.x + 20, self.rect.y)
        x_dio += 20

    def go_left(self):
        global x_dio
        pg.time.set_timer(self.one_step_event, 630)
        self.rect.move(self.rect.x - 20, self.rect.y)
        x_dio -= 20

    def jump(self):
        pg.time.set_timer(self.jump_event, 930)

    def start_sitting(self):
        pg.time.set_timer(self.start_sitting_event, 235)

    def stand_up(self):
        pg.time.set_timer(self.stand_up_event, 235)

    def light_attack(self):
        pg.time.set_timer(self.light_attack_event, 400)


class Jotaro(pg.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(all_sprites)
        ''' Ивенты Джотаро '''
        self.one_step_event, self.jump_event, self.start_sitting_event, self.stand_up_event, \
        self.light_attack_event, self.start_blocking_event, self.end_blocking_event = pg.USEREVENT + 1, \
                                                                                      pg.USEREVENT + 2, pg.USEREVENT + 3, pg.USEREVENT + 4, pg.USEREVENT + 5, pg.USEREVENT + 6, pg.USEREVENT + 7
        ''' Конец Ивентов '''
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
        pg.time.set_timer(self.one_step_event, 630)
        self.rect.move(self.rect.x + 20, self.rect.y)
        x_jotaro += 20

    def go_left(self):
        global x_jotaro
        pg.time.set_timer(self.one_step_event, 630)
        self.rect.move(self.rect.x - 20, self.rect.y)
        x_jotaro -= 20

    def jump(self):
        pg.time.set_timer(self.jump_event, 1695)

    def start_sitting(self):
        pg.time.set_timer(self.start_sitting_event, 310)

    def stand_up(self):
        pg.time.set_timer(self.stand_up_event, 772)

    def light_attack(self):
        pg.time.set_timer(self.light_attack_event, 630)


if __name__ == '__main__':
    # Инициализируем pygame
    pg.init()
    pg.display.set_caption('Jotaro VS Dio')
    # Задаём размер окна
    size = width, height = 800, 600
    # Создаём окно
    screen = pg.display.set_mode(size)
    # Создаём группы спрайтов
    all_sprites, hp_and_mana_sprites = pg.sprite.Group(), pg.sprite.Group()
    # Задаём спрайты шкал хп и маны
    hp_and_mana_jotaro = HpandMana(sprite_hp_and_mana_jotaro, 0, 0)
    hp_and_mana_dio = HpandMana(sprite_hp_and_mana_dio, 499, 0)
    # Задаём координаты отрисовки спрайтов в игровом окне:
    x_jotaro, y_jotaro, x_dio, y_dio = (0, 380, 660, 356)
    # Задаём кол-во хп и маны у персонажей
    hp_jotaro, mana_jotaro, hp_dio, mana_dio = 100, 30, 100, 30
    # Задаём флаги событий персонажей
    flag_walking_jotaro, flag_jumping_jotaro, flag_sitting_jotaro, flag_attacking_jotaro, flag_blocking_jotaro = \
        False, False, False, False, False
    flag_walking_dio, flag_jumping_dio, flag_sitting_dio, flag_attacking_dio, flag_blocking_dio = \
        False, False, False, False, False
    # Создаём экземпляры анимированных спрайтов:
    sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
    sprite_dio = Dio(sprite_dio_afk_left_side, x_dio, y_dio)
    # Задаём повтор клавиш
    pg.key.set_repeat(1, 10)
    # Задаём fps
    fps = 13
    # count - переменная, которая считает, на какую ногу должен будет наступать персонаж
    # (0 - правая, 1 - левая)
    count_jotaro, count_dio = 0, 0
    running = True
    # Главный игровой цикл:
    while running:
        if x_jotaro < x_dio:
            flag_stop_jotaro = False
            flag_stop_dio = False
        elif hp_jotaro <= 0 or hp_dio <= 0:
            end = True
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            flags_jotaro = {flag_walking_jotaro, flag_jumping_jotaro, flag_sitting_jotaro, flag_attacking_jotaro}
            flags_dio = {flag_jumping_dio, flag_sitting_dio, flag_attacking_dio, flag_walking_dio}
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                # Обработка клавиш для Джотаро
                if keys[pg.K_d] and x_jotaro + 97 <= width and not any(flags_jotaro):
                    sprite_jotaro.kill()
                    if count_jotaro == 0:
                        sprite_jotaro = Jotaro(sprite_jotaro_walking_right1, x_jotaro, y_jotaro)
                    elif count_jotaro == 1:
                        sprite_jotaro = Jotaro(sprite_jotaro_walking_right2, x_jotaro, y_jotaro)
                    flag_walking_jotaro = True
                    count_jotaro = (count_jotaro + 1) % 2
                    sprite_jotaro.go_right()
                elif keys[pg.K_a] and x_jotaro - 20 >= 0 and not any(flags_jotaro):
                    sprite_jotaro.kill()
                    if count_jotaro == 0:
                        sprite_jotaro = Jotaro(sprite_jotaro_walking_left1, x_jotaro, y_jotaro)
                    elif count_jotaro == 1:
                        sprite_jotaro = Jotaro(sprite_jotaro_walking_left2, x_jotaro, y_jotaro)
                    flag_walking_jotaro = True
                    count_jotaro = (count_jotaro + 1) % 2
                    sprite_jotaro.go_left()
                elif keys[pg.K_w] and not any(flags_jotaro):
                    sprite_jotaro.kill()
                    flag_jumping_jotaro = True
                    sprite_jotaro = Jotaro(sprite_jotaro_jumping, x_jotaro, y_jotaro)
                    sprite_jotaro.jump()
                elif keys[pg.K_s] and not any(flags_jotaro):
                    sprite_jotaro.kill()
                    flag_sitting_jotaro = True
                    sprite_jotaro = Jotaro(sprite_jotaro_start_sitting, x_jotaro, y_jotaro)
                    sprite_jotaro.start_sitting()
                elif keys[pg.K_l] and not any(flags_jotaro):
                    sprite_jotaro.kill()
                    flag_attacking_jotaro = True
                    sprite_jotaro = Jotaro(sprite_jotaro_light_attack, x_jotaro, y_jotaro)
                    sprite_jotaro.light_attack()
                elif keys[pg.K_l] and flag_sitting_jotaro and not flag_attacking_jotaro:
                    sprite_jotaro.kill()
                    flag_attacking_jotaro = True
                    sprite_jotaro = Jotaro(sprite_jotaro_sitting_light_attack, x_jotaro, y_jotaro)
                    sprite_jotaro.light_attack()

                # Обработка клавиш для Дио
                elif keys[pg.K_LEFT] and not any(flags_dio) and x_dio + 20 >= 0:
                    sprite_dio.kill()
                    if count_dio == 0:
                        sprite_dio = Dio(sprite_dio_walking_left1, x_dio, y_dio)
                    elif count_dio == 1:
                        sprite_dio = Dio(sprite_dio_walking_left2, x_dio, y_dio)
                    flag_walking_dio = True
                    count_dio = (count_dio + 1) % 2
                    sprite_dio.go_left()
                elif keys[pg.K_RIGHT] and not any(flags_dio) and x_dio + 150 <= width:
                    sprite_dio.kill()
                    if count_dio == 0:
                        sprite_dio = Dio(sprite_dio_walking_right1, x_dio, y_dio)
                    elif count_dio == 1:
                        sprite_dio = Dio(sprite_dio_walking_right2, x_dio, y_dio)
                    flag_walking_dio = True
                    count_dio = (count_dio + 1) % 2
                    sprite_dio.go_right()
                elif keys[pg.K_UP] and not any(flags_dio):
                    sprite_dio.kill()
                    flag_jumping_dio = True
                    sprite_dio = Dio(sprite_dio_jumping, x_dio, y_dio)
                    sprite_dio.jump()
                elif keys[pg.K_DOWN] and not any(flags_dio):
                    sprite_dio.kill()
                    flag_sitting_dio = True
                    sprite_dio = Dio(sprite_dio_start_sitting, x_dio, y_dio)
                    sprite_dio.start_sitting()
                elif keys[pg.K_KP7] and not any(flags_dio):
                    sprite_dio.kill()
                    flag_attacking_dio = True
                    sprite_dio = Dio(sprite_dio_light_attack, x_dio, y_dio)
                    sprite_dio.light_attack()
                elif keys[pg.K_KP7] and flag_sitting_dio and not flag_attacking_dio:
                    sprite_dio.kill()
                    flag_attacking_dio = True
                    sprite_dio = Dio(sprite_dio_sitting_light_attack, x_dio, y_dio)
                    sprite_dio.light_attack()

            # Добавление event'ов для проигрывания анимаций Джотаро
            elif event.type == sprite_jotaro.one_step_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.one_step_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
                flag_walking_jotaro = False
            elif event.type == sprite_jotaro.jump_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.jump_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
                flag_jumping_jotaro = False
            elif event.type == sprite_jotaro.start_sitting_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.start_sitting_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_sitting, x_jotaro, y_jotaro)
            elif event.type == sprite_jotaro.stand_up_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.stand_up_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
                flag_sitting_jotaro = False
            elif event.type == sprite_jotaro.light_attack_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.light_attack_event, 0)
                if flag_sitting_jotaro:
                    sprite_jotaro = Jotaro(sprite_jotaro_sitting, x_jotaro, y_jotaro)
                else:
                    sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
                flag_attacking_jotaro = False

            # Добавление отпускания
            elif event.type == pg.KEYUP:
                if event.key == pg.K_s and flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    sprite_jotaro = Jotaro(sprite_jotaro_end_sitting, x_jotaro, y_jotaro)
                    sprite_jotaro.stand_up()
                elif event.key == pg.K_DOWN and flag_sitting_dio:
                    sprite_dio.kill()
                    sprite_dio = Dio(sprite_dio_end_sitting, x_dio, y_dio)
                    sprite_dio.stand_up()

            # Добавление event'ов для проигрывания анимаций Дио
            elif event.type == sprite_dio.one_step_event:
                sprite_dio.kill()
                pg.time.set_timer(sprite_dio.one_step_event, 0)
                sprite_dio = Dio(sprite_dio_afk_left_side, x_dio, y_dio)
                flag_walking_dio = False
            elif event.type == sprite_dio.jump_event:
                sprite_dio.kill()
                pg.time.set_timer(sprite_dio.jump_event, 0)
                sprite_dio = Dio(sprite_dio_afk_left_side, x_dio, y_dio)
                flag_jumping_dio = False
            elif event.type == sprite_dio.start_sitting_event:
                sprite_dio.kill()
                pg.time.set_timer(sprite_dio.start_sitting_event, 0)
                sprite_dio = Dio(sprite_dio_sitting, x_dio, y_dio)
            elif event.type == sprite_dio.stand_up_event:
                sprite_dio.kill()
                pg.time.set_timer(sprite_dio.stand_up_event, 0)
                sprite_dio = Dio(sprite_dio_afk_left_side, x_dio, y_dio)
                flag_sitting_dio = False
            elif event.type == sprite_dio.light_attack_event:
                sprite_dio.kill()
                pg.time.set_timer(sprite_dio.light_attack_event, 0)
                if flag_sitting_dio:
                    sprite_dio = Dio(sprite_dio_sitting, x_dio, y_dio)
                else:
                    sprite_dio = Dio(sprite_dio_afk_left_side, x_dio, y_dio)
                flag_attacking_dio = False

        screen.fill(pg.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()
        hp_and_mana_sprites.draw(screen)
        hp_and_mana_dio.update()
        # Отрисовка здоровья и маны
        pg.draw.rect(screen, pg.Color('red'), (0, 21, hp_jotaro * 3, 5))
        pg.draw.rect(screen, pg.Color('blue'), (0, 26, mana_jotaro * 3, 4))
        pg.draw.rect(screen, pg.Color('red'), (800 - hp_dio * 3, 21, 800, 5))
        pg.draw.rect(screen, pg.Color('blue'), (800 - mana_dio * 3, 26, 800, 4))
        pg.draw.rect(screen, pg.Color('black'), (0, 530, 800, 1))
        pg.display.flip()
        time.Clock().tick(fps)
    pg.quit()
