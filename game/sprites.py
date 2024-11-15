# Імпорт бібліотек
import pygame
import json
import os

# Ініціалізація Pygame
pygame.init()

# Частота оновлення гри
clock = pygame.time.Clock()

# Масштабування
n = 5

# Анімація
anim_count = 0

# Ініціалізація розмірів вікна
WINDOW_WIDTH = 140 * n
WINDOW_HEIGHT = 140 * n

# Розмір плитки
TILE_SIZE = 14 * n
OFFSET = 1 * n

# Кольори
YELLOW = (255, 186, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Створення вікна гри
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("funny run")
pygame.display.set_icon(pygame.image.load("../game_files/icon.png"))

# Завантаження зображень
background_image_menu = pygame.image.load("../game_files/images/bg/menu/menu 1.png")
background_image_game_1 = pygame.image.load("../game_files/images/bg/game/map 1.png")
background_image_game_2 = pygame.image.load("../game_files/images/bg/game/map 2.png")
background_image_game_3 = pygame.image.load("../game_files/images/bg/game/map 3.png")
background_image_game_4 = pygame.image.load("../game_files/images/bg/game/map 4.png")
background_image_select_skin_menu = pygame.image.load("../game_files/images/bg/menu/menu 2.png")
background_image_select_location_menu = pygame.image.load("../game_files/images/bg/menu/menu 3.png")
background_image_help = pygame.image.load("../game_files/images/bg/menu/help.png")
background_image_gacha = pygame.image.load("../game_files/images/bg/game/home.png")
play_image = pygame.image.load("../game_files/images/sprites/buttons/play.png")
exit_image = pygame.image.load("../game_files/images/sprites/buttons/exit.png")
help_image = pygame.image.load("../game_files/images/bg/menu/help.png")
back_image = pygame.image.load("../game_files/images/sprites/buttons/back.png")
retry_image = pygame.image.load("../game_files/images/sprites/buttons/retry.png")
select_skin_image = pygame.image.load("../game_files/images/sprites/buttons/select skin.png")
player_image_1_button = pygame.image.load("../game_files/images/sprites/player/1/down/0.png")
player_image_2_button = pygame.image.load("../game_files/images/sprites/player/2/player down.png")
player_image_3_button = pygame.image.load("../game_files/images/sprites/player/3/player down.png")
player_image_1_down = pygame.image.load("../game_files/images/sprites/player/1/down/0.png")
player_image_2_down = pygame.image.load("../game_files/images/sprites/player/2/player down.png")
player_image_3_down = pygame.image.load("../game_files/images/sprites/player/3/player down.png")
player_image_1_up = pygame.image.load("../game_files/images/sprites/player/1/up/0.png")
player_image_2_up = pygame.image.load("../game_files/images/sprites/player/2/player up.png")
player_image_3_up = pygame.image.load("../game_files/images/sprites/player/3/player up.png")
player_image_1_left = pygame.image.load("../game_files/images/sprites/player/1/left/0.png")
player_image_2_left = pygame.image.load("../game_files/images/sprites/player/2/player left.png")
player_image_3_left = pygame.image.load("../game_files/images/sprites/player/3/player left.png")
player_image_1_right = pygame.image.load("../game_files/images/sprites/player/1/right/0.png")
player_image_2_right = pygame.image.load("../game_files/images/sprites/player/2/player right.png")
player_image_3_right = pygame.image.load("../game_files/images/sprites/player/3/player right.png")
wall_image_1 = pygame.image.load("../game_files/images/sprites/walls/wall 1.png")
wall_image_2 = pygame.image.load("../game_files/images/sprites/walls/wall 2.png")
wall_image_3 = pygame.image.load("../game_files/images/sprites/walls/wall 3 off.png")
wall_image_4 = pygame.image.load("../game_files/images/sprites/walls/wall 3 on.png")
wood_image = pygame.image.load("../game_files/images/sprites/other/wood.png")
car_image_1 = pygame.image.load("../game_files/images/sprites/other/cars/1.png")
car_image_2 = pygame.image.load("../game_files/images/sprites/other/cars/2.png")
train_image_1 = pygame.image.load("../game_files/images/sprites/other/train/train 1.png")
train_image_2 = pygame.image.load("../game_files/images/sprites/other/train/train 2.png")
lock_image = pygame.image.load("../game_files/images/sprites/buttons/lock.png")
buy_image = pygame.image.load("../game_files/images/sprites/buttons/buy.png")
meteor_image = pygame.image.load("../game_files/images/sprites/other/magma zone.png")
coin_image = pygame.image.load("../game_files/images/sprites/other/coin/1.png")
coin_boost_image = pygame.image.load("../game_files/images/sprites/other/coin/2.png")
select_location_image = pygame.image.load("../game_files/images/sprites/buttons/select map.png")
meteorits_off_image = pygame.image.load("../game_files/images/sprites/buttons/meteorits off.png")
meteorits_on_image = pygame.image.load("../game_files/images/sprites/buttons/meteorits on.png")
classical_image_button = pygame.image.load("../game_files/images/sprites/buttons/classical location.png")
river_image_1 = pygame.image.load("../game_files/images/sprites/other/river/river 1.png")
river_image_2 = pygame.image.load("../game_files/images/sprites/other/river/river 2.png")
easter_image_button = pygame.image.load("../game_files/images/sprites/buttons/easter location.png")

# Ініціалізація звуків
city = pygame.mixer.Sound("../game_files/sounds/city.mp3")
die = pygame.mixer.Sound("../game_files/sounds/die.mp3")
car_die = pygame.mixer.Sound("../game_files/sounds/car.mp3")
river_die = pygame.mixer.Sound("../game_files/sounds/river.mp3")
coin_sound = pygame.mixer.Sound("../game_files/sounds/coin.mp3")
boost_sound = pygame.mixer.Sound("../game_files/sounds/boost.mp3")

# Масштабування зображень
background_image_menu = pygame.transform.scale(background_image_menu, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_game_1 = pygame.transform.scale(background_image_game_1, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_game_2 = pygame.transform.scale(background_image_game_2, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_game_3 = pygame.transform.scale(background_image_game_3, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_game_4 = pygame.transform.scale(background_image_game_4, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_gacha = pygame.transform.scale(background_image_gacha, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_help = pygame.transform.scale(background_image_help, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_select_skin_menu = pygame.transform.scale(background_image_select_skin_menu, (WINDOW_WIDTH,
                                                                                               WINDOW_HEIGHT))
background_image_select_location_menu = pygame.transform.scale(background_image_select_location_menu,
                                                               (WINDOW_WIDTH, WINDOW_HEIGHT))
play_image = pygame.transform.scale(play_image, (56 * n, 14 * n))
exit_image = pygame.transform.scale(exit_image, (56 * n, 14 * n))
help_image = pygame.transform.scale(help_image, (56 * n, 14 * n))
back_image = pygame.transform.scale(back_image, (56 * n, 14 * n))
retry_image = pygame.transform.scale(retry_image, (28 * n, 12 * n))
select_skin_image = pygame.transform.scale(select_skin_image, (12 * n, 12 * n))
player_image_1_down = pygame.transform.scale(player_image_1_down, (12 * n, 12 * n))
player_image_1_up = pygame.transform.scale(player_image_1_up, (12 * n, 12 * n))
player_image_1_left = pygame.transform.scale(player_image_1_left, (12 * n, 12 * n))
player_image_1_right = pygame.transform.scale(player_image_1_right, (12 * n, 12 * n))
player_image_2_down = pygame.transform.scale(player_image_2_down, (12 * n, 12 * n))
player_image_2_up = pygame.transform.scale(player_image_2_up, (12 * n, 12 * n))
player_image_2_left = pygame.transform.scale(player_image_2_left, (12 * n, 12 * n))
player_image_2_right = pygame.transform.scale(player_image_2_right, (12 * n, 12 * n))
player_image_3_down = pygame.transform.scale(player_image_3_down, (12 * n, 12 * n))
player_image_3_up = pygame.transform.scale(player_image_3_up, (12 * n, 12 * n))
player_image_3_left = pygame.transform.scale(player_image_3_left, (12 * n, 12 * n))
player_image_3_right = pygame.transform.scale(player_image_3_right, (12 * n, 12 * n))
wall_image_1 = pygame.transform.scale(wall_image_1, (12 * n, 12 * n))
wall_image_2 = pygame.transform.scale(wall_image_2, (12 * n, 12 * n))
wall_image_3 = pygame.transform.scale(wall_image_3, (12 * n, 12 * n))
wall_image_4 = pygame.transform.scale(wall_image_4, (12 * n, 12 * n))
wood_image = pygame.transform.scale(wood_image, (28 * n, 14 * n))
car_image_1 = pygame.transform.scale(car_image_1, (14 * n, 12 * n))
car_image_2 = pygame.transform.scale(car_image_2, (28 * n, 12 * n))
train_image_1 = pygame.transform.scale(train_image_1, (140 * n, 12 * n))
train_image_2 = pygame.transform.scale(train_image_2, (140 * n, 12 * n))
player_image_1_button = pygame.transform.scale(player_image_1_button, (12 * n * 2, 12 * n * 2))
player_image_2_button = pygame.transform.scale(player_image_2_button, (12 * n * 2, 12 * n * 2))
player_image_3_button = pygame.transform.scale(player_image_3_button, (12 * n * 2, 12 * n * 2))
lock_image = pygame.transform.scale(lock_image, (12 * n * 2, 12 * n * 2))
buy_image = pygame.transform.scale(buy_image, (12 * n * 2, 12 * n * 2))
meteor_image = pygame.transform.scale(meteor_image, (42 * n, 42 * n))
coin_image = pygame.transform.scale(coin_image, (10 * n, 10 * n))
coin_boost_image = pygame.transform.scale(coin_boost_image, (10 * n, 10 * n))
select_location_image = pygame.transform.scale(select_location_image, (12 * n, 12 * n))
meteorits_off_image = pygame.transform.scale(meteorits_off_image, (12 * n, 12 * n))
meteorits_on_image = pygame.transform.scale(meteorits_on_image, (12 * n, 12 * n))
classical_image_button = pygame.transform.scale(classical_image_button, (12 * n * 2, 12 * n * 2))
river_image_1 = pygame.transform.scale(river_image_1, (140 * n, 14 * n))
river_image_2 = pygame.transform.scale(river_image_2, (140 * n, 14 * n))
easter_image_button = pygame.transform.scale(easter_image_button, (12 * n * 2, 12 * n * 2))
river = [
    river_image_1,
    river_image_2
]
train = [
    train_image_1,
    train_image_2
]

# Ініціалізація прямокутників для кнопок та гравця
play_rect = play_image.get_rect(center=(WINDOW_WIDTH // 1.9, WINDOW_HEIGHT // 1.9))
player_rect = player_image_1_up.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - player_image_1_up.get_height() // 2)
                                         )
exit_rect = exit_image.get_rect(center=(WINDOW_WIDTH // 1.9, WINDOW_HEIGHT // 1.1))
help_rect = help_image.get_rect(center=(WINDOW_WIDTH // 1.9, WINDOW_HEIGHT // 1.5))
back_rect = back_image.get_rect(center=(WINDOW_WIDTH // 1.9, WINDOW_HEIGHT // 1.1))
retry_rect = retry_image.get_rect(center=(WINDOW_WIDTH // 8, WINDOW_HEIGHT // 1.05))
select_rect = select_skin_image.get_rect(center=(WINDOW_WIDTH // 3.5, WINDOW_HEIGHT // 1.05))
player_button_rect = player_image_1_button.get_rect(center=(28 * n, 98 * n))
player_2_button_rect = player_image_2_button.get_rect(center=(70 * n, 98 * n))
player_3_button_rect = player_image_3_button.get_rect(center=(112 * n, 98 * n))
location_image_rect = select_location_image.get_rect(center=(133 * n, 133 * n))
meteorits_on_off_rect = meteorits_off_image.get_rect(center=(127 * n, 98 * n))
classical_image_button_rect = classical_image_button.get_rect(center=(28 * n, 98 * n))
easter_image_button_rect = easter_image_button.get_rect(center=(84 * n, 96 * n))
wood_rects = []
river_rects = []
train_rects = []
car_rects_1 = []
car_rects_2 = []
wall_rects_1 = []
meteor_rect = (-10000, -10000)
coin_rect = (-10000, -10000)

# Ініціалізація швидкостей
WOOD_SPEED = -0.6 * n
WOOD_2_SPEED = 0.6 * n
CAR_SPEED = -0.6 * n
CAR_2_SPEED = -0.8 * n

# Ініціалізація станів різних об'єктів
location_classic = False
location_easter = False
in_game_1 = False
in_game_2 = False
gacha = False
main_menu = True
help_menu = False
select_skin_menu = False
select_location_menu = False
skin_1 = True
skin_2 = False
skin_3 = False
skin_in_1 = True
skin_in_2 = False
skin_in_3 = False
wall_rects_2_anim = False
timer_started = False
object_created = False
METEORITS = False
meteor_1 = False
meteor_2 = False
meteor_3 = False
meteor_4 = False
COINS = True
coin_on_1 = False
coin_on_2 = False
coin_on_3 = False
coin_on_4 = False
player_up = True
player_down = False
player_right = False
player_left = False
player_on_wood = False
wood_player_is_on = None
texting = False
boost = False

# Ініціалізація даних гри
numbers = [1, 2, 3, 4]

map_1_spawn_car = 0

score = 0
max_score = 0
coins = 0

start_time = 0
delay_create = 1
delay_remove = 5

initial_player_pos = (57 * n, 127 * n)

# Ініціалізація шрифту
font = pygame.font.Font(None, 8 * n)

# Таймер для спавну спрайтів
sprite_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(sprite_spawn_timer, 2000)

city.play(-1)

# Завантаження даних гравця
data_file_name = "../game_files/data.json"
name = ""

if os.path.exists(data_file_name):
    with open(data_file_name, "r") as file:
        data = json.load(file)
        if "players" not in data:
            data["players"] = {}
        if "NAME" in data:
            name = data["NAME"]
else:
    # Створення нового файлу з даними
    with open(data_file_name, "w") as file:
        data = {"players": {}}
        json.dump(data, file)


# Збереження даних гравця
def save_data():
    with open(data_file_name, "w") as FILE:
        json.dump(data, FILE)


# Переміщення гравця на плитку
def move_player_to_tile(dx=0, dy=0):
    global player_rect

    new_x = ((player_rect.x + dx + OFFSET) // TILE_SIZE) * TILE_SIZE
    new_y = ((player_rect.y + dy + OFFSET) // TILE_SIZE) * TILE_SIZE

    player_rect.x = new_x + OFFSET
    player_rect.y = new_y + OFFSET


# Скидання гри
def reset_game():
    global score, player_rect, car_rects_1, wood_rects, car_rects_2, river_rects, \
        wall_rects_1, train_rects, boost
    global sprite_spawn_timer

    player_rect.topleft = initial_player_pos

    car_rects_1.clear()
    wood_rects.clear()
    car_rects_2.clear()
    wall_rects_1.clear()
    river_rects.clear()
    train_rects.clear()

    car_rects_1 = []
    wood_rects = []
    car_rects_2 = []
    wall_rects_1 = []
    river_rects = []
    train_rects = []

    boost = False

    pygame.time.set_timer(sprite_spawn_timer, 0)

    pygame.time.set_timer(sprite_spawn_timer, 2000)
