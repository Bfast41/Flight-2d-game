import pygame as py

py.init()

width = 800
length = 600
screen = py.display.set_mode((width,length))
clock = py.time.Clock()

player = py.Rect(500,150,50,30)
speed = 5

enemy = py.Rect(400,200,40,20)
enemy2 = py.Rect(100,300,40,20)
enemy3 = py.Rect(175,100,40,20)
enemy4 = py.Rect(250,150,40,20)
enemy5 = py.Rect(120,230,40,20)
enemy_speed = 3


run = True
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    keys = py.key.get_pressed()
    if keys[py.K_a]and player.left > 0:
            player.x -=speed
    if keys[py.K_d] and player.right < width:
            player.x +=speed
    if keys[py.K_w] and player.top > 0:
            player.y -=speed
    if keys[py.K_s] and player.bottom < length:
            player.y +=speed

    enemy.x -=enemy_speed
    enemy2.x -=enemy_speed
    enemy3.x -=enemy_speed
    enemy4.x -= enemy_speed
    enemy5.x -= enemy_speed

    if enemy.right < 0:
          enemy.x=width
    if enemy2.right < 0:
              enemy2.x=width
    if enemy3.right < 0:
            enemy3.x=width
    if enemy4.right < 0:
                enemy4.x=width
    if enemy5.right < 0:
           enemy5.x=width
   
    screen.fill((135, 206, 235))
    py.draw.rect(screen,(255,140,0),player)
    py.draw.rect(screen ,(255,0,0),enemy )
    py.draw.rect(screen ,(255,125,0),enemy2 )
    py.draw.rect(screen ,(235,210,0),enemy3 )
    py.draw.rect(screen ,(150,156,135),enemy4 )
    py.draw.circle(screen ,(180,0,255),enemy5.center , 25 )
    py.display.flip()
    clock.tick(60)
py.quit()


