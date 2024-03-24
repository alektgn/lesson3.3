import pygame
import sys
import random

pygame.init()

# Настройки экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Игра: Попади в движущуюся цель")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Цель
target_radius = 20
target_x = random.randint(target_radius, screen_width - target_radius)
target_y = random.randint(target_radius, screen_height - target_radius)

# Скорость и направление движения цели
target_speed_x = 2
target_speed_y = 2

# Счет
score = 0
font = pygame.font.Font(None, 36)

# Запуск игрового цикла
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Проверка попадания
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
            if distance < target_radius:
                score += 1
                # Переместим цель
                target_x = random.randint(target_radius, screen_width - target_radius)
                target_y = random.randint(target_radius, screen_height - target_radius)

    # Обновляем позицию цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Отскок от границ экрана
    if target_x < target_radius or target_x > screen_width - target_radius:
        target_speed_x = -target_speed_x
    if target_y < target_radius or target_y > screen_height - target_radius:
        target_speed_y = -target_speed_y

    # Очистка экрана
    screen.fill(white)
    # Рисуем цель
    pygame.draw.circle(screen, red, (target_x, target_y), target_radius)
    # Вывод счета
    text = font.render(f'Score: {score}', True, black)
    screen.blit(text, (10, 10))
    # Обновление экрана
    pygame.display.flip()

    pygame.time.delay(10)

pygame.quit()