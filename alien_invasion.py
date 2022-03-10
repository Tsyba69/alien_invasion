import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:

            for event in pygame.event.get():  # Отслеживание событий клавиатуры и мыши.
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)  # При каждом проходе цикла перерисовывается экран

            pygame.display.flip()  # Отображение последнего прорисованного экрана


if __name__ == '__main__':
    ai = AlienInvasion()  # создание экземпляра и запуск игры
    ai.run_game()
