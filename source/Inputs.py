import pygame, Setup
from pygame.locals import *

def check_inputs():
    global running, mbdown, mbup, mx, my, click

    mbdown, mbup = False, False # reset mouse button variables

    for ev in pygame.event.get(): # gets inputs for the frame
        if ev.type == QUIT: # checks whether the window has been closed -> stops the main loop
            Setup.running = not Setup.running
        if ev.type == MOUSEBUTTONDOWN: # checks whether a mouse button has been pressed down during the current frame
            mbdown = True
        if ev.type == MOUSEBUTTONUP: # checks whether a mouse button has been released during the current frame
            mbup = True

    mx, my = pygame.mouse.get_pos() # gets current cursor coordinates
    click = pygame.mouse.get_pressed()[0] # checks  wether the left mouse button is currently pressed down or not