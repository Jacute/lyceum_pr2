import os
import pygame as pg
from pygame import time
import time as tm


flag_walking_jotaro, flag_jumping_jotaro, flag_sitting_jotaro = False, False, False
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
        pg.time.set_timer(one_step_event, 500)
        self.rect.move(self.rect.x + 20, self.rect.y)
        x += 20

    def go_left(self):
        global x
        pg.time.set_timer(one_step_event, 500)
        self.rect.move(self.rect.x - 20, self.rect.y)
        x -= 20

    def jump(self):
        pg.time.set_timer(jump_event, 1711)

    def start_sitting(self):
        pg.time.set_timer(start_sitting_event, 200)

    def stand_up(self):
        pg.time.set_timer(stand_up_event, 777)


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
    sprite_jotaro_walking_left1 = [load_image('jotaro_walking_left8.png'),
                            load_image('jotaro_walking_left7.png'),
                            load_image('jotaro_walking_left6.png'),
                            load_image('jotaro_walking_left5.png'),
                            load_image('jotaro_walking_left4.png'),
                            load_image('jotaro_walking_left3.png'),
                            load_image('jotaro_walking_left2.png'),
                            load_image('jotaro_walking_left1.png')]
    sprite_jotaro_walking_left2 = [load_image('jotaro_walking_left16.png'),
                            load_image('jotaro_walking_left15.png'),
                            load_image('jotaro_walking_left14.png'),
                            load_image('jotaro_walking_left13.png'),
                            load_image('jotaro_walking_left12.png'),
                            load_image('jotaro_walking_left11.png'),
                            load_image('jotaro_walking_left10.png'),
                            load_image('jotaro_walking_left9.png')]
    sprite_jotaro_jumping = [load_image('jotaro_jump1.png'), load_image('jotaro_jump2.png'),
                      load_image('jotaro_jump3.png'), load_image('jotaro_jump4.png'),
                      load_image('jotaro_jump5.png'), load_image('jotaro_jump6.png'),
                      load_image('jotaro_jump7.png'), load_image('jotaro_jump8.png'),
                      load_image('jotaro_jump9.png'), load_image('jotaro_jump10.png'),
                      load_image('jotaro_jump11.png'), load_image('jotaro_jump12.png'),
                      load_image('jotaro_jump13.png'), load_image('jotaro_jump14.png'),
                      load_image('jotaro_jump15.png'), load_image('jotaro_jump16.png'),
                      load_image('jotaro_jump17.png'), load_image('jotaro_jump18.png'),
                      load_image('jotaro_jump19.png'), load_image('jotaro_jump20.png'),
                      load_image('jotaro_jump21.png'), load_image('jotaro_jump22.png')]
    sprite_jotaro_start_sitting = [load_image('jotaro_sit1.png'), load_image('jotaro_sit2.png'),
                                   load_image('jotaro_sit3.png'), load_image('jotaro_sit4.png')]
    sprite_jotaro_sitting = [load_image('jotaro_sit5.png')]
    sprite_jotaro_end_sitting = [load_image('jotaro_sit8.png'), load_image('jotaro_sit9.png'),
                                 load_image('jotaro_sit10.png'), load_image('jotaro_sit11.png'),
                                 load_image('jotaro_sit12.png'), load_image('jotaro_sit13.png'),
                                 load_image('jotaro_sit14.png'), load_image('jotaro_sit15.png'),
                                 load_image('jotaro_sit16.png'), load_image('jotaro_sit17.png')]
    sprite_hp_and_mana_jotaro = load_image("hp_and_mana_jotaro.png")
    sprite_hp_and_mana_dio = load_image("hp_and_mana_dio.png")
    hp_and_mana_jotaro = Hp_and_Mana(sprite_hp_and_mana_jotaro, 0, 0)
    hp_and_mana_dio = Hp_and_Mana(sprite_hp_and_mana_dio, 499, 0)
    one_step_event = pg.USEREVENT + 1
    jump_event = pg.USEREVENT + 2
    start_sitting_event = pg.USEREVENT + 3
    stand_up_event = pg.USEREVENT + 4
    # Задаём координаты отрисовки спрайта в игровом окне:
    x, y = (0, 380)
    hp_jotaro, mana_jotaro = 100, 45
    # Создаём экземпляр анимированного спрайта:
    sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, x, y)
    pg.key.set_repeat(1, 20)
    fps = 13
    # count - переменная, которая считает, на какую ногу должен будет наступать персонаж
    # (0 - правая, 1 - левая)
    count = 0
    running = True
    # Главный игровой цикл:
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d and not flag_walking_jotaro and x + 97 <= width\
                        and not flag_jumping_jotaro and not flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    if count == 0:
                        sprite_jotaro = AnimaSprite(sprite_jotaro_walking_right1, x, y)
                    elif count == 1:
                        sprite_jotaro = AnimaSprite(sprite_jotaro_walking_right2, x, y)
                    flag_walking_jotaro = True
                    count = (count + 1) % 2
                    sprite_jotaro.go_right()
                elif event.key == pg.K_a and not flag_walking_jotaro and x - 20 >= 0\
                        and not flag_jumping_jotaro and not flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    if count == 0:
                        sprite_jotaro = AnimaSprite(sprite_jotaro_walking_left1, x, y)
                    elif count == 1:
                        sprite_jotaro = AnimaSprite(sprite_jotaro_walking_left2, x, y)
                    flag_walking_jotaro = True
                    count = (count + 1) % 2
                    sprite_jotaro.go_left()
                elif event.key == pg.K_w and not flag_walking_jotaro and not flag_jumping_jotaro and not flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    flag_jumping_jotaro = True
                    sprite_jotaro = AnimaSprite(sprite_jotaro_jumping, x, y)
                    sprite_jotaro.jump()
                elif event.key == pg.K_s and not flag_walking_jotaro and not flag_jumping_jotaro and not flag_sitting_jotaro:
                    sprite_jotaro.kill()
                    flag_sitting_jotaro = True
                    sprite_jotaro = AnimaSprite(sprite_jotaro_start_sitting, x, y)
                    sprite_jotaro.start_sitting()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_s:
                    sprite_jotaro.kill()
                    sprite_jotaro = AnimaSprite(sprite_jotaro_end_sitting, x, y)
                    sprite_jotaro.stand_up()
            elif event.type == one_step_event:
                sprite_jotaro.kill()
                pg.time.set_timer(one_step_event, 0)
                sprite_jotaro.kill()
                sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, x, y)
                flag_walking_jotaro = False
            elif event.type == jump_event:
                sprite_jotaro.kill()
                pg.time.set_timer(jump_event, 0)
                sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, x, y)
                flag_jumping_jotaro = False
            elif event.type == start_sitting_event:
                sprite_jotaro.kill()
                pg.time.set_timer(start_sitting_event, 0)
                sprite_jotaro = AnimaSprite(sprite_jotaro_sitting, x, y)
            elif event.type == stand_up_event:
                sprite_jotaro.kill()
                pg.time.set_timer(stand_up_event, 0)
                sprite_jotaro = AnimaSprite(sprite_jotaro_afk_right_side, x, y)
                flag_sitting_jotaro = False
        screen.fill(pg.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()
        hp_and_mana_sprites.draw(screen)
        pg.draw.rect(screen, pg.Color('red'), (0, 21, hp_jotaro * 3, 5))
        pg.draw.rect(screen, pg.Color('blue'), (0, 26, mana_jotaro * 3, 5))
        pg.display.flip()
        time.Clock().tick(fps)
    pg.quit()
