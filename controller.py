import pygame

import model


def process_events():
    events = pygame.event.get()
    for e in events:
        if e.type==pygame.QUIT:
            exit()

        if e.type==pygame.MOUSEMOTION:
            model.move_victim(e.pos[0], e.pos[1])