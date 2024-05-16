# Імпортуємо важливі функції
import pygame
import random

pygame.init()

scale = 7

WINDOW_WIDTH = 140 * scale
WINDOW_HEIGHT = 140 * scale

TILE_SIZE = 14 * scale
OFFSET = 1 * scale

YELLOW = (255, 186, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 30

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("funny run")
pygame.display.set_icon(pygame.image.load("game_files/icon.png"))

moving_up = True
moving_down = False
moving_left = False
moving_right = False

direction = "1"
position = "up"
score = 0
max_score = 0
coins = 0

car_position_1_x = 0
car_position_1_y = 78 * scale
car_position_2_x = 0
car_position_2_y = 50 * scale
car_type = "1"

background_height = 140 * scale
background_y_1 = 0
background_y_2 = -background_height
gamemode = "game"
background_list = ['map 1', 'map 2', 'map 3', 'map 4']
map_1 = random.choice(background_list)
map_2 = random.choice(background_list)
background_1 = pygame.image.load(f"game_files/images/bg/{gamemode}/{map_1}.png")
background_2 = pygame.image.load(f"game_files/images/bg/{gamemode}/{map_2}.png")
background_1 = pygame.transform.scale(background_1, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_2 = pygame.transform.scale(background_2, (WINDOW_WIDTH, WINDOW_HEIGHT))

sprite_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(sprite_spawn_timer, 1500)

run = True

game = True


def draw_bg():
    global score, max_score
    if score > max_score:
        max_score = score
    font = pygame.font.Font(None, 8 * scale)
    score_text = font.render(f"Очки: {score}", False, WHITE)
    window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10 * scale, 10 * scale))
    max_score_text = font.render(f"Рекорд: {max_score}", True, BLACK)
    window.blit(max_score_text, (WINDOW_WIDTH - max_score_text.get_width() - 10 * scale, 16 * scale))
    coins_text = font.render(f"Монети: {coins}", True, YELLOW)
    window.blit(coins_text, (WINDOW_WIDTH - coins_text.get_width() - 10 * scale, 22 * scale))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.direction = direction
        self.position = position
        self.load_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x * scale, y * scale)

    def load_image(self):
        for i in range(2):
            img = pygame.image.load(f"game_files/images/sprites/player/{self.direction}/{self.position}/{i}.png")
            image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animation_list.append(image)
        self.image = self.animation_list[self.frame_index]

    def update(self):
        self.load_image()
        if self.rect.y > WINDOW_HEIGHT:
            self.rect.y -= 14 * scale
        if self.rect.x > WINDOW_WIDTH:
            self.rect.x -= 14 * scale
        if self.rect.x < 0:
            self.rect.x += 14 * scale

    def update_animation(self):
        animation_cooldown = 500
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def move_to_tile(self, dx=0, dy=0):
        global moving_up, moving_down, moving_left, moving_right, score
        if dx > 0:
            self.position = "right"
            self.animation_list.clear()
            self.frame_index = 0
            moving_right = True
            moving_up = False
            moving_down = False
            moving_left = False
        elif dx < 0:
            self.position = "left"
            self.animation_list.clear()
            self.frame_index = 0
            moving_left = True
            moving_up = False
            moving_down = False
            moving_right = False
        elif dy > 0:
            score -= 1
            self.position = "down"
            self.animation_list.clear()
            self.frame_index = 0
            moving_down = True
            moving_up = False
            moving_left = False
            moving_right = False
        elif dy < 0:
            score += 1
            self.position = "up"
            self.animation_list.clear()
            self.frame_index = 0
            moving_up = True
            moving_down = False
            moving_left = False
            moving_right = False
        # правило переміщення
        new_x = ((self.rect.x + dx + OFFSET) // TILE_SIZE) * TILE_SIZE
        if moving_left or moving_right:
            self.rect.x = new_x + OFFSET
            self.rect.y = self.rect.y
        if moving_up:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y - TILE_SIZE
        if moving_down:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y + TILE_SIZE

    def draw(self):
        window.blit(self.image, self.rect)


class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position_list = [(car_position_1_x, car_position_1_y), (car_position_2_x, car_position_2_y)]
        self.active_cars = []  # Список активних автомобілів
        self.spawn_index = 0
        self.update_time = pygame.time.get_ticks()
        self.type = car_type
        self.load_image()

    def load_image(self):
        img = pygame.image.load(f"game_files/images/sprites/other/cars/{self.type}.png")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))

    def update(self):
        self.load_image()

    def update_position(self):
        car_animation_cooldown = 3000
        if pygame.time.get_ticks() - self.update_time > car_animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            new_car = self.create_car()
            self.active_cars.append(new_car)

    def create_car(self):
        car_rect = self.image.get_rect()
        car_rect.center = self.position_list[self.spawn_index]
        self.spawn_index = (self.spawn_index + 1) % len(
            self.position_list)  # Це, щоб постійно перемикатись між місцями для спавну
        return car_rect

    def draw(self):
        for car_rect in self.active_cars:
            window.blit(self.image, car_rect)


player = Player(49.4, 133.4)
car = Car()
