import pygame

import model

pygame.init()

screen = pygame.display.set_mode([700, 700])
pygame.display.set_caption("Убеги, если сможешь!")

font = pygame.font.SysFont("Arial", 15, True)

def draw():
    screen.fill([0,0,0])

    pygame.draw.rect(screen, [122, 232,12], model.victim["rect"])
    t = font.render(str(model.victim["touches"]), True, [0, 0, 0])
    trect = t.get_rect()
    trect.center = model.victim["rect"].center
    screen.blit(t, trect)

    pygame.draw.rect(screen, [200, 30, 70], model.hunter["rect"])
    t = font.render(str(model.hunter["touches"]), True, [0, 0, 0])
    trect = t.get_rect()
    trect.center = model.hunter["rect"].center
    screen.blit(t, trect)

    pygame.display.set_caption("Убеги, если сможешь! SpeedX="+str(model.hunter["speed_x"])+" SpeedY="+str(model.hunter["speed_y"]))

    if model.game_over:
        t = font.render("Game over!", True, [255, 0, 255])
        trect = t.get_rect()
        trect.center=[350, 350]
        screen.blit(t, trect)

    pygame.display.flip()