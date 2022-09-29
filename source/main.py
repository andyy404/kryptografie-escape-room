import pygame
from pygame.locals import *
import Setup, Inputs

Setup.init()
Setup.colors()
Setup.constants()
Setup.variables()
Setup.instances()

while Setup.running:
    Inputs.check_inputs()

    Setup.screen.fill(Setup.color_theme[0])

    if Setup.scene == 0: # renders the main menu
        Setup.menu.update()
        
    if Setup.scene == 1: # if this is true, it means you are in game
        Setup.room.draw_lines()
        Setup.room.draw_objects()

        Setup.room.check_hitboxes()

        Setup.uv_lamp.update()
        Setup.cipher_wheel.check()

        Setup.room.draw_uv_things()
        
        Setup.pause.button()

        Setup.timer.update()
        Setup.timer.draw()

    if Setup.scene == 2:
        Setup.end_screen.update(True)
        Setup.timer.draw()

    if Setup.scene == 3:
        Setup.end_screen.update(False)

    if Setup.scene == 4:
        Setup.pause.update()
        Setup.timer.draw()

    if Setup.scene == 5:
        Setup.cipher_wheel.update()
        Setup.timer.update()
        Setup.timer.draw()

    if Setup.scene == 6:
        Setup.room.active_interaction_screen()

        Setup.uv_lamp.update()
        Setup.cipher_wheel.check()

        Setup.room.draw_uv_things()

        Setup.back_button()

        Setup.timer.update()
        Setup.timer.draw()


    if Setup.timer.time < 0:
        Setup.scene = 3
        Setup.color_theme = Setup.dark_theme
        Setup.timer.time = 0
        Setup.timer.running = False

    pygame.display.flip() # put everything on the screen

    Setup.clock.tick(60)

pygame.quit()