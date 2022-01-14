import pygame
import random


def create_snake(surface, x, y, w, h, color):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, color, rect)
    return rect


def random_coords():
    x1 = random.randint(10, WIDTH - 10)
    y1 = random.randint(10, HEIGHT - 10)
    return x1, y1


def make_apples(surface):
    global col_apples, x_apple, y_apple, player_x, player_y, player_speed
    if eat_apple(player_x, player_y, x_apple, y_apple):
        col_apples = 0
        new_size_snake(player_x, player_y)
        if player_speed <= 8:
            player_speed += 0.25
    if col_apples == 0:
        x_apple, y_apple = random_coords()
        rect_apple = pygame.Rect(x_apple, y_apple, 12, 12)
    else:
        rect_apple = pygame.Rect(x_apple, y_apple, 12, 12)
    pygame.draw.rect(surface, (0, 255, 0), rect_apple)
    col_apples += 1
    return rect_apple


def make_textures():
    player = create_snake(display, player_x, player_y, 15, 15, (255, 0, 0))
    apples = make_apples(display)


def in_game():
    global player_x, player_y, speed_limit, player_speed

    if poz_x:
        player_x += vx
    if poz_y:
        player_y += vy
    if player_x <= 0 or player_y <= 0 or player_y >= HEIGHT or player_x >= WIDTH:
        print('GAME OVER')
        exit(0)


def eat_apple(x_player, y_player, x_apple, y_apple):
    global your_score
    x1_player, y1_player, w_player, h_player = x_player, y_player, 15, 25
    x2_player = x1_player + w_player
    y2_player = y1_player + h_player

    x1_apple, y1_apple, w_apple, h_apple = x_apple, y_apple, 15, 15
    x2_apple = x1_apple + w_apple
    y2_apple = y1_apple + h_apple

    s1 = (x1_player >= x1_apple and x1_player <= x2_apple) or (x2_player >= x1_apple and x2_player <= x2_apple)
    s2 = (y1_player >= y1_apple and y1_player <= y2_apple) or (y2_player >= y1_apple and y2_player <= y2_apple)
    s3 = (x1_apple >= x1_player and x1_apple <= x2_player) or (x2_apple >= x1_player and x2_apple <= x2_player)
    s4 = (y1_apple >= y1_player and y1_apple <= y2_player) or (y2_apple >= y1_player and y2_apple <= y2_player)

    if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
        your_score += 10
        return True
    return False


def new_size_snake(player_x, player_y):
    where_head()
    pass


def where_head():
    global poz_x, pox_y, player_speed
    if poz_x:
        if player_speed < 0:
            return 'UP'
        else:
            return 'DOWN'
    else:
        if player_speed < 0:
            return 'LEFT'
        else:
            return 'RIGHT'


# В класс game
WIDTH = 800
HEIGHT = 650
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
FPS = 50
teta = pygame.transform.scale(pygame.image.load("textures\img.png"), (800, 650))
your_score = 0


# В класс snake
vx = 0
vy = 0
player_x = WIDTH / 2
player_y = HEIGHT / 2
player_speed = 2
poz_x = False
poz_y = False

# В класс apple
col_apples = 0
x_apple = 0
y_apple = 0

# def main():
running = True

while running:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                if not poz_x:
                    vx = -player_speed
                    poz_x = True
                    poz_y = False
            elif e.key == pygame.K_RIGHT:
                if not poz_x:
                    vx = player_speed
                    poz_x = True
                    poz_y = False
            if e.key == pygame.K_UP:
                if not poz_y:
                    vy = -player_speed
                    poz_x = False
                    poz_y = True
            elif e.key == pygame.K_DOWN:
                if not poz_y:
                    vy = player_speed
                    poz_x = False
                    poz_y = True

    in_game()
    eat_apple(player_x, player_y, x_apple, y_apple)
    clock.tick(FPS)
    display.blit(teta, (0, 0))
    make_textures()

    pygame.display.flip()

# main()