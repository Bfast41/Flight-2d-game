import pygame as py
import random as rd

py.init()

width, height = 800, 600
screen = py.display.set_mode((width, height))
py.display.set_caption("Flighter 2d game")
clock = py.time.Clock()

base = py.image.load('Flighter/base.png').convert_alpha()
base_1 = py.transform.scale(base, (700, 300))  # Scaled to fit nicely

bg_x = 0
level = 1
enemy_speed = 5

player_1 = py.image.load('Flighter/fighter.png').convert_alpha()
player_1 = py.transform.scale(player_1, (100, 100))

enemy_m = py.image.load('Flighter/Rocket.png').convert_alpha()
enemy_m = py.transform.scale(enemy_m, (90, 90))

player = player_1.get_rect()
player.topleft = (300, 400)
speed = 8

enemies = [
    py.Rect(200, 150, 90, 90),
    py.Rect(100, 350, 90, 90),
    py.Rect(300, 550, 90, 90),
    py.Rect(500, 300, 90, 90)
]

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    key = py.key.get_pressed()
    if key[py.K_a] and player.left > 0:
        player.x -= speed
    if key[py.K_d] and player.right < width:
        player.x += speed
    if key[py.K_w] and player.top > 0:
        player.y -= speed
    if key[py.K_s] and player.bottom < height:
        player.y += speed

    # Background scrolling
    bg_x -= 2
    if bg_x <= -700:
        bg_x = 0
        if level < 10:
            level += 1
            enemy_speed += 1

    # Orange background
    screen.fill((255, 140, 0))

    # FIX: Draw base at the bottom where it's fully visible on screen
    screen.blit(base_1, (bg_x, height - 300))
    screen.blit(base_1, (bg_x + 700, height - 300))

    # Level text
    font = py.font.SysFont(None, 36)
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(level_text, (20, 20))

    for enemy in enemies:
        enemy.x -= enemy_speed
        if enemy.right < 0:
            enemy.x = width + rd.randint(50, 300)
            enemy.y = rd.randint(50, height - 100)

        if player.inflate(-40, -40).colliderect(enemy.inflate(-40, -40)):
            print('You got one job, which is to survive')
            running = False

        screen.blit(enemy_m, enemy)

    screen.blit(player_1, player)

    py.display.flip()
    clock.tick(60)

py.quit()


