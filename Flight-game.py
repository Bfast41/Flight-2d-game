import pygame as py
import random as rd

py.init()

width = 800
height = 1000
screen = py.display.set_mode((width,height))
py.display.set_caption('fighter 2d game')
clock = py.time.Clock()

player_1 = py.image.load("Flighter/fighter.png").convert_alpha()
player_1 = py.transform.scale(player_1 , (100,100))

enemy_m = py.image.load("Flighter/Rocket.png").convert_alpha()
enemy_m = py.transform.scale(enemy_m,(90,90))

player = player_1.get_rect()
player.topleft = (300,400)
speed = 8

enemies = [py.Rect(200,150,50,20),
           py.Rect(100,350,50,20),
           py.Rect(300,550,50,20),
           py.Rect(500,300,50,20)]

enemy_speed = 5

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    key = py.key.get_pressed()
    if key[py.K_a] and player.left > 0:
        player.x -=speed
    if key[py.K_d] and player.right < width:
        player.x+=speed
    if key[py.K_w] and player.top > 0:
        player.y-=speed
    if key[py.K_s] and player.bottom < height:
        player.y +=speed 

    for enemy in enemies:

        enemy.x -= enemy_speed
        if enemy.right < 0:
                enemy.x = rd.randint(850,1200)
                enemy.y = rd.randint(50 ,height - 150)
        
        if player.colliderect(enemy.inflate(-40, -40)):
            print('You got one job , which is to surive')
            running = False

   
    screen.fill((255,125,0))
    screen.blit(player_1 , player)
    for enemy in enemies:
        screen.blit(enemy_m , enemy)

    py.display.flip()
    clock.tick(60)
py.quit()

            


