import pygame, random

hunter_rect = pygame.Rect(
    random.randint(0,660),
    random.randint(0,300),
    40, 40
)
hunter={"rect":hunter_rect, "speed_x": 2, "speed_y":4, "touches": 0}

victim_rect = pygame.Rect(330, 450, 40, 40)
victim={"rect":victim_rect, "touches": 0}

game_over = False

def step():
    if not game_over:
        move_hunter()

def move_hunter():
    hunter["rect"].x+=hunter["speed_x"]
    if hunter["rect"].right>=700:
        hunter["rect"].right=700
        hunter["speed_x"]=-hunter["speed_x"]
        hunter["touches"]+=1

    if hunter["rect"].left <= 0:
        hunter["rect"].left = 0
        hunter["speed_x"] = -hunter["speed_x"]
        hunter["touches"] += 1

    hunter["rect"].y+=hunter["speed_y"]
    if hunter["rect"].bottom>=700:
        hunter["rect"].bottom=700
        hunter["speed_y"]=-hunter["speed_y"]
        hunter["touches"]+=1

    if hunter["rect"].top <= 0:
        hunter["rect"].top = 0
        hunter["speed_y"] = -hunter["speed_y"]
        hunter["touches"] += 1

    if hunter["touches"]>3:
        hunter["touches"]=0
        x, y = random.choice([ [0, 1], [1, 0] ])

        if hunter["speed_x"]>0:
            hunter["speed_x"]+=x
            hunter["rect"].height=40+hunter["speed_x"]*6
        else:
            hunter["speed_x"] -= x
            hunter["rect"].height = 40 - hunter["speed_x"] * 6

        if hunter["speed_y"]>0:
            hunter["speed_y"]+=y
            hunter["rect"].width = 40 + hunter["speed_y"] * 6
        else:
            hunter["speed_y"] -= y
            hunter["rect"].width = 40 - hunter["speed_y"] * 6

    check_touch()

def move_victim(x, y):
    if game_over:
        return

    victim["rect"].centerx=x
    victim["rect"].centery = y
    check_touch()

def check_touch():
    global game_over
    center = victim['rect'].center
    if victim['rect'].colliderect(hunter['rect']):
        victim['touches']+=1

    if victim['touches']>1:
        victim['touches']-=1
        victim['rect'].width+=1
        victim['rect'].height += 1
        victim['rect'].center = center

    if victim['rect'].width>=700:
        game_over=True