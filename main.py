import pygame
from random import randint
import time


class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.score = 0
        self.play_surface = pygame.display.set_mode((870, 630))
        self.x_button = 150
        self.y_button = 250
        self.w_button = 130
        self.h_button = 65

    def set_title(self):
        self.play_surface = pygame.display.set_mode((870, 630))

    def start_screen(self):
        intro_text = ["                 Змейка",
                      "Кликните тобы начать игру", ]
        button_text = ["Таблица", "лидеров"]

        fon = pygame.transform.scale(pygame.image.load('textures\img.png'), (870, 630))
        self.play_surface.blit(fon, (0, 0))
        font = pygame.font.Font(None, 60)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, True, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 100
            text_coord += intro_rect.height
            self.play_surface.blit(string_rendered, intro_rect)
        first_button = pygame.draw.rect(self.play_surface, (255, 255, 255), (150, 250, 130, 65))
        text_coord = 250
        font2 = pygame.font.Font(None, 30)
        for line2 in button_text:
            string_rendered = font2.render(line2, True, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 170
            text_coord += intro_rect.height
            self.play_surface.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x > self.x_button and x < self.x_button + self.w_button and \
                            y > self.y_button and y < self.y_button + self.h_button:
                        print('yes')
                    else:
                        return
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()
            self.clock.tick(60)

    def show_score(self, choice=1):
        s_font = pygame.font.SysFont('consolas', 24)
        s_surf = s_font.render(
            'Score ' + str(self.score), True, pygame.Color('black'))
        s_rect = s_surf.get_rect()
        if choice == 1:
            s_rect.midtop = (80, 10)
        else:
            s_rect.midtop = (360, 120)
        self.play_surface.blit(s_surf, s_rect)

    def events(self, change_to):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
        return change_to

    def game_over(self):
        self.end_screen()

    def end_screen(self):
        intro_text = ["Нажмите любую кнопку для продолжения"]

        fon = pygame.transform.scale(pygame.image.load('textures\img_1.png'), (870, 630))
        self.play_surface.blit(fon, (0, 0))
        font = pygame.font.Font(None, 40)
        text_coord = 350

        string_rendered = font.render('Ваш счёт: ' + str(self.score), True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 50
        intro_rect.x = 130
        text_coord += intro_rect.height
        self.play_surface.blit(string_rendered, intro_rect)

        for line in intro_text:
            string_rendered = font.render(line, True, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = text_coord
            intro_rect.x = 130
            text_coord += intro_rect.height
            self.play_surface.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    main()
            pygame.display.flip()
            self.clock.tick(60)


class Snake():
    def __init__(self):
        self.snake_head_pos = [360, 240]
        self.snake_body = [[360, 240]]
        self.snake_color = pygame.Color(255, 0, 0)
        self.direction = ''
        self.change_to = self.direction

    def my_direction(self):
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def where_head(self):
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 15
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 15
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 15
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 15

    def body_mechanism(
            self, score, food_pos, screen_width, screen_height):
        self.snake_body.insert(0, list(self.snake_head_pos))
        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):
            food_pos = [randint(1, 855 // 15) * 15,
                        randint(1, 615 // 15) * 15]
            score += 1
        else:
            del self.snake_body[-1]
        return score, food_pos

    def draw_snake(self, play_surface, surface_color):
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(
                play_surface, self.snake_color, pygame.Rect(
                    pos[0], pos[1], 15, 15))

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        if self.snake_head_pos[0] > screen_width - 15 or self.snake_head_pos[0] < 0\
                or self.snake_head_pos[1] > screen_height - 15 or self.snake_head_pos[1] < 0:
            game_over()
        for block in self.snake_body[1:]:
            if block[0] == self.snake_head_pos[0] and block[1] == self.snake_head_pos[1]:
                game_over()


class Food():
    def __init__(self):
        self.food_color = pygame.Color(0, 255, 0)
        self.food_size_x = 15
        self.food_size_y = 15
        self.food_pos = [randint(1, 855 // 15) * 15, randint(1, 615 // 15) * 15]
        self.image = pygame.image.load("textures/apple.png")
        self.image1 = pygame.transform.scale(self.image, (15, 15))

    def draw_food(self, play_surface):
        play_surface.blit(self.image1, (self.food_pos[0], self.food_pos[1]))


def main():
    game = Game()
    snake = Snake()
    food = Food()
    game.start_screen()
    game.set_title()
    screen_width = 720
    screen_height = 460
    pygame.display.set_caption('Snake Game')

    while True:
        snake.change_to = game.events(snake.change_to)
        snake.my_direction()
        snake.where_head()
        game.score, food.food_pos = snake.body_mechanism(game.score, food.food_pos, 870, 630)
        snake.draw_snake(game.play_surface, (255, 255, 255))

        food.draw_food(game.play_surface)

        snake.check_for_boundaries(
            game.game_over, 870, 630)
        game.show_score()
        pygame.display.flip()
        game.clock.tick(10)


main()