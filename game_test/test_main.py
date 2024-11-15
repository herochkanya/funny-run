# Імпортуємо важливі функції
from test_sprites import *

while run:

    clock.tick(FPS)

    player.update_animation()

    for event in pygame.event.get():
        # вимикаємо гру
        if event.type == pygame.QUIT:
            run = False
        # натиснення клавіш клавіатури
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_w:
                if player.rect.y > 0:
                    player.move_to_tile(dy=-TILE_SIZE)
            if event.key == pygame.K_s:
                player.move_to_tile(dy=TILE_SIZE)
            if event.key == pygame.K_a:
                player.move_to_tile(dx=-TILE_SIZE)
            if event.key == pygame.K_d:
                player.move_to_tile(dx=TILE_SIZE)
        # таймер для створення спрайта
        if event.type == sprite_spawn_timer and game:
            print('true')
            print(background_y_1)
            car.position_list = [(car_position_1_x, car_position_1_y), (car_position_2_x, car_position_2_y)]
            car.update_position()

    if game:
        background_y_1 += 1
        background_y_2 += 1
        if background_y_1 > 140 * scale:
            if map_1 == "map 1":
                game_1 = False
            if map_1 == "map 2":
                game_2 = False
            if map_1 == "map 3":
                game_3 = False
            if map_1 == "map 4":
                game_4 = False
            map_1 = random.choice(background_list)
            background_y_1 = -background_height
        if background_y_2 > 140 * scale:
            if map_1 == "map 1":
                game_1 = False
            if map_1 == "map 2":
                game_2 = False
            if map_1 == "map 3":
                game_3 = False
            if map_1 == "map 4":
                game_4 = False
            map_2 = random.choice(background_list)
            background_y_2 = -background_height
        if background_y_1 > 0 or background_y_2 > 0 and map_1 == "map 1":
            game_1 = True
        if background_y_1 > 0 or background_y_2 > 0 and map_1 == "map 2":
            game_2 = True
        if background_y_1 > 0 or background_y_2 > 0 and map_1 == "map 3":
            game_3 = True
        if background_y_1 > 0 or background_y_2 > 0 and map_1 == "map 4":
            game_4 = True
        window.blit(background_1, (0, background_y_1))
        window.blit(background_2, (0, background_y_2))
        draw_bg()

        player.draw()
        player.rect.y += 1

        car_position_1_y += 1
        car_position_2_y +=1
        if car_position_1_y > 140 * scale:
            car.position_list.clear()
            car.active_cars.clear()
        if car_position_2_y > 140 * scale:
            car.position_list.clear()
            car.active_cars.clear()
        car.draw()
        for car_rect in car.active_cars:
            car_rect.y += 1
            car_rect.x += 3
            if car_rect.right < 0:
                car.active_cars.remove(car_rect)
            if car_rect.bottom >= WINDOW_HEIGHT:
                lowest_position = 0
                car_rect.top = lowest_position

    player.update()

    car.update()

    pygame.display.update()


pygame.quit()
