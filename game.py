import pygame
import random


class Snake():
    def __init__(self):
        self.vx = 0
        self.vy = 0
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT // 2
        self.snake_head = [self.player_x, self.player_y]
        self.poz_x = False
        self.poz_y = False

    def create_snake(self, surface, w, h, color):
        global snake_body
        for i in snake_body:
            rect = pygame.Rect(i[0], i[1], w, h)
            pygame.draw.rect(surface, color, rect)
        return

    def in_game(self):
        global snake_body
        for i in snake_body:
            #print(i[0], i[1])
            if self.poz_x:
                i[0] += self.vx
            if self.poz_y:
                i[1] += self.vy
            if i[0] <= 0 or i[1] <= 0 or i[1] >= HEIGHT - 10 or i[0] >= WIDTH - 10:
                print('GAME OVER')
                exit(0)

    def new_size_snake(self, player_x, player_y):
        self.where_head()
        pass

    def where_head(self):
        global player_speed
        if self.poz_x:
            if player_speed < 0:
                return 'UP'
            else:
                return 'DOWN'
        else:
            if player_speed < 0:
                return 'LEFT'
            else:
                return 'RIGHT'


class Apple(Snake):
    def __init__(self):
        super().__init__()
        self.col_apples = 0
        self.x_apple = 0
        self.y_apple = 0

    def random_coords(self):
        x1 = random.randint(10, WIDTH - 10)
        y1 = random.randint(10, HEIGHT - 10)
        return x1, y1

    def make_apples(self, surface, x1, y1):
        global player_speed
        if self.eat_apple(x1, y1, self.x_apple, self.y_apple):
            self.col_apples = 0
            self.new_size_snake(self.player_x, self.player_y)
            if player_speed <= 8:
                player_speed += 0.25
        if self.col_apples == 0:
            self.x_apple, self.y_apple = self.random_coords()
            rect_apple = pygame.Rect(self.x_apple, self.y_apple, 12, 12)
        else:
            rect_apple = pygame.Rect(self.x_apple, self.y_apple, 12, 12)
        pygame.draw.rect(surface, (0, 255, 0), rect_apple)
        self.col_apples += 1
        return rect_apple

    def eat_apple(self, x_player, y_player, x_apple, y_apple):
        global your_score, snake_body
        for i in snake_body:
            print(i[0], i[1])
            x1_player, y1_player, w_player, h_player = i[0], i[1], 15, 15
            x2_player = x1_player + w_player
            y2_player = y1_player + h_player

            x1_apple, y1_apple, w_apple, h_apple = self.x_apple, self.y_apple, 15, 15
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


def main():
    global running
    while running:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    if not snake.poz_x:
                        snake.vx = -player_speed
                        snake.poz_x = True
                        snake.poz_y = False
                elif e.key == pygame.K_RIGHT:
                    if not snake.poz_x:
                        snake.vx = player_speed
                        snake.poz_x = True
                        snake.poz_y = False
                if e.key == pygame.K_UP:
                    if not snake.poz_y:
                        snake.vy = -player_speed
                        snake.poz_x = False
                        snake.poz_y = True
                elif e.key == pygame.K_DOWN:
                    if not snake.poz_y:
                        snake.vy = player_speed
                        snake.poz_x = False
                        snake.poz_y = True

        snake.in_game()
        clock.tick(FPS)
        display.blit(teta, (0, 0))
        snake.create_snake(display, 15, 15, (255, 0, 0))
        apple.make_apples(display, snake.player_x, snake.player_y)
        pygame.display.flip()


WIDTH = 800
HEIGHT = 650
player_speed = 2
running = True
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
FPS = 50
apple = Apple()
snake = Snake()
snake_body = [[snake.player_x, snake.player_y]]
teta = pygame.transform.scale(pygame.image.load("textures\img.png"), (800, 650))
your_score = 0
main()