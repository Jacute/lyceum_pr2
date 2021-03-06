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


class HpandMana(pg.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(hp_and_mana_sprites)
        self.image = sheet
        self.rect = self.image.get_rect().move(x, y)


class Dio(pg.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(all_sprites)
        ''' Ивенты Дио '''
        self.one_step_event, self.jump_event, self.start_sitting_event, self.stand_up_event, self.light_attack_event,\
            self.start_blocking_event, self.end_blocking_event, self.sitting_light_damage_event,\
            self.light_damage_event = pg.USEREVENT + 9, pg.USEREVENT + 10, pg.USEREVENT + 11, pg.USEREVENT + 12,\
            pg.USEREVENT + 13, pg.USEREVENT + 14, pg.USEREVENT + 15, pg.USEREVENT + 16, pg.USEREVENT + 17
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
        self.mask = pg.mask.from_surface(self.image)

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
        if not pg.sprite.collide_mask(self, sprite_jotaro):
            pg.time.set_timer(self.one_step_event, 630)
            self.rect.move(self.rect.x - 20, self.rect.y)
            x_dio -= 20
        else:
            pg.time.set_timer(self.one_step_event, 630)

    def jump(self):
        pg.time.set_timer(self.jump_event, 930)

    def start_sitting(self):
        pg.time.set_timer(self.start_sitting_event, 235)

    def stand_up(self):
        pg.time.set_timer(self.stand_up_event, 235)

    def start_blocking(self):
        pg.time.set_timer(self.start_blocking_event, 400)

    def end_blocking(self):
        pg.time.set_timer(self.end_blocking_event, 400)

    def light_attack(self):
        pg.time.set_timer(self.light_attack_event, 400)

    def sitting_light_damage(self):
        global hp_dio
        pg.time.set_timer(self.sitting_light_damage_event, 200)

    def light_damage(self):
        global hp_dio
        pg.time.set_timer(self.light_damage_event, 200)


class Jotaro(pg.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(all_sprites)
        ''' Ивенты Джотаро '''
        self.one_step_event, self.jump_event, self.start_sitting_event, self.stand_up_event, self.light_attack_event,\
            self.start_blocking_event, self.end_blocking_event, self.sitting_light_damage_event,\
            self.light_damage_event = pg.USEREVENT + 1, pg.USEREVENT + 2, pg.USEREVENT + 3, pg.USEREVENT + 4,\
            pg.USEREVENT + 5, pg.USEREVENT + 6, pg.USEREVENT + 7, pg.USEREVENT + 18, pg.USEREVENT + 19
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
        self.mask = pg.mask.from_surface(self.image)

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
        if not pg.sprite.collide_mask(self, sprite_dio):
            pg.time.set_timer(self.one_step_event, 630)
            self.rect.move(self.rect.x + 20, self.rect.y)
            x_jotaro += 20
        else:
            pg.time.set_timer(self.one_step_event, 630)

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

    def start_blocking(self):
        pg.time.set_timer(self.start_blocking_event, 200)

    def end_blocking(self):
        pg.time.set_timer(self.end_blocking_event, 772)

    def light_attack(self):
        pg.time.set_timer(self.light_attack_event, 630)

    def sitting_light_damage(self):
        global hp_jotaro
        pg.time.set_timer(self.sitting_light_damage_event, 200)

    def light_damage(self):
        global hp_jotaro
        pg.time.set_timer(self.light_damage_event, 200)


if __name__ == '__main__':
    # Инициализируем pygame
    pg.init()
    pg.mixer.music.load(os.path.abspath("sounds/Danton - JC OST.wav"))
    pg.mixer.music.set_volume(0.75)
    pg.mixer.music.play(-1)
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
    flag_walking_jotaro, flag_jumping_jotaro, flag_sitting_jotaro, flag_attacking_jotaro, flag_blocking_jotaro,\
        flag_jotaro_tacking_damage = False, False, False, False, False, False
    flag_walking_dio, flag_jumping_dio, flag_sitting_dio, flag_attacking_dio, flag_blocking_dio,\
        flag_dio_tacking_damage = False, False, False, False, False, False
    # Создаём экземпляры анимированных спрайтов:
    sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
    sprite_dio = Dio(sprite_dio_afk_left_side, x_dio, y_dio)
    # Задаём повтор клавиш
    pg.key.set_repeat(1, 20)
    # Задаём fps
    fps = 13
    # count - переменная, которая считает, на какую ногу должен будет наступать персонаж
    # (0 - правая, 1 - левая)
    count_jotaro, count_dio = 0, 0
    running = True
    # Главный игровой цикл:
    while running:
        if hp_jotaro <= 0:
            print('Победил Дио')
            running = False
        elif hp_dio <= 0:
            print('Победил Джотаро')
            running = False
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            flags_jotaro = {flag_walking_jotaro, flag_jumping_jotaro, flag_sitting_jotaro, flag_attacking_jotaro,
                            flag_jotaro_tacking_damage, flag_blocking_jotaro}
            flags_dio = {flag_jumping_dio, flag_sitting_dio, flag_attacking_dio, flag_walking_dio,
                         flag_dio_tacking_damage, flag_blocking_dio}
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
                    if pg.sprite.collide_mask(sprite_jotaro, sprite_dio) and not flag_jumping_dio:
                        if flag_blocking_dio:
                            hp_dio -= 5
                        elif flag_sitting_dio:
                            sprite_dio.kill()
                            sprite_dio = Dio(sprite_dio_sitting_light_attack_taking_damage, x_dio, y_dio)
                            sprite_dio.sitting_light_damage()
                            hp_dio -= 10
                        else:
                            sprite_dio.kill()
                            sprite_dio = Dio(sprite_dio_light_attack_taking_damage, x_dio, y_dio)
                            sprite_dio.light_damage()
                            hp_dio -= 10
                    sprite_jotaro.light_attack()
                elif keys[pg.K_l] and flag_sitting_jotaro and not flag_attacking_jotaro:
                    sprite_jotaro.kill()
                    flag_attacking_jotaro = True
                    sprite_jotaro = Jotaro(sprite_jotaro_sitting_light_attack, x_jotaro, y_jotaro)
                    if pg.sprite.collide_mask(sprite_jotaro, sprite_dio) and not flag_jumping_dio:
                        if flag_blocking_dio:
                            hp_dio -= 5
                        elif flag_sitting_dio:
                            hp_dio -= 10
                            sprite_dio.kill()
                            sprite_dio = Dio(sprite_dio_sitting_light_attack_taking_damage, x_dio, y_dio)
                            sprite_dio.sitting_light_damage()
                        else:
                            hp_dio -= 10
                            sprite_dio.kill()
                            sprite_dio = Dio(sprite_dio_light_attack_taking_damage, x_dio, y_dio)
                            sprite_dio.light_damage()
                    sprite_jotaro.light_attack()
                elif keys[pg.K_k] and not any(flags_jotaro):
                    sprite_jotaro.kill()
                    flag_blocking_jotaro = True
                    sprite_jotaro = Jotaro(sprite_jotaro_start_blocking, x_jotaro, y_jotaro)
                    sprite_jotaro.start_blocking()

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
                    if pg.sprite.collide_mask(sprite_jotaro, sprite_dio) and not flag_sitting_jotaro:
                        if flag_blocking_jotaro:
                            hp_jotaro -= 3.75
                        else:
                            hp_jotaro -= 7.5
                            sprite_jotaro.kill()
                            sprite_jotaro = Jotaro(sprite_jotaro_light_attack_taking_damage, x_jotaro, y_jotaro)
                            sprite_jotaro.light_damage()
                    sprite_dio = Dio(sprite_dio_light_attack, x_dio, y_dio)
                    sprite_dio.light_attack()
                elif keys[pg.K_KP7] and flag_sitting_dio and not flag_attacking_dio:
                    sprite_dio.kill()
                    flag_attacking_dio = True
                    sprite_dio = Dio(sprite_dio_sitting_light_attack, x_dio, y_dio)
                    if pg.sprite.collide_mask(sprite_jotaro, sprite_dio) and not flag_jumping_jotaro:
                        if flag_blocking_jotaro:
                            hp_jotaro -= 3.75
                        elif flag_sitting_jotaro:
                            sprite_jotaro.kill()
                            sprite_jotaro = Jotaro(sprite_jotaro_sitting_light_attack_taking_damage, x_jotaro, y_jotaro)
                            sprite_jotaro.sitting_light_damage()
                            hp_jotaro -= 7.5
                        else:
                            sprite_jotaro.kill()
                            sprite_jotaro = Jotaro(sprite_jotaro_light_attack_taking_damage, x_jotaro, y_jotaro)
                            sprite_jotaro.light_damage()
                            hp_jotaro -= 7.5
                    sprite_dio.light_attack()
                elif keys[pg.K_KP8] and not any(flags_dio):
                    sprite_dio.kill()
                    flag_blocking_dio = True
                    sprite_dio = Dio(sprite_dio_start_blocking, x_dio, y_dio)
                    sprite_dio.start_blocking()

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
            elif event.type == sprite_jotaro.light_damage_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.light_damage_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
                flag_jotaro_tacking_damage = False
            elif event.type == sprite_jotaro.sitting_light_damage_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.sitting_light_damage_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_sitting, x_jotaro, y_jotaro)
                flag_jotaro_tacking_damage = False
            elif event.type == sprite_jotaro.start_blocking_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.start_blocking_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_blocking, x_jotaro, y_jotaro)
            elif event.type == sprite_jotaro.end_blocking_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.end_blocking_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
                flag_blocking_jotaro = False

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
                elif event.key == pg.K_KP8 and flag_blocking_dio:
                    sprite_dio.kill()
                    sprite_dio = Dio(sprite_dio_end_blocking, x_dio, y_dio)
                    sprite_dio.end_blocking()
                elif event.key == pg.K_k and flag_blocking_jotaro:
                    sprite_jotaro.kill()
                    sprite_jotaro = Jotaro(sprite_jotaro_end_blocking, x_jotaro, y_jotaro)
                    sprite_jotaro.end_blocking()

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
            elif event.type == sprite_dio.light_damage_event:
                sprite_dio.kill()
                pg.time.set_timer(sprite_dio.light_damage_event, 0)
                sprite_dio = Dio(sprite_dio_afk_left_side, x_dio, y_dio)
                flag_dio_tacking_damage = False
            elif event.type == sprite_dio.sitting_light_damage_event:
                sprite_dio.kill()
                pg.time.set_timer(sprite_dio.sitting_light_damage_event, 0)
                sprite_dio = Dio(sprite_dio_sitting, x_dio, y_dio)
                flag_dio_tacking_damage = False
            elif event.type == sprite_dio.start_blocking_event:
                sprite_dio.kill()
                pg.time.set_timer(sprite_dio.start_blocking_event, 0)
                sprite_dio = Dio(sprite_dio_blocking, x_dio, y_dio)
            elif event.type == sprite_dio.end_blocking_event:
                sprite_dio.kill()
                pg.time.set_timer(sprite_dio.end_blocking_event, 0)
                sprite_dio = Dio(sprite_dio_afk_left_side, x_dio, y_dio)
                flag_blocking_dio = False

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
