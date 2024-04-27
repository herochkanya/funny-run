import pygame
import random
import json
import os

pygame.init()

n = 5

clock = pygame.time.Clock()

anim_count = 0

WINDOW_WIDTH = 140 * n
WINDOW_HEIGHT = 140 * n

TILE_SIZE = 14 * n
OFFSET = 1 * n

YELLOW = (255, 186, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("funny run")

background_image_menu = pygame.image.load("menu.png")
background_image_game = pygame.image.load("map 1.png")
background_image_game_2 = pygame.image.load("map 2.png")
background_image_game_3 = pygame.image.load("map 3.png")
background_image_game_4 = pygame.image.load("map 4.png")
background_image_select_menu = pygame.image.load("menu 2.png")
background_image_location_menu = pygame.image.load("menu 3.png")
button_image = pygame.image.load("play.png")
exit_image = pygame.image.load("exit.png")
retry_image = pygame.image.load("retry.png")
select_image = pygame.image.load("select.png")
player_image_button = pygame.image.load("slime 1.png")
player_image_2_button = pygame.image.load("slime 2.png")
player_image_3_button = pygame.image.load("slime 3.png")
player_image = pygame.image.load("slime 1.png")
player_image_2 = pygame.image.load("slime 2.png")
player_image_3 = pygame.image.load("slime 3.png")
player_image_back = pygame.image.load("slime 1 back.png")
player_image_2_back = pygame.image.load("slime 2 back.png")
player_image_3_back = pygame.image.load("slime 3 back.png")
player_image_left = pygame.image.load("slime 1 left.png")
player_image_2_left = pygame.image.load("slime 2 left.png")
player_image_3_left = pygame.image.load("slime 3 left.png")
player_image_right = pygame.image.load("slime 1 right.png")
player_image_2_right = pygame.image.load("slime 2 right.png")
player_image_3_right = pygame.image.load("slime 3 right.png")
wall_image = pygame.image.load("wall.png")
wall_image_2 = pygame.image.load("wall 2.png")
wall_image_3 = pygame.image.load("wall 3.png")
wall_image_4 = pygame.image.load("wall 4.png")
wood_image = pygame.image.load("wood.png")
car_image = pygame.image.load("car.png")
train_image = pygame.image.load("train.png")
lock_image = pygame.image.load("lock 1.png")
lock_2_image = pygame.image.load("lock 2.png")
meteor_image = pygame.image.load("magma.png")
coin_image = pygame.image.load("coin.png")
location_image = pygame.image.load("mode.png")
meteorits_off_image = pygame.image.load("meteorits off.png")
meteorits_on_image = pygame.image.load("meteorits on.png")
classical_image_button = pygame.image.load("location 1.png")
river_image_1 = pygame.image.load("river/river.gif")
river_image_2 = pygame.image.load("river/river 2.png")


city = pygame.mixer.Sound("city.mp3")
die = pygame.mixer.Sound("die.mp3")

background_image_menu = pygame.transform.scale(background_image_menu, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_game = pygame.transform.scale(background_image_game, (WINDOW_WIDTH, WINDOW_HEIGHT))
button_image = pygame.transform.scale(button_image, (56 * n, 14 * n))
player_image = pygame.transform.scale(player_image, (12 * n, 12 * n))
player_image_back = pygame.transform.scale(player_image_back, (12 * n, 12 * n))
player_image_left = pygame.transform.scale(player_image_left, (12 * n, 12 * n))
player_image_right = pygame.transform.scale(player_image_right, (12 * n, 12 * n))
player_image_2_back = pygame.transform.scale(player_image_2_back, (12 * n, 12 * n))
player_image_2_left = pygame.transform.scale(player_image_2_left, (12 * n, 12 * n))
player_image_2_right = pygame.transform.scale(player_image_2_right, (12 * n, 12 * n))
player_image_3_back = pygame.transform.scale(player_image_3_back, (12 * n, 12 * n))
player_image_3_left = pygame.transform.scale(player_image_3_left, (12 * n, 12 * n))
player_image_3_right = pygame.transform.scale(player_image_3_right, (12 * n, 12 * n))
wall_image = pygame.transform.scale(wall_image, (12 * n, 12 * n))
wood_image = pygame.transform.scale(wood_image, (28 * n, 14 * n))
car_image = pygame.transform.scale(car_image, (14 * n, 12 * n))
exit_image = pygame.transform.scale(exit_image, (56 * n, 14 * n))
wall_image_2 = pygame.transform.scale(wall_image_2, (12 * n, 12 * n))
background_image_game_2 = pygame.transform.scale(background_image_game_2, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_game_3 = pygame.transform.scale(background_image_game_3, (WINDOW_WIDTH, WINDOW_HEIGHT))
wall_image_3 = pygame.transform.scale(wall_image_3, (12 * n, 12 * n))
wall_image_4 = pygame.transform.scale(wall_image_4, (12 * n, 12 * n))
train_image = pygame.transform.scale(train_image, (140 * n, 12 * n))
retry_image = pygame.transform.scale(retry_image, (28 * n, 12 * n))
select_image = pygame.transform.scale(select_image, (12 * n, 12 * n))
background_image_select_menu = pygame.transform.scale(background_image_select_menu, (WINDOW_WIDTH, WINDOW_HEIGHT))
player_image_button = pygame.transform.scale(player_image_button, (12 * n * 2, 12 * n * 2))
player_image_2_button = pygame.transform.scale(player_image_2_button, (12 * n * 2, 12 * n * 2))
player_image_3_button = pygame.transform.scale(player_image_3_button, (12 * n * 2, 12 * n * 2))
player_image_2 = pygame.transform.scale(player_image_2, (12 * n, 12 * n))
player_image_3 = pygame.transform.scale(player_image_3, (12 * n, 12 * n))
background_image_game_4 = pygame.transform.scale(background_image_game_4, (WINDOW_WIDTH, WINDOW_HEIGHT))
lock_image = pygame.transform.scale(lock_image, (12 * n * 2, 12 * n * 2))
lock_2_image = pygame.transform.scale(lock_2_image, (12 * n * 2, 12 * n * 2))
meteor_image = pygame.transform.scale(meteor_image, (42 * n, 42 * n))
coin_image = pygame.transform.scale(coin_image, (12 * n, 12 * n))
background_image_location_menu = pygame.transform.scale(background_image_location_menu, (WINDOW_WIDTH, WINDOW_HEIGHT))
location_image = pygame.transform.scale(location_image, (12 * n, 12 * n))
meteorits_off_image = pygame.transform.scale(meteorits_off_image, (12 * n, 12 * n))
meteorits_on_image = pygame.transform.scale(meteorits_on_image, (12 * n, 12 * n))
classical_image_button = pygame.transform.scale(classical_image_button, (12 * n * 2, 12 * n * 2))
river_image_1 = pygame.transform.scale(river_image_1, (140 * n, 14 * n))
river_image_2 = pygame.transform.scale(river_image_2, (140 * n, 14 * n))

river = [
    river_image_1,
    river_image_2
]

button_rect = button_image.get_rect(center=(WINDOW_WIDTH // 1.9, WINDOW_HEIGHT // 1.9))
player_rect = player_image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - player_image.get_height() // 2))
exit_rect = exit_image.get_rect(center=(WINDOW_WIDTH // 1.9, WINDOW_HEIGHT // 1.5))
retry_rect = retry_image.get_rect(center=(WINDOW_WIDTH // 8, WINDOW_HEIGHT // 1.05))
select_rect = select_image.get_rect(center=(WINDOW_WIDTH // 3.5, WINDOW_HEIGHT // 1.05))
player_button_rect = player_image_button.get_rect(center=(28 * n, 98 * n))
player_2_button_rect = player_image_2_button.get_rect(center=(70 * n, 98 * n))
player_3_button_rect = player_image_3_button.get_rect(center=(112 * n, 98 * n))
location_image_rect = location_image.get_rect(center=(133 * n, 133 * n))
meteorits_on_off_rect = meteorits_off_image.get_rect(center=(127 * n, 98 * n))
classical_image_button_rect = classical_image_button.get_rect(center=(28 * n, 98 * n))

wood_rects = []

WOOD_SPEED = -WINDOW_WIDTH / 28 + 18 / 28 + 18

car_rects = []
car_rects_2 = []
car_rects_3 = []

CAR_SPEED = -WINDOW_WIDTH / 30 / 28 - 6

wall_rects_2 = []

meteor_rect = (-10000, -10000)
coin_rect = (-10000, -10000)

skin_1 = True
skin_2 = False
skin_3 = False
skin_in_1 = True
skin_in_2 = False
skin_in_3 = False

in_game_4 = False
in_game_3 = False
in_game_2 = False
in_game = False
menu = True
wall_rects_2_i = False
select_skin_menu = False
location_menu = False

timer_started = False
start_time = 0
delay_create = 1
delay_remove = 5
object_created = False
meteorits = False
meteor = False
meteor_2 = False
meteor_3 = False
meteor_4 = False

coion_1 = False
coion_2 = False
coion_3 = False
coion_4 = False

player_up = True
player_down = False
player_right = False
player_left = False

location_classic = True
location_easter = False

numbers = [1, 2, 3, 4]

score = 0
max_score = 0

coins = 0

initial_player_pos = (57 * n, 127 * n)

font = pygame.font.Font(None, 8 * n)

car_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(car_spawn_timer, 3000)

car_spawn_timer_2 = pygame.USEREVENT + 3
pygame.time.set_timer(car_spawn_timer_2, 3000)

wood_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(wood_spawn_timer, 900)

wood_spawn_timer_2 = pygame.USEREVENT + 8
pygame.time.set_timer(wood_spawn_timer_2, 2000)

light_spawn_timer = pygame.USEREVENT + 2
pygame.time.set_timer(light_spawn_timer, 100)

light_spawn_2_timer = pygame.USEREVENT + 3
pygame.time.set_timer(light_spawn_timer, 100)

light_spawn_3_timer = pygame.USEREVENT + 8
pygame.time.set_timer(light_spawn_timer, 8000)

city.play(-1)

player_on_wood = False
wood_player_is_on = None

data_file_name = "data.json"
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


def save_data():
    with open(data_file_name, "w") as file:
        json.dump(data, file)


def move_player_to_tile(dx=0, dy=0):
    global player_rect

    new_x = ((player_rect.x + dx + OFFSET) // TILE_SIZE) * TILE_SIZE
    new_y = ((player_rect.y + dy + OFFSET) // TILE_SIZE) * TILE_SIZE

    player_rect.x = new_x + OFFSET
    player_rect.y = new_y + OFFSET


def reset_game():
    global score, player_rect, car_rects, wood_rects, car_rects_2, car_rects_3, wall_rects, river_rects, wall_rects_2, \
        train_rects, wall_rects_3
    global car_spawn_timer, wood_spawn_timer, car_spawn_timer_2, wood_spawn_timer_2, \
        light_spawn_timer

    player_rect.topleft = initial_player_pos

    car_rects = []
    wood_rects = []
    car_rects_2 = []
    car_rects_3 = []
    wall_rects = []
    river_rects = []
    wall_rects_2 = []
    train_rects = []
    wall_rects_3 = []

    pygame.time.set_timer(car_spawn_timer, 0)
    pygame.time.set_timer(wood_spawn_timer, 0)
    pygame.time.set_timer(car_spawn_timer_2, 0)
    pygame.time.set_timer(wood_spawn_timer_2, 0)
    pygame.time.set_timer(light_spawn_timer, 0)

    pygame.time.set_timer(car_spawn_timer, 3000)
    pygame.time.set_timer(wood_spawn_timer, 900)
    pygame.time.set_timer(car_spawn_timer_2, 3000)
    pygame.time.set_timer(wood_spawn_timer_2, 2000)
    pygame.time.set_timer(light_spawn_timer, 100)


running = True
while running:
    current_time = pygame.time.get_ticks() / 1000
    current_time_2 = pygame.time.get_ticks() / 1100
    if score >= max_score:
        max_score = score
    if max_score >= 11:
        skin_2 = True
    if max_score >= 50:
        skin_3 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                in_game = False
                in_game_2 = False
                in_game_3 = False
                in_game_4 = False
                menu = True

            if event.key == pygame.K_LEFT:
                player_up = False
                player_left = True
                player_down = False
                player_right = False
                if player_on_wood:
                    temp_rect = player_rect.move(-TILE_SIZE, 0)
                    if not any(temp_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                        player_rect.move_ip(-TILE_SIZE, 0)
                else:
                    # Звичайний рух гравця ліворуч
                    temp_rect = player_rect.move(-TILE_SIZE, 0)
                    # Перевіряємо зіткнення з якоюсь зі стін
                    if not any(temp_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                        move_player_to_tile(dx=-TILE_SIZE)
                if player_rect.x < 0:
                    score = 0
                    player_rect.topleft = initial_player_pos
                    die.play()

            elif event.key == pygame.K_RIGHT:
                player_up = False
                player_left = False
                player_down = False
                player_right = True
                if player_on_wood:
                    temp_rect = player_rect.move(TILE_SIZE, 0)
                    if not any(temp_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                        player_rect.move_ip(TILE_SIZE, 0)
                else:
                    # Звичайний рух гравця праворуч
                    temp_rect = player_rect.move(TILE_SIZE, 0)
                    # Перевіряємо зіткнення з якоюсь зі стін
                    if not any(temp_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                        move_player_to_tile(dx=TILE_SIZE)
                if player_rect.x > WINDOW_WIDTH:
                    score = 0
                    player_rect.topleft = initial_player_pos
                    die.play()

            elif event.key == pygame.K_UP:
                player_up = True
                player_left = False
                player_down = False
                player_right = False
                temp_rect = player_rect.move(0, -TILE_SIZE)
                if not any(temp_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                    move_player_to_tile(dy=-TILE_SIZE)
                    score += 1
                if player_rect.y < 0:
                    random_choice = random.choice(numbers)
                    initial_player_pos = (57 * n, 127 * n)
                    player_rect.topleft = initial_player_pos
                    if random_choice == 1:
                        in_game = True
                        in_game_2 = False
                        in_game_3 = False
                        in_game_4 = False
                    elif random_choice == 2:
                        in_game_2 = True
                        in_game = False
                        in_game_3 = False
                        in_game_4 = False
                    elif random_choice == 3:
                        in_game_3 = True
                        in_game = False
                        in_game_2 = False
                        in_game_4 = False
                    elif random_choice == 4:
                        in_game_4 = True
                        in_game_3 = False
                        in_game = False
                        in_game_2 = False
                    reset_game()
                if player_on_wood:
                    player_on_wood = False
                    wood_player_is_on = None

            elif event.key == pygame.K_DOWN:
                player_up = False
                player_left = False
                player_down = True
                player_right = False
                temp_rect = player_rect.move(0, TILE_SIZE)
                if not any(temp_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                    move_player_to_tile(dy=TILE_SIZE)
                    score -= 1
                if player_rect.y >= WINDOW_HEIGHT:
                    score = 0
                    player_rect.topleft = initial_player_pos
                    die.play()
                if player_on_wood:
                    player_on_wood = False
                    wood_player_is_on = None

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (menu and not in_game and not in_game_2 and not in_game_3 and not in_game_4 and not select_skin_menu and
                    not location_menu and button_rect.collidepoint(event.pos)):
                if menu and button_rect.collidepoint(event.pos):
                    name = input("Enter your name: ")
                    # Перевіряємо, чи є вже таке ім'я в списку
                    if name not in data["players"]:
                        data["players"][name] = {"MAX_SCORE": 0, "COINS": 0}
                    else:
                        max_score = data["players"][name]["MAX_SCORE"]
                        coins = data["players"][name]["COINS"]
                    # Оновлення даних у файлі
                    with open(data_file_name, "w") as file:
                        json.dump(data, file)
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            if (menu and not in_game and not in_game_2 and not in_game_3 and not select_skin_menu and not in_game_4 and
                    not location_menu and exit_rect.collidepoint(event.pos)):
                if name in data["players"]:
                    data["players"][name]["MAX_SCORE"] = max_score
                    data["players"][name]["COINS"] = coins
                    save_data()
                else:
                    # Додавання нового запису для поточного гравця у списку data["players"]
                    data["players"][name] = {"NAME": name, "MAX_SCORE": score, "COINS": coins}
                    # Збереження даних у файлі
                    save_data()
                running = False
            if in_game and retry_rect.collidepoint(event.pos):
                score = 0
                player_rect.topleft = initial_player_pos
            elif in_game_2 and retry_rect.collidepoint(event.pos):
                in_game_2 = False
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            elif in_game_3 and retry_rect.collidepoint(event.pos):
                in_game_3 = False
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            elif in_game_4 and retry_rect.collidepoint(event.pos):
                in_game_4 = False
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            if in_game and select_rect.collidepoint(event.pos):
                in_game = False
                select_skin_menu = True
            elif in_game_2 and select_rect.collidepoint(event.pos):
                in_game_2 = False
                select_skin_menu = True
            elif in_game_3 and select_rect.collidepoint(event.pos):
                in_game_3 = False
                select_skin_menu = True
            elif in_game_4 and select_rect.collidepoint(event.pos):
                in_game_4 = False
                select_skin_menu = True
            if select_skin_menu and player_button_rect.collidepoint(event.pos):
                skin_in_2 = False
                skin_in_3 = False
                skin_in_1 = True
                select_skin_menu = False
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            elif select_skin_menu and player_2_button_rect.collidepoint(event.pos):
                if skin_2:
                    skin_in_2 = True
                    skin_in_3 = False
                    skin_in_1 = False
                    select_skin_menu = False
                    in_game = True
                    score = 0
                    player_rect.topleft = initial_player_pos
            elif select_skin_menu and player_3_button_rect.collidepoint(event.pos):
                if skin_3:
                    skin_in_2 = False
                    skin_in_3 = True
                    skin_in_1 = False
                    select_skin_menu = False
                    in_game = True
                    score = 0
                    player_rect.topleft = initial_player_pos
            if in_game and location_image_rect.collidepoint(event.pos):
                in_game = False
                location_menu = True
            elif in_game_2 and location_image_rect.collidepoint(event.pos):
                in_game_2 = False
                location_menu = True
            elif in_game_3 and location_image_rect.collidepoint(event.pos):
                in_game_3 = False
                location_menu = True
            elif in_game_4 and location_image_rect.collidepoint(event.pos):
                in_game_4 = False
                location_menu = True
            if location_menu and meteorits_on_off_rect.collidepoint(event.pos):
                if not meteorits:
                    meteorits = True
                else:
                    meteorits = False
                location_menu = False
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            if location_menu and classical_image_button_rect.collidepoint(event.pos):
                location_menu = False
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
        if event.type == wood_spawn_timer and in_game:
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 14 * n)))
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 112 * n)))
        if event.type == car_spawn_timer and in_game:
            car_rects.append(car_image.get_rect(topleft=(0, 84 * n)))
            car_rects_2.append(car_image.get_rect(topleft=(0, 56 * n)))
        if event.type == car_spawn_timer_2 and in_game:
            car_rects_3.append(car_image.get_rect(topleft=(0, 42 * n)))
        if event.type == wood_spawn_timer and in_game_2:
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 14 * n)))
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 112 * n)))
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 84 * n)))
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 42 * n)))
        if event.type == wood_spawn_timer_2 and in_game_2:
            wood_rects.append((wood_image.get_rect(topleft=(140 * n, 28 * n))))
            wood_rects.append((wood_image.get_rect(topleft=(140 * n, 70 * n))))
        if event.type == wood_spawn_timer and in_game_3:
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 14 * n)))
        if event.type == car_spawn_timer and in_game_3:
            car_rects_3.append(car_image.get_rect(topleft=(0, 28 * n)))
            car_rects_3.append(car_image.get_rect(topleft=(0, 112 * n)))
        if event.type == light_spawn_timer and in_game_3:
            if not object_created:
                if not timer_started:
                    timer_started = True
                    start_time = current_time

                elapsed_time_create = current_time - start_time

                if elapsed_time_create >= delay_create:
                    wall_rects_2_i = True
                    object_created = True
                    remove_start_time = current_time

            else:
                elapsed_time_remove = current_time - remove_start_time

                if elapsed_time_remove >= delay_remove:
                    wall_rects_2_i = False
                    object_created = False
                    timer_started = False
        if event.type == car_spawn_timer and in_game_4:
            car_rects_3.append(car_image.get_rect(topleft=(0, 0)))
            car_rects_3.append(car_image.get_rect(topleft=(0, 84 * n)))
            car_rects_3.append(car_image.get_rect(topleft=(0, 112 * n)))
        if event.type == wood_spawn_timer and in_game_4:
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 42 * n)))
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 98 * n)))
        if event.type == wood_spawn_timer_2 and in_game_4:
            wood_rects.append((wood_image.get_rect(topleft=(140 * n, 28 * n))))
        if event.type == light_spawn_timer and in_game_4:
            if not object_created:
                if not timer_started:
                    timer_started = True
                    start_time = current_time

                elapsed_time_create = current_time - start_time

                if elapsed_time_create >= delay_create:
                    wall_rects_2_i = True
                    object_created = True
                    remove_start_time = current_time

            else:
                elapsed_time_remove = current_time - remove_start_time

                if elapsed_time_remove >= delay_remove:
                    wall_rects_2_i = False
                    object_created = False
                    timer_started = False
        if meteorits:
            if event.type == light_spawn_2_timer and in_game_3 or in_game or in_game_2 or in_game_4:
                if not meteor and not meteor_2 and not meteor_3 and not meteor_4:
                    if not timer_started:
                        timer_started = True
                        start_time = current_time

                    elapsed_time_create = current_time - start_time

                    if elapsed_time_create >= delay_create:
                        random_choice = random.choice(numbers)
                        if random_choice == 1:
                            meteor = True
                        elif random_choice == 2:
                            meteor_2 = True
                        elif random_choice == 3:
                            meteor_3 = True
                        elif random_choice == 4:
                            meteor_4 = True
                        remove_start_time = current_time

                else:
                    elapsed_time_remove = current_time - remove_start_time

                    if elapsed_time_remove >= delay_remove:
                        meteor = False
                        meteor_2 = False
                        meteor_3 = False
                        meteor_4 = False
                        timer_started = False
        if event.type == light_spawn_3_timer and in_game_3 or in_game or in_game_2 or in_game_4:
            if not coion_1 and not coion_2 and not coion_3 and not coion_4:
                if not timer_started:
                    timer_started = True
                    start_time = current_time_2
                    remove_start_time = current_time_2

                elapsed_time_create = current_time_2 - start_time

                if elapsed_time_create >= delay_create:
                    random_choice = random.choice(numbers)
                    if random_choice == 1:
                        coion_1 = True
                    elif random_choice == 2:
                        coion_2 = True
                    elif random_choice == 3:
                        coion_3 = True
                    elif random_choice == 4:
                        coion_4 = True

            else:
                elapsed_time_remove = current_time_2 - remove_start_time

                if elapsed_time_remove >= delay_remove:
                    coion_1 = False
                    coion_2 = False
                    coion_3 = False
                    coion_4 = False
                    timer_started = False
        if event.type == wood_spawn_timer:
            anim_count += 1
            if anim_count == 2:
                anim_count = 0

    if in_game:
        river_positions = [(0, 14 * n), (0, 112 * n)]
        river_rects = [river_image_1.get_rect(topleft=(x, y)) for x, y in river_positions]
        wall_positions = [(44 * n, 30 * n), (72 * n, 72 * n), (30 * n, 100 * n), (114 * n, 100 * n)]
        wall_rects = [wall_image.get_rect(topleft=(x, y)) for x, y in wall_positions]
        if coion_1:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 1 * n))
        elif coion_2:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 43 * n))
        elif coion_3:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 71 * n))
        elif coion_4:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 99 * n))
        elif not coion_1 and not coion_2 and not coion_3 and not coion_4:
            coin_rect = coin_image.get_rect(topleft=(10000, 10000))
        if meteor:
            meteor_rect = meteor_image.get_rect(topleft=(28 * n, 0))
        elif meteor_2:
            meteor_rect = meteor_image.get_rect(topleft=(28 * n, 56 * n))
        elif meteor_3:
            meteor_rect = meteor_image.get_rect(topleft=(98 * n, 84 * n))
        elif meteor_4:
            meteor_rect = meteor_image.get_rect(topleft=(70 * n, 98 * n))
        elif not meteor and not meteor_2 and not meteor_3 and not meteor_4:
            meteor_rect = meteor_image.get_rect(topleft=(10000, 10000))
        for wall_rect in wall_rects:
            wall_rect.inflate_ip(2 * n, 2 * n)

        for car in car_rects:
            car.x -= CAR_SPEED

            if car.left > 140 * n:
                car_rects.remove(car)

            if player_rect.colliderect(car):
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        for car_2 in car_rects_2:
            car_2.x -= CAR_SPEED

            if car_2.left > 140 * n:
                car_rects_2.remove(car_2)

            if player_rect.colliderect(car_2):
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        for car_3 in car_rects_3:
            car_3.x -= CAR_SPEED

            if car_3.right < 0:
                car_rects_3.remove(car_3)

            if player_rect.colliderect(car_3):
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        for wood in wood_rects:
            wood.x += WOOD_SPEED

            if wood.right < 0:
                wood_rects.remove(wood)

            if player_rect.colliderect(wood):
                player_on_wood = True
                wood_player_is_on = wood

            if player_on_wood and wood_player_is_on:
                player_rect.x = wood_player_is_on.x
        for riv in river_rects:
            if player_rect.colliderect(riv) and not player_on_wood:
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        if player_rect.colliderect(meteor_rect):
            score = 0
            player_rect.topleft = initial_player_pos
            die.play()
        if player_rect.colliderect(coin_rect):
            coins += 1
            coion_1 = False
            coion_2 = False
            coion_3 = False
            coion_4 = False

        window.blit(background_image_game, (0, 0))
        for riv in river_rects:
            window.blit(river[anim_count], riv)
        window.blit(meteor_image, meteor_rect)
        for wall_rect in wall_rects:
            window.blit(wall_image, wall_rect)
        for wood in wood_rects:
            window.blit(wood_image, wood)
        for car in car_rects:
            window.blit(car_image, car)
        for car_2 in car_rects_2:
            window.blit(car_image, car_2)
        for car_3 in car_rects_3:
            window.blit(car_image, car_3)
        window.blit(coin_image, coin_rect)
        if skin_in_1:
            if player_up:
                window.blit(player_image_back, player_rect)
            elif player_down:
                window.blit(player_image, player_rect)
            elif player_right:
                window.blit(player_image_right, player_rect)
            elif player_left:
                window.blit(player_image_left, player_rect)
        elif skin_in_2:
            if player_up:
                window.blit(player_image_2_back, player_rect)
            elif player_down:
                window.blit(player_image_2, player_rect)
            elif player_right:
                window.blit(player_image_2_right, player_rect)
            elif player_left:
                window.blit(player_image_2_left, player_rect)
        elif skin_in_3:
            if player_up:
                window.blit(player_image_3_back, player_rect)
            elif player_down:
                window.blit(player_image_3, player_rect)
            elif player_right:
                window.blit(player_image_3_right, player_rect)
            elif player_left:
                window.blit(player_image_3_left, player_rect)

        score_text = font.render(f"Очки: {score}", True, WHITE)
        window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10 * n, 10 * n))
        max_score_text = font.render(f"Рекорд: {max_score}", True, BLACK)
        window.blit(max_score_text, (WINDOW_WIDTH - max_score_text.get_width() - 10 * n, 16 * n))
        coins_text = font.render(f"Монети: {coins}", True, YELLOW)
        window.blit(coins_text, (WINDOW_WIDTH - coins_text.get_width() - 10 * n, 22 * n))
        window.blit(retry_image, retry_rect)
        window.blit(select_image, select_rect)
        window.blit(location_image, location_image_rect)

    elif in_game_2:
        river_positions = [(0, 14 * n), (0, 112 * n), (0, 84 * n), (0, 42 * n), (0, 28 * n), (0, 70 * n)]
        river_rects = [river_image_1.get_rect(topleft=(x, y)) for x, y in river_positions]
        wall_positions = [(42 * n, 56 * n), (126 * n, 126 * n)]
        wall_rects = [wall_image_2.get_rect(topleft=(x, y)) for x, y in wall_positions]
        if coion_1:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 1 * n))
        elif coion_2:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 43 * n))
        elif coion_3:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 71 * n))
        elif coion_4:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 99 * n))
        elif not coion_1 and not coion_2 and not coion_3 and not coion_4:
            coin_rect = coin_image.get_rect(topleft=(10000, 10000))
        if meteor:
            meteor_rect = meteor_image.get_rect(topleft=(28 * n, 0))
        elif meteor_2:
            meteor_rect = meteor_image.get_rect(topleft=(28 * n, 56 * n))
        elif meteor_3:
            meteor_rect = meteor_image.get_rect(topleft=(98 * n, 84 * n))
        elif meteor_4:
            meteor_rect = meteor_image.get_rect(topleft=(70 * n, 98 * n))
        elif not meteor and not meteor_2 and not meteor_3 and not meteor_4:
            meteor_rect = meteor_image.get_rect(topleft=(10000, 10000))
        window.blit(background_image_game_2, (0, 0))
        for wood in wood_rects:
            wood.x += WOOD_SPEED

            if wood.right < 0:
                wood_rects.remove(wood)

            if player_rect.colliderect(wood):
                player_on_wood = True
                wood_player_is_on = wood

            if player_on_wood and wood_player_is_on:
                player_rect.x = wood_player_is_on.x
        for riv in river_rects:
            if player_rect.colliderect(riv) and not player_on_wood:
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        if player_rect.colliderect(meteor_rect):
            score = 0
            player_rect.topleft = initial_player_pos
            die.play()
        if player_rect.colliderect(coin_rect):
            coins += 1
            coion_1 = False
            coion_2 = False
            coion_3 = False
            coion_4 = False

        for riv in river_rects:
            window.blit(river[anim_count], riv)
        window.blit(meteor_image, meteor_rect)
        for wall_rect in wall_rects:
            window.blit(wall_image_2, wall_rect)
        for wood in wood_rects:
            window.blit(wood_image, wood)
        window.blit(coin_image, coin_rect)
        if skin_in_1:
            if player_up:
                window.blit(player_image_back, player_rect)
            elif player_down:
                window.blit(player_image, player_rect)
            elif player_right:
                window.blit(player_image_right, player_rect)
            elif player_left:
                window.blit(player_image_left, player_rect)
        elif skin_in_2:
            if player_up:
                window.blit(player_image_2_back, player_rect)
            elif player_down:
                window.blit(player_image_2, player_rect)
            elif player_right:
                window.blit(player_image_2_right, player_rect)
            elif player_left:
                window.blit(player_image_2_left, player_rect)
        elif skin_in_3:
            if player_up:
                window.blit(player_image_3_back, player_rect)
            elif player_down:
                window.blit(player_image_3, player_rect)
            elif player_right:
                window.blit(player_image_3_right, player_rect)
            elif player_left:
                window.blit(player_image_3_left, player_rect)

        score_text = font.render(f"Очки: {score}", True, WHITE)
        window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10 * n, 10 * n))
        max_score_text = font.render(f"Рекорд: {max_score}", True, BLACK)
        window.blit(max_score_text, (WINDOW_WIDTH - max_score_text.get_width() - 10 * n, 16 * n))
        coins_text = font.render(f"Монети: {coins}", True, YELLOW)
        window.blit(coins_text, (WINDOW_WIDTH - coins_text.get_width() - 10 * n, 22 * n))
        window.blit(retry_image, retry_rect)
        window.blit(select_image, select_rect)
        window.blit(location_image, location_image_rect)

    elif in_game_3:
        river_positions = [(0, 14 * n)]
        river_rects = [river_image_1.get_rect(topleft=(x, y)) for x, y in river_positions]
        train_positions = [(0, 56 * n), (0, 84 * n)]
        train_rects = [train_image.get_rect(topleft=(x, y)) for x, y in train_positions]
        wall_positions = [(28 * n, 70 * n), (84 * n, 98 * n)]
        wall_rects = [wall_image_3.get_rect(topleft=(x, y)) for x, y in wall_positions]
        if coion_1:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 1 * n))
        elif coion_2:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 43 * n))
        elif coion_3:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 71 * n))
        elif coion_4:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 99 * n))
        elif not coion_1 and not coion_2 and not coion_3 and not coion_4:
            coin_rect = coin_image.get_rect(topleft=(10000, 10000))
        if meteor:
            meteor_rect = meteor_image.get_rect(topleft=(28 * n, 0))
        elif meteor_2:
            meteor_rect = meteor_image.get_rect(topleft=(28 * n, 56 * n))
        elif meteor_3:
            meteor_rect = meteor_image.get_rect(topleft=(98 * n, 84 * n))
        elif meteor_4:
            meteor_rect = meteor_image.get_rect(topleft=(70 * n, 98 * n))
        elif not meteor and not meteor_2 and not meteor_3 and not meteor_4:
            meteor_rect = meteor_image.get_rect(topleft=(10000, 10000))
        window.blit(background_image_game_3, (0, 0))
        for wood in wood_rects:
            wood.x += WOOD_SPEED

            if wood.right < 0:
                wood_rects.remove(wood)

            if player_rect.colliderect(wood):
                player_on_wood = True
                wood_player_is_on = wood

            if player_on_wood and wood_player_is_on:
                player_rect.x = wood_player_is_on.x
        for riv in river_rects:
            if player_rect.colliderect(riv) and not player_on_wood:
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        for car_3 in car_rects_3:
            car_3.x -= CAR_SPEED

            if car_3.right < 0:
                car_rects_3.remove(car_3)

            if player_rect.colliderect(car_3):
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        if player_rect.colliderect(meteor_rect):
            score = 0
            player_rect.topleft = initial_player_pos
            die.play()
        if player_rect.colliderect(coin_rect):
            coins += 1
            coion_1 = False
            coion_2 = False
            coion_3 = False
            coion_4 = False

        for riv in river_rects:
            window.blit(river[anim_count], riv)
        window.blit(meteor_image, meteor_rect)
        for wood in wood_rects:
            window.blit(wood_image, wood)
        for car_3 in car_rects_3:
            window.blit(car_image, car_3)
        if not wall_rects_2_i:
            for wall_rect in wall_rects:
                window.blit(wall_image_3, wall_rect)
        elif wall_rects_2_i:
            for train in train_rects:
                window.blit(train_image, train)
                if player_rect.colliderect(train):
                    score = 0
                    player_rect.topleft = initial_player_pos
                    die.play()
            for wall_rect in wall_rects:
                window.blit(wall_image_4, wall_rect)
        window.blit(coin_image, coin_rect)
        if skin_in_1:
            if player_up:
                window.blit(player_image_back, player_rect)
            elif player_down:
                window.blit(player_image, player_rect)
            elif player_right:
                window.blit(player_image_right, player_rect)
            elif player_left:
                window.blit(player_image_left, player_rect)
        elif skin_in_2:
            if player_up:
                window.blit(player_image_2_back, player_rect)
            elif player_down:
                window.blit(player_image_2, player_rect)
            elif player_right:
                window.blit(player_image_2_right, player_rect)
            elif player_left:
                window.blit(player_image_2_left, player_rect)
        elif skin_in_3:
            if player_up:
                window.blit(player_image_3_back, player_rect)
            elif player_down:
                window.blit(player_image_3, player_rect)
            elif player_right:
                window.blit(player_image_3_right, player_rect)
            elif player_left:
                window.blit(player_image_3_left, player_rect)

        score_text = font.render(f"Очки: {score}", True, WHITE)
        window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10 * n, 10 * n))
        max_score_text = font.render(f"Рекорд: {max_score}", True, BLACK)
        window.blit(max_score_text, (WINDOW_WIDTH - max_score_text.get_width() - 10 * n, 16 * n))
        coins_text = font.render(f"Монети: {coins}", True, YELLOW)
        window.blit(coins_text, (WINDOW_WIDTH - coins_text.get_width() - 10 * n, 22 * n))
        window.blit(retry_image, retry_rect)
        window.blit(select_image, select_rect)
        window.blit(location_image, location_image_rect)

    elif in_game_4:
        river_positions = [(0, 42 * n), (0, 98 * n), (0, 28 * n)]
        river_rects = [river_image_1.get_rect(topleft=(x, y)) for x, y in river_positions]
        train_positions = [(0, 56 * n)]
        train_rects = [train_image.get_rect(topleft=(x, y)) for x, y in train_positions]
        wall_positions = [(28 * n, 70 * n)]
        wall_rects = [wall_image_3.get_rect(topleft=(x, y)) for x, y in wall_positions]
        wall_2_positions = [(56 * n, 14 * n)]
        wall_rects_3 = [wall_image_2.get_rect(topleft=(x, y)) for x, y in wall_2_positions]
        if coion_1:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 1 * n))
        elif coion_2:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 43 * n))
        elif coion_3:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 71 * n))
        elif coion_4:
            coin_rect = coin_image.get_rect(topleft=(57 * n, 99 * n))
        elif not coion_1 and not coion_2 and not coion_3 and not coion_4:
            coin_rect = coin_image.get_rect(topleft=(10000, 10000))
        if meteor:
            meteor_rect = meteor_image.get_rect(topleft=(28 * n, 0))
        elif meteor_2:
            meteor_rect = meteor_image.get_rect(topleft=(28 * n, 56 * n))
        elif meteor_3:
            meteor_rect = meteor_image.get_rect(topleft=(98 * n, 84 * n))
        elif meteor_4:
            meteor_rect = meteor_image.get_rect(topleft=(70 * n, 98 * n))
        elif not meteor and not meteor_2 and not meteor_3 and not meteor_4:
            meteor_rect = meteor_image.get_rect(topleft=(10000, 10000))
        window.blit(background_image_game_4, (0, 0))

        for wood in wood_rects:
            wood.x += WOOD_SPEED

            if wood.right < 0:
                wood_rects.remove(wood)

            if player_rect.colliderect(wood):
                player_on_wood = True
                wood_player_is_on = wood

            if player_on_wood and wood_player_is_on:
                player_rect.x = wood_player_is_on.x
        for car_3 in car_rects_3:
            car_3.x -= CAR_SPEED

            if car_3.right < 0:
                car_rects_3.remove(car_3)

            if player_rect.colliderect(car_3):
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        for riv in river_rects:
            if player_rect.colliderect(riv) and not player_on_wood:
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        if player_rect.colliderect(meteor_rect):
            score = 0
            player_rect.topleft = initial_player_pos
            die.play()
        if player_rect.colliderect(coin_rect):
            coins += 1
            coion_1 = False
            coion_2 = False
            coion_3 = False
            coion_4 = False

        for riv in river_rects:
            window.blit(river[anim_count], riv)
        window.blit(meteor_image, meteor_rect)
        for wood in wood_rects:
            window.blit(wood_image, wood)
        for car_3 in car_rects_3:
            window.blit(car_image, car_3)
        for wall_rect_3 in wall_rects_3:
            window.blit(wall_image_2, wall_rect_3)
        if not wall_rects_2_i:
            for wall_rect in wall_rects:
                window.blit(wall_image_3, wall_rect)
        elif wall_rects_2_i:
            for train in train_rects:
                window.blit(train_image, train)
                if player_rect.colliderect(train):
                    score = 0
                    player_rect.topleft = initial_player_pos
                    die.play()
            for wall_rect in wall_rects:
                window.blit(wall_image_4, wall_rect)
        window.blit(coin_image, coin_rect)
        if skin_in_1:
            if player_up:
                window.blit(player_image_back, player_rect)
            elif player_down:
                window.blit(player_image, player_rect)
            elif player_right:
                window.blit(player_image_right, player_rect)
            elif player_left:
                window.blit(player_image_left, player_rect)
        elif skin_in_2:
            if player_up:
                window.blit(player_image_2_back, player_rect)
            elif player_down:
                window.blit(player_image_2, player_rect)
            elif player_right:
                window.blit(player_image_2_right, player_rect)
            elif player_left:
                window.blit(player_image_2_left, player_rect)
        elif skin_in_3:
            if player_up:
                window.blit(player_image_3_back, player_rect)
            elif player_down:
                window.blit(player_image_3, player_rect)
            elif player_right:
                window.blit(player_image_3_right, player_rect)
            elif player_left:
                window.blit(player_image_3_left, player_rect)

        score_text = font.render(f"Очки: {score}", True, WHITE)
        window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10 * n, 10 * n))
        max_score_text = font.render(f"Рекорд: {max_score}", True, BLACK)
        window.blit(max_score_text, (WINDOW_WIDTH - max_score_text.get_width() - 10 * n, 16 * n))
        coins_text = font.render(f"Монети: {coins}", True, YELLOW)
        window.blit(coins_text, (WINDOW_WIDTH - coins_text.get_width() - 10 * n, 22 * n))
        window.blit(retry_image, retry_rect)
        window.blit(select_image, select_rect)
        window.blit(location_image, location_image_rect)

    elif select_skin_menu:
        window.blit(background_image_select_menu, (0, 0))
        window.blit(player_image_button, player_button_rect)
        if not skin_2:
            window.blit(lock_image, player_2_button_rect)
        else:
            window.blit(player_image_2_button, player_2_button_rect)
        if not skin_3:
            window.blit(lock_2_image, player_3_button_rect)
        else:
            window.blit(player_image_3_button, player_3_button_rect)

    elif location_menu:
        window.blit(background_image_location_menu, (0, 0))
        window.blit(classical_image_button, classical_image_button_rect)
        if not meteorits:
            window.blit(meteorits_off_image, meteorits_on_off_rect)
        else:
            window.blit(meteorits_on_image, meteorits_on_off_rect)

    elif menu:
        window.blit(background_image_menu, (0, 0))
        window.blit(button_image, button_rect)
        window.blit(exit_image, exit_rect)

    pygame.display.update()

pygame.quit()
