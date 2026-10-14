import pygame as py
import random

py.init()
width = 800
length = 1000
screen = py.display.set_mode((width,length))
py.display.set_caption('Flighter  Game')
clock = py.time.Clock()

player = py.Rect(400,200,50,20)
speed = 10

enemies = [
 py.Rect(-100,200,40,20),
py.Rect(-200,400,40,20),
py.Rect(-300,200,40,20),
py.Rect(-100,200,40,20)
]
enemy_speed = 5


run = True
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    key = py.key.get_pressed()
    if key[py.K_a] and player.left > 0:
        player.x -=speed
    if key[py.K_d] and player.right < width:
        player.x +=speed
    if key[py.K_s] and player.bottom < length:
        player.y +=speed
    if key[py.K_w] and player.top > 0:
        player.y-=speed

    for enemy in enemies:
        enemy.x+=enemy_speed
        if enemy.left > width:
            enemy.x = random.randint(-400,-80)
            enemy.y = random.randint(50,length - 100)


    for enemy in enemies:
       if player.colliderect(enemy):
           print('Game over')
           run = False

    screen.fill((235,120,0))
    py.draw.rect(screen ,(255,140,0),player)
    for enemy in enemies:
        py.draw.rect(screen,(230,140,60),enemy)
    py.display.flip()
    clock.tick(60)
py.quit()
            


