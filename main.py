import pygame
import random

pygame.init()

WINDOW_WIDTH = 140 * 3
WINDOW_HEIGHT = 140 * 3

TILE_SIZE = 42
OFFSET = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("funny run")

background_image_menu = pygame.image.load("menu.png")
background_image_game = pygame.image.load("map 1.png")
button_image = pygame.image.load("play.png")
player_image = pygame.image.load("slime 1.png")
wall_image = pygame.image.load("wall.png")
wood_image = pygame.image.load("wood.png")
river_image = pygame.image.load("river.gif")
car_image = pygame.image.load("car.png")
exit_image = pygame.image.load("exit.png")
background_image_game_2 = pygame.image.load("map 2.png")
wall_image_2 = pygame.image.load("wall 2.png")
background_image_game_3 = pygame.image.load("map 3.png")
wall_image_3 = pygame.image.load("wall 3.png")
wall_image_4 = pygame.image.load("wall 4.png")
train_image = pygame.image.load("train.png")

city = pygame.mixer.Sound("city.mp3")
die = pygame.mixer.Sound("die.mp3")

background_image_menu = pygame.transform.scale(background_image_menu, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_game = pygame.transform.scale(background_image_game, (WINDOW_WIDTH, WINDOW_HEIGHT))
button_image = pygame.transform.scale(button_image, (56 * 3, 14 * 3))
player_image = pygame.transform.scale(player_image, (12 * 3, 12 * 3))
wall_image = pygame.transform.scale(wall_image, (12 * 3, 12 * 3))
wood_image = pygame.transform.scale(wood_image, (28 * 3, 14 * 3))
river_image = pygame.transform.scale(river_image, (140 * 3, 14 * 3))
car_image = pygame.transform.scale(car_image, (14 * 3, 12 * 3))
exit_image = pygame.transform.scale(exit_image, (56 * 3, 14 * 3))
wall_image_2 = pygame.transform.scale(wall_image_2, (12 * 3, 12 * 3))
background_image_game_2 = pygame.transform.scale(background_image_game_2, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_image_game_3 = pygame.transform.scale(background_image_game_3, (WINDOW_WIDTH, WINDOW_HEIGHT))
wall_image_3 = pygame.transform.scale(wall_image_3, (12 * 3, 12 * 3))
wall_image_4 = pygame.transform.scale(wall_image_4, (12 * 3, 12 * 3))
train_image = pygame.transform.scale(train_image, (140 * 3, 12 * 3))

button_rect = button_image.get_rect(center=(WINDOW_WIDTH // 1.9, WINDOW_HEIGHT // 1.9))
player_rect = player_image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - player_image.get_height() // 2))
exit_rect = button_image.get_rect(center=(WINDOW_WIDTH // 1.9, WINDOW_HEIGHT // 1.5))

wood_rects = []

WOOD_SPEED = -WINDOW_WIDTH / 28 / 28

car_rects = []
car_rects_2 = []
car_rects_3 = []

CAR_SPEED = -WINDOW_WIDTH / 30 / 28

wall_rects_2 = []

in_game_3 = False
in_game_2 = False
in_game = False
menu = True
wall_rects_2_i = False

timer_started = False
start_time = 0
delay_create = 1
delay_remove = 5
object_created = False

numbers = [1, 2, 3]

score = 0
max_score = 0

initial_player_pos = (171, 381)

font = pygame.font.Font(None, 24)

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

city.play(-1)

player_on_wood = False
wood_player_is_on = None


def move_player_to_tile(dx=0, dy=0):
    global player_rect

    new_x = ((player_rect.x + dx + OFFSET) // TILE_SIZE) * TILE_SIZE
    new_y = ((player_rect.y + dy + OFFSET) // TILE_SIZE) * TILE_SIZE

    player_rect.x = new_x + OFFSET
    player_rect.y = new_y + OFFSET


def reset_game():
    global score, player_rect, car_rects, wood_rects, car_rects_2, car_rects_3, wall_rects, river_rects, wall_rects_2, \
        train_rects
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
    if score >= max_score:
        max_score = score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                in_game = False
                in_game_2 = False
                in_game_3 = False
                menu = True

            if event.key == pygame.K_LEFT:
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
                temp_rect = player_rect.move(0, -TILE_SIZE)
                if not any(temp_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                    move_player_to_tile(dy=-TILE_SIZE)
                    score += 1
                if player_rect.y < 0:
                    random_choice = random.choice(numbers)
                    initial_player_pos = (171, 381)
                    player_rect.topleft = initial_player_pos
                    if random_choice == 1:
                        in_game = True
                        in_game_2 = False
                        in_game_3 = False
                    elif random_choice == 2:
                        in_game_2 = True
                        in_game = False
                        in_game_3 = False
                    elif random_choice == 3:
                        in_game_3 = True
                        in_game = False
                        in_game_2 = False
                    reset_game()
                if player_on_wood:
                    player_on_wood = False
                    wood_player_is_on = None

            elif event.key == pygame.K_DOWN:
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

        if event.type == pygame.MOUSEBUTTONDOWN and not in_game and not in_game_2:
            if menu and button_rect.collidepoint(event.pos):
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            if menu and exit_rect.collidepoint(event.pos):
                running = False
        if event.type == wood_spawn_timer and in_game:
            wood_rects.append(wood_image.get_rect(topleft=(420, 42)))
            wood_rects.append(wood_image.get_rect(topleft=(420, 336)))
        if event.type == car_spawn_timer and in_game:
            car_rects.append(car_image.get_rect(topleft=(0, 252)))
            car_rects_2.append(car_image.get_rect(topleft=(0, 168)))
        if event.type == car_spawn_timer_2 and in_game:
            car_rects_3.append(car_image.get_rect(topleft=(0, 126)))
        if event.type == wood_spawn_timer and in_game_2:
            wood_rects.append(wood_image.get_rect(topleft=(420, 42)))
            wood_rects.append(wood_image.get_rect(topleft=(420, 336)))
            wood_rects.append(wood_image.get_rect(topleft=(420, 252)))
            wood_rects.append(wood_image.get_rect(topleft=(420, 126)))
        if event.type == wood_spawn_timer_2 and in_game_2:
            wood_rects.append((wood_image.get_rect(topleft=(420, 84))))
            wood_rects.append((wood_image.get_rect(topleft=(420, 210))))
        if event.type == wood_spawn_timer and in_game_3:
            wood_rects.append(wood_image.get_rect(topleft=(420, 42)))
        if event.type == car_spawn_timer and in_game_3:
            car_rects_3.append(car_image.get_rect(topleft=(0, 84)))
            car_rects_3.append(car_image.get_rect(topleft=(0, 338)))
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

    if in_game:
        river_positions = [(0, 42), (0, 336)]
        river_rects = [river_image.get_rect(topleft=(x, y)) for x, y in river_positions]
        wall_positions = [(132, 90), (216, 216), (90, 300), (342, 300)]
        wall_rects = [wall_image.get_rect(topleft=(x, y)) for x, y in wall_positions]
        for wall_rect in wall_rects:
            wall_rect.inflate_ip(6, 6)

        for car in car_rects:
            car.x -= CAR_SPEED

            if car.left > 420:
                car_rects.remove(car)

            if player_rect.colliderect(car):
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()
        for car_2 in car_rects_2:
            car_2.x -= CAR_SPEED

            if car_2.left > 420:
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
        for river in river_rects:
            if player_rect.colliderect(river) and not player_on_wood:
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()

        window.blit(background_image_game, (0, 0))
        for wall_rect in wall_rects:
            window.blit(wall_image, wall_rect)
        for river in river_rects:
            window.blit(river_image, river)
        for wood in wood_rects:
            window.blit(wood_image, wood)
        for car in car_rects:
            window.blit(car_image, car)
        for car_2 in car_rects_2:
            window.blit(car_image, car_2)
        for car_3 in car_rects_3:
            window.blit(car_image, car_3)
        window.blit(player_image, player_rect)

        score_text = font.render(f"Очки: {score}", True, WHITE)
        window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 30, 30))
        max_score_text = font.render(f"Рекорд: {max_score}", True, BLACK)
        window.blit(max_score_text, (WINDOW_WIDTH - max_score_text.get_width() - 30, 50))

    elif in_game_2:
        river_positions = [(0, 42), (0, 336), (0, 252), (0, 126), (0, 84), (0, 210)]
        river_rects = [river_image.get_rect(topleft=(x, y)) for x, y in river_positions]
        wall_positions = [(126, 168), (378, 378)]
        wall_rects = [wall_image_2.get_rect(topleft=(x, y)) for x, y in wall_positions]
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
        for river in river_rects:
            if player_rect.colliderect(river) and not player_on_wood:
                score = 0
                player_rect.topleft = initial_player_pos
                die.play()

        for wall_rect in wall_rects:
            window.blit(wall_image_2, wall_rect)
        for river in river_rects:
            window.blit(river_image, river)
        for wood in wood_rects:
            window.blit(wood_image, wood)
        window.blit(player_image, player_rect)

        score_text = font.render(f"Очки: {score}", True, WHITE)
        window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 30, 30))
        max_score_text = font.render(f"Рекорд: {max_score}", True, BLACK)
        window.blit(max_score_text, (WINDOW_WIDTH - max_score_text.get_width() - 30, 50))

    elif in_game_3:
        river_positions = [(0, 42)]
        river_rects = [river_image.get_rect(topleft=(x, y)) for x, y in river_positions]
        train_positions = [(0, 168), (0, 252)]
        train_rects = [train_image.get_rect(topleft=(x, y)) for x, y in train_positions]
        wall_positions = [(84, 210), (252, 294)]
        wall_rects = [wall_image_3.get_rect(topleft=(x, y)) for x, y in wall_positions]
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
        for river in river_rects:
            if player_rect.colliderect(river) and not player_on_wood:
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

        for river in river_rects:
            window.blit(river_image, river)
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
        window.blit(player_image, player_rect)

        score_text = font.render(f"Очки: {score}", True, WHITE)
        window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 30, 30))
        max_score_text = font.render(f"Рекорд: {max_score}", True, BLACK)
        window.blit(max_score_text, (WINDOW_WIDTH - max_score_text.get_width() - 30, 50))

    elif menu:
        window.blit(background_image_menu, (0, 0))
        window.blit(button_image, button_rect)
        window.blit(exit_image, exit_rect)

    pygame.display.update()

pygame.quit()
