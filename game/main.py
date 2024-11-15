# Імпортуємо важливі дані
import random

import pygame

from sprites import *

# Головний цикл гри
running = True
while running:
    if not location_classic:
        in_game = False
        in_game_2 = False
    if COINS:
        random_choice = random.choice(numbers)
        if random_choice == 1:
            coin_on_1 = True
        if random_choice == 2:
            coin_on_2 = True
        if random_choice == 3:
            coin_on_3 = True
            boost = True
        if random_choice == 4:
            coin_on_4 = True
            boost = True
        COINS = False
    # Перевірка виходу за межі екрана
    if player_rect.x < 0:
        if not player_on_wood:
            score = 0
            player_rect.topleft = initial_player_pos
            die.play()
        else:
            score = 0
            player_on_wood = False
            player_rect.topleft = initial_player_pos
            river_die.play()
    current_time = pygame.time.get_ticks() / 1000
    current_time_2 = pygame.time.get_ticks() / 1100
    # Перевірка рекорду
    if score >= max_score:
        max_score = score
    # Умова для отримання нового скіна
    if max_score >= 50:
        skin_3 = True
    # Обробка подій
    for event in pygame.event.get():
        # Вихід з гри
        if event.type == pygame.QUIT:
            running = False

        # Обробка введення тексту
        if texting and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if name not in data["players"]:
                    data["players"][name] = {"MAX_SCORE": 0, "COINS": 0, "SKIN": False}
                else:
                    max_score = data["players"][name]["MAX_SCORE"]
                    coins = data["players"][name]["COINS"]
                    skin_2 = data["players"][name]["SKIN"]
                # Оновлення даних у файлі
                with open(data_file_name, "w") as file:
                    json.dump(data, file)
                location_classic = True
                in_game_1 = True
                score = 0
                player_rect.topleft = initial_player_pos
                texting = False
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            else:
                if len(name) < 10:
                    name += event.unicode

        # Обробка натискання клавіш
        if event.type == pygame.KEYDOWN:
            # Вихід в головне меню
            if event.key == pygame.K_ESCAPE:
                location_classic = False
                menu = True

            # Відстежування руху гравця
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
                    if not any(temp_rect.colliderect(wall) for wall in wall_rects_1):
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
                    if not any(temp_rect.colliderect(wall) for wall in wall_rects_1):
                        player_rect.move_ip(TILE_SIZE, 0)
                else:
                    # Звичайний рух гравця праворуч
                    temp_rect = player_rect.move(TILE_SIZE, 0)
                    # Перевіряємо зіткнення з якоюсь зі стін
                    if not any(temp_rect.colliderect(wall) for wall in wall_rects_1):
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
                if not any(temp_rect.colliderect(wall) for wall in wall_rects_1):
                    move_player_to_tile(dy=-TILE_SIZE)
                    score += 1
                if player_rect.y < 0:
                    COINS = True
                    coin_on_1 = False
                    coin_on_2 = False
                    coin_on_3 = False
                    coin_on_4 = False
                    random_choice = random.choice(numbers)
                    initial_player_pos = (57 * n, 127 * n)
                    player_rect.topleft = initial_player_pos
                    if random_choice == 1:
                        location_classic = True
                        in_game_1 = True
                        in_game_2 = False
                        gacha = False
                    elif random_choice == 2:
                        location_classic = True
                        in_game_2 = True
                        in_game_1 = False
                        gacha = False
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
                if not any(temp_rect.colliderect(wall) for wall in wall_rects_1):
                    move_player_to_tile(dy=TILE_SIZE)
                    score -= 1
                if player_rect.y >= WINDOW_HEIGHT:
                    score = 0
                    location_classic = False
                    gacha = True
                    reset_game()
                    player_rect.topleft = (57 * n, 1 * n)
                if player_on_wood:
                    player_on_wood = False
                    wood_player_is_on = None

        # Обробка натискання клавіш миші
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Обробка натискання по кнопках в головному меню
            if (main_menu and not location_classic and not select_skin_menu and
                    not select_location_menu and play_rect.collidepoint(event.pos)):
                if main_menu and play_rect.collidepoint(event.pos):
                    texting = True
            if (main_menu and not location_classic and not select_skin_menu and
                    not select_location_menu and exit_rect.collidepoint(event.pos)):
                if name in data["players"]:
                    data["players"][name]["MAX_SCORE"] = max_score
                    data["players"][name]["COINS"] = coins
                    data["players"][name]["SKIN"] = skin_2
                    save_data()
                else:
                    # Додавання нового запису для поточного гравця у списку data["players"]
                    data["players"][name] = {"NAME": name, "MAX_SCORE": score, "COINS": coins, "SKIN": skin_2}
                    # Збереження даних у файлі
                    save_data()
                running = False
            if (main_menu and not location_classic and not select_skin_menu and
                    not select_location_menu and not help_menu and help_rect.collidepoint(event.pos)):
                help_menu = True
                main_menu = False
            if (help_menu and not location_classic and not select_skin_menu and
                    not select_location_menu and not main_menu and back_rect.collidepoint(event.pos)):
                main_menu = True
                help_menu = False
            # Обробка натискання по кнопках у грі
            if location_classic and retry_rect.collidepoint(event.pos):
                score = 0
                player_rect.topleft = initial_player_pos
            if location_classic and select_rect.collidepoint(event.pos):
                location_classic = False
                select_skin_menu = True
            if location_classic and location_image_rect.collidepoint(event.pos):
                location_classic = False
                select_location_menu = True
            # Обробка натискання по кнопках скінів в меню вибору скінів
            if select_skin_menu and player_button_rect.collidepoint(event.pos):
                skin_in_2 = False
                skin_in_3 = False
                skin_in_1 = True
                select_skin_menu = False
                location_classic = True
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            elif select_skin_menu and player_2_button_rect.collidepoint(event.pos):
                if skin_2:
                    skin_in_2 = True
                    skin_in_3 = False
                    skin_in_1 = False
                    select_skin_menu = False
                    location_classic = True
                    in_game = True
                    score = 0
                    player_rect.topleft = initial_player_pos
                if not skin_2:
                    if coins >= 50:
                        coins -= 50
                        skin_2 = True
            elif select_skin_menu and player_3_button_rect.collidepoint(event.pos):
                if skin_3:
                    skin_in_2 = False
                    skin_in_3 = True
                    skin_in_1 = False
                    select_skin_menu = False
                    location_classic = True
                    in_game = True
                    score = 0
                    player_rect.topleft = initial_player_pos
            # Обробка натискання по кнопках зміни локації та включення режиму з метеоритами в меню вибору режимів
            if select_location_menu and meteorits_on_off_rect.collidepoint(event.pos):
                if not METEORITS:
                    METEORITS = True
                else:
                    METEORITS = False
                select_location_menu = False
                location_classic = True
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            if select_location_menu and classical_image_button_rect.collidepoint(event.pos):
                location_classic = True
                select_location_menu = False
                in_game = True
                score = 0
                player_rect.topleft = initial_player_pos
            if select_location_menu and easter_image_button_rect.collidepoint(event.pos):
                location_easter = True
                select_location_menu = False
                score = 0
                player_rect.topleft = initial_player_pos

        # Обробка спавну спрайтів по таймеру
        if event.type == sprite_spawn_timer and in_game_1:
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 14 * n)))
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 112 * n)))
            car_rects_1.append(car_image_1.get_rect(topleft=(0, 84 * n)))
            car_rects_1.append(car_image_1.get_rect(topleft=(0, 56 * n)))

        if event.type == sprite_spawn_timer and in_game_2:
            wood_rects.append(wood_image.get_rect(topleft=(140 * n, 14 * n)))
            for wood in wood_rects:
                if wood.right < 112 * n:
                    car_rects_1.append(car_image_1.get_rect(topleft=(0, 28 * n)))
                    car_rects_1.append(car_image_1.get_rect(topleft=(0, 112 * n)))

        if event.type == sprite_spawn_timer and in_game_2:
            if not object_created:
                if not timer_started:
                    timer_started = True
                    start_time = current_time

                elapsed_time_create = current_time - start_time

                if elapsed_time_create >= delay_create:
                    wall_rects_2_anim = True
                    object_created = True
                    remove_start_time = current_time

            else:
                elapsed_time_remove = current_time - remove_start_time

                if elapsed_time_remove >= delay_remove:
                    wall_rects_2_anim = False
                    object_created = False
                    timer_started = False
        # Обробка спавну метеоритів на окремих локаціях
        if METEORITS:
            if event.type == sprite_spawn_timer and location_classic or location_easter:
                if not meteor_1 and not meteor_2 and not meteor_3 and not meteor_4:
                    if not timer_started:
                        timer_started = True
                        start_time = current_time

                    elapsed_time_create = current_time - start_time

                    if elapsed_time_create >= delay_create:
                        random_choice = random.choice(numbers)
                        if random_choice == 1:
                            meteor_1 = True
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
                        meteor_1 = False
                        meteor_2 = False
                        meteor_3 = False
                        meteor_4 = False
                        timer_started = False
        elif not METEORITS:
            meteor_1 = False
            meteor_2 = False
            meteor_3 = False
            meteor_4 = False

        # Обробка анімації по таймеру
        if event.type == sprite_spawn_timer:
            anim_count += 1
            if anim_count == 2:
                anim_count = 0

    # Перевірка режиму гри
    if location_classic:
        if in_game_1:
            # Встановлення позицій
            river_positions = [(0, 14 * n), (0, 112 * n)]
            river_rects = [river_image_1.get_rect(topleft=(x, y)) for x, y in river_positions]
            wall_positions = [(44 * n, 30 * n), (72 * n, 72 * n), (30 * n, 100 * n), (114 * n, 100 * n)]
            wall_rects_1 = [wall_image_1.get_rect(topleft=(x, y)) for x, y in wall_positions]
            if coin_on_1:
                coin_rect = coin_image.get_rect(topleft=(58 * n, 2 * n))
            elif coin_on_2:
                coin_rect = coin_image.get_rect(topleft=(58 * n, 44 * n))
            elif coin_on_3:
                coin_rect = coin_image.get_rect(topleft=(58 * n, 72 * n))
            elif coin_on_4:
                coin_rect = coin_image.get_rect(topleft=(58 * n, 100 * n))
            elif not coin_on_1 and not coin_on_2 and not coin_on_3 and not coin_on_4:
                coin_rect = coin_image.get_rect(topleft=(-10000, -10000))
            if meteor_1:
                meteor_rect = meteor_image.get_rect(topleft=(28 * n, 0))
            elif meteor_2:
                meteor_rect = meteor_image.get_rect(topleft=(28 * n, 56 * n))
            elif meteor_3:
                meteor_rect = meteor_image.get_rect(topleft=(98 * n, 84 * n))
            elif meteor_4:
                meteor_rect = meteor_image.get_rect(topleft=(70 * n, 98 * n))
            elif not meteor_1 and not meteor_2 and not meteor_3 and not meteor_4:
                meteor_rect = meteor_image.get_rect(topleft=(10000, 10000))
            for wall_rect in wall_rects_1:
                wall_rect.inflate_ip(2 * n, 2 * n)

            # Обробка спавну та торкання колізій
            for car in car_rects_1:
                car.x -= CAR_SPEED

                if car.left > 140 * n:
                    car_rects_1.remove(car)
                    map_1_spawn_car += 1
                    if map_1_spawn_car > 4:
                        map_1_spawn_car = 0
                    if map_1_spawn_car == 4:
                        car_rects_2.append(car_image_2.get_rect(topleft=(0, 42 * n)))

                if player_rect.colliderect(car):
                    car_die.play()
                    reset_game()
            for car_2 in car_rects_2:
                car_2.x -= CAR_2_SPEED / 2

                if car_2.left > 140 * n:
                    car_rects_2.remove(car_2)

                if player_rect.colliderect(car_2):
                    car_die.play()
                    reset_game()
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
                    river_die.play()
                    reset_game()
            if player_rect.colliderect(meteor_rect):
                die.play()
                reset_game()
            if player_rect.colliderect(coin_rect) and not boost:
                coins += 1
                coin_sound.play()
                coin_on_1 = False
                coin_on_2 = False
                coin_on_3 = False
                coin_on_4 = False
            if player_rect.colliderect(coin_rect) and boost:
                coins += 1
                boost_sound.play()
                for i in range(2):
                    move_player_to_tile(dy=-TILE_SIZE)
                coin_on_1 = False
                coin_on_2 = False
                coin_on_3 = False
                coin_on_4 = False
                boost = False

            # Відмальовування на екрані
            window.blit(background_image_game_1, (0, 0))
            for riv in river_rects:
                window.blit(river[anim_count], riv)
            window.blit(meteor_image, meteor_rect)
            for wall_rect in wall_rects_1:
                window.blit(wall_image_1, wall_rect)
            for wood in wood_rects:
                window.blit(wood_image, wood)
            for car in car_rects_1:
                window.blit(car_image_1, car)
            for car_2 in car_rects_2:
                window.blit(car_image_2, car_2)
            if not boost:
                window.blit(coin_image, coin_rect)
            if boost:
                window.blit(coin_boost_image, coin_rect)
            if skin_in_1:
                if player_up:
                    window.blit(player_image_1_up, player_rect)
                elif player_down:
                    window.blit(player_image_1_down, player_rect)
                elif player_right:
                    window.blit(player_image_1_right, player_rect)
                elif player_left:
                    window.blit(player_image_1_left, player_rect)
            elif skin_in_2:
                if player_up:
                    window.blit(player_image_2_up, player_rect)
                elif player_down:
                    window.blit(player_image_2_down, player_rect)
                elif player_right:
                    window.blit(player_image_2_right, player_rect)
                elif player_left:
                    window.blit(player_image_2_left, player_rect)
            elif skin_in_3:
                if player_up:
                    window.blit(player_image_3_up, player_rect)
                elif player_down:
                    window.blit(player_image_3_down, player_rect)
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
            window.blit(select_skin_image, select_rect)
            window.blit(select_location_image, location_image_rect)

        elif in_game_2:
            # Встановлення позицій
            river_positions = [(0, 14 * n)]
            river_rects = [river_image_1.get_rect(topleft=(x, y)) for x, y in river_positions]
            train_positions = [(0, 56 * n), (0, 84 * n)]
            train_rects = [train_image_1.get_rect(topleft=(x, y)) for x, y in train_positions]
            wall_positions = [(28 * n, 70 * n), (84 * n, 98 * n)]
            wall_rects_1 = [wall_image_3.get_rect(topleft=(x, y)) for x, y in wall_positions]
            if coin_on_1:
                coin_rect = coin_image.get_rect(topleft=(58 * n, 2 * n))
            elif coin_on_2:
                coin_rect = coin_image.get_rect(topleft=(58 * n, 44 * n))
            elif coin_on_3:
                coin_rect = coin_image.get_rect(topleft=(58 * n, 72 * n))
            elif coin_on_4:
                coin_rect = coin_image.get_rect(topleft=(58 * n, 100 * n))
            elif not coin_on_1 and not coin_on_2 and not coin_on_3 and not coin_on_4:
                coin_rect = coin_image.get_rect(topleft=(-10000, -10000))
            if meteor_1:
                meteor_rect = meteor_image.get_rect(topleft=(28 * n, 0))
            elif meteor_2:
                meteor_rect = meteor_image.get_rect(topleft=(28 * n, 56 * n))
            elif meteor_3:
                meteor_rect = meteor_image.get_rect(topleft=(98 * n, 84 * n))
            elif meteor_4:
                meteor_rect = meteor_image.get_rect(topleft=(70 * n, 98 * n))
            elif not meteor_1 and not meteor_2 and not meteor_3 and not meteor_4:
                meteor_rect = meteor_image.get_rect(topleft=(10000, 10000))

            # Обробка спавну та торкання колізій
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
                    river_die.play()
                    reset_game()
            for car in car_rects_1:
                car.x -= CAR_SPEED

                if car.right < 0:
                    car_rects_1.remove(car)

                if player_rect.colliderect(car):
                    car_die.play()
                    reset_game()
            if player_rect.colliderect(meteor_rect):
                die.play()
                reset_game()
            if player_rect.colliderect(coin_rect) and not boost:
                coins += 1
                coin_sound.play()
                coin_on_1 = False
                coin_on_2 = False
                coin_on_3 = False
                coin_on_4 = False
            if player_rect.colliderect(coin_rect) and boost:
                coins += 1
                boost_sound.play()
                for i in range(2):
                    move_player_to_tile(dy=-TILE_SIZE)
                coin_on_1 = False
                coin_on_2 = False
                coin_on_3 = False
                coin_on_4 = False
                boost = False

            # Відмальовування на екрані
            window.blit(background_image_game_3, (0, 0))
            for riv in river_rects:
                window.blit(river[anim_count], riv)
            window.blit(meteor_image, meteor_rect)
            for wood in wood_rects:
                window.blit(wood_image, wood)
            for car in car_rects_1:
                window.blit(car_image_1, car)
            if not wall_rects_2_anim:
                for wall_rect in wall_rects_1:
                    window.blit(wall_image_3, wall_rect)
            elif wall_rects_2_anim:
                for tra in train_rects:
                    window.blit(train[anim_count], tra)
                    if player_rect.colliderect(tra):
                        score = 0
                        player_rect.topleft = initial_player_pos
                        die.play()
                for wall_rect in wall_rects_1:
                    window.blit(wall_image_4, wall_rect)
            if not boost:
                window.blit(coin_image, coin_rect)
            if boost:
                window.blit(coin_boost_image, coin_rect)
            if skin_in_1:
                if player_up:
                    window.blit(player_image_1_up, player_rect)
                elif player_down:
                    window.blit(player_image_1_down, player_rect)
                elif player_right:
                    window.blit(player_image_1_right, player_rect)
                elif player_left:
                    window.blit(player_image_1_left, player_rect)
            elif skin_in_2:
                if player_up:
                    window.blit(player_image_2_up, player_rect)
                elif player_down:
                    window.blit(player_image_2_down, player_rect)
                elif player_right:
                    window.blit(player_image_2_right, player_rect)
                elif player_left:
                    window.blit(player_image_2_left, player_rect)
            elif skin_in_3:
                if player_up:
                    window.blit(player_image_3_up, player_rect)
                elif player_down:
                    window.blit(player_image_3_down, player_rect)
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
            window.blit(select_skin_image, select_rect)
            window.blit(select_location_image, location_image_rect)

    elif gacha:
        # Очищення колізій стін
        wall_rects_1 = []

        # Відмальовування на екрані
        window.blit(background_image_gacha, (0, 0))
        if skin_in_1:
            if player_up:
                window.blit(player_image_1_up, player_rect)
            elif player_down:
                window.blit(player_image_1_down, player_rect)
            elif player_right:
                window.blit(player_image_1_right, player_rect)
            elif player_left:
                window.blit(player_image_1_left, player_rect)
        elif skin_in_2:
            if player_up:
                window.blit(player_image_2_up, player_rect)
            elif player_down:
                window.blit(player_image_2_down, player_rect)
            elif player_right:
                window.blit(player_image_2_right, player_rect)
            elif player_left:
                window.blit(player_image_2_left, player_rect)
        elif skin_in_3:
            if player_up:
                window.blit(player_image_3_up, player_rect)
            elif player_down:
                window.blit(player_image_3_down, player_rect)
            elif player_right:
                window.blit(player_image_3_right, player_rect)
            elif player_left:
                window.blit(player_image_3_left, player_rect)

    elif select_skin_menu:
        # Відмальовування на екрані
        window.blit(background_image_select_skin_menu, (0, 0))
        window.blit(player_image_1_button, player_button_rect)
        if not skin_2:
            window.blit(buy_image, player_2_button_rect)
        else:
            window.blit(player_image_2_button, player_2_button_rect)
        if not skin_3:
            window.blit(lock_image, player_3_button_rect)
        else:
            window.blit(player_image_3_button, player_3_button_rect)

    elif select_location_menu:
        # Відмальовування на екрані
        window.blit(background_image_select_location_menu, (0, 0))
        window.blit(classical_image_button, classical_image_button_rect)
        window.blit(easter_image_button, easter_image_button_rect)
        if not METEORITS:
            window.blit(meteorits_off_image, meteorits_on_off_rect)
        else:
            window.blit(meteorits_on_image, meteorits_on_off_rect)

    elif main_menu:
        # Відмальовування на екрані
        window.blit(background_image_menu, (0, 0))
        window.blit(play_image, play_rect)
        window.blit(exit_image, exit_rect)
        window.blit(help_image, help_rect)
        if texting:
            pls_text = font.render(f"Введіть ім'я: {name}", True, WHITE)
            window.blit(pls_text, (WINDOW_WIDTH - pls_text.get_width() - 50 * n, 110 * n))

    elif help_menu:
        # Відмальовування на екрані
        window.blit(background_image_help, (0, 0))
        window.blit(back_image, back_rect)

    # Оновлення дисплея
    pygame.display.update()

# Вихід
pygame.quit()
