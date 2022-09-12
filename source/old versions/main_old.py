# kryptografie escape room
# programmiert von Medea Emch im Rahmen einer Maturaarbeit an der Kantonsschule Alpenquai Luzern im Jahr 2022


#! IMPORTS --------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *
import varANDfunc

pygame.init()


#! MAIN LOOP ------------------------------------------------------------------------------------------------------------------
while varANDfunc.running:
    varANDfunc.screen.fill(varANDfunc.color_theme[0])
    
    if varANDfunc.scene > 0: # if this is true, it means you are in game
        #? room.render() # once the room stuff works, remove the comment
        varANDfunc.userinterface()
        #? room.render_uv_stuff() # once the room stuff works, remove the comment 
    if varANDfunc.scene == 0: # renders the main menu
        varANDfunc.menu()
    if varANDfunc.scene == -1: # render the info screen
        varANDfunc.info_screen()


    mbdown, mbup = False, False # reset mouse button variables

    pygame.display.flip() # put everything on the screen

    varANDfunc.clock.tick(varANDfunc.fps)

pygame.quit()
