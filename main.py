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
    def __init__(self, sheet, cols, rows, x, y):
        super().__init__(all_sprites)

        # frames - атрибут класса,
        # список для хранения последовательности кадров спрайта:
        self.frames = []

        # Разрезаем лист на кадры,
        # используя функцию cut_sheet() из данного класса (см. ниже):
        self.cut_sheet(sheet, cols, rows)

        # Обнуляем номер текущего кадра:
        self.cur_frame = 0

        # image - атрибут класса,
        # в который помещаем текущий кадр:
        self.image = self.frames[self.cur_frame]

        # Помещаем прямоугольник с кадром в координаты (x, y):
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, cols, rows):
        """Функция разрезания листа с кадрами спрайта"""
        # Задаём маленький прямоугольник размером с кадр:
        self.rect = pg.Rect(0, 0, sheet.get_width() // cols, sheet.get_height() // rows)
        # Пробегаем по всем кадрам спрайта:
        for j in range(rows):
            for i in range(cols):
                # Определяем координаты кадра на листе:
                frame_location = (self.rect.w * i, self.rect.h * j)
                # Копируем кадр из листа в список frames, используя метод subsurface(),
                # который возвращает новую поверхность с нарисованным на ней кадром:
                self.frames.append(sheet.subsurface(pg.Rect(frame_location, self.rect.size)))

    def update(self):
        """Смена кадра спрайта"""
        # Переключаемся на номер следующего кадра,
        # но так, чтобы не выйти за границы списка frames.
        # Для этого закольцовываем счёт кадров при помощи операции %:
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)

        # Меняем кадр - помещаем новый кадр в атрибут image:
        self.image = self.frames[self.cur_frame]


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Игра')
    size = width, height = 300, 300
    screen = pg.display.set_mode((size), pg.RESIZABLE)
    all_sprites = pg.sprite.Group()
    sheet_jotaro = load_image('jotaro_afk.png')

    # Задаём способ разрезания листа на кадры.
    # (столбцов, строк) --> (20, 1) --> 20 кадров:
    cols, rows = (20, 1)

    # Задаём координаты отрисовки спрайта в игровом окне:
    x, y = (0, 0)

    # Создаём экземпляр анимированного спрайта:
    sprite_jotaro = AnimaSprite(sheet_jotaro, cols, rows, x, y)

    fps = 15
    # Главный игровой цикл:
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(pg.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()
        pg.display.flip()
        time.Clock().tick(fps)
    pg.quit()
