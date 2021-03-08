'''elif keys[pg.K_s] and not any(flags_jotaro):
    sprite_jotaro.kill()
    flag_sitting_jotaro = True
    sprite_jotaro = Jotaro(sprite_jotaro_start_sitting, x_jotaro, y_jotaro)
    sprite_jotaro.start_sitting()

                elif keys[pg.K_k] and not any(flags_jotaro):
                    sprite_jotaro.kill()
                    flag_blocking_jotaro = True
                    sprite_jotaro = Jotaro(sprite_jotaro_blocking1, x_jotaro, y_jotaro)
                    sprite_jotaro.start_blocking()

elif event.type == sprite_jotaro.start_sitting_event:
    sprite_jotaro.kill()
    pg.time.set_timer(sprite_jotaro.start_sitting_event, 0)
    sprite_jotaro = Jotaro(sprite_jotaro_sitting, x_jotaro, y_jotaro)
elif event.type == sprite_jotaro.stand_up_event:
    sprite_jotaro.kill()
    pg.time.set_timer(sprite_jotaro.stand_up_event, 0)
    sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
    flag_sitting_jotaro = False

            elif event.type == sprite_jotaro.start_blocking_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.start_blocking_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_blocking2, x_jotaro, y_jotaro)
            elif event.type == sprite_jotaro.end_blocking_event:
                sprite_jotaro.kill()
                pg.time.set_timer(sprite_jotaro.end_blocking_event, 0)
                sprite_jotaro = Jotaro(sprite_jotaro_afk_right_side, x_jotaro, y_jotaro)
                flag_blocking_jotaro = False

elif event.type == pg.KEYUP:
    if event.key == pg.K_s and flag_sitting_jotaro:
        sprite_jotaro.kill()
        sprite_jotaro = Jotaro(sprite_jotaro_end_sitting, x_jotaro, y_jotaro)
        sprite_jotaro.stand_up()

                elif event.key == pg.K_k and flag_blocking_jotaro:
                    sprite_jotaro.kill()
                    sprite_jotaro = Jotaro(sprite_jotaro_blocking3, x_jotaro, y_jotaro)
                    sprite_jotaro.end_blocking()
'''