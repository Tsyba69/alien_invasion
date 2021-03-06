import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши."""
        for event in pygame.event.get():  # Отслеживание событий клавиатуры и мыши.
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # Перемещение корабля вправо
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True  # Перемещение корабля влево

        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # Остановка перемещения корабля вправо
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False  # Остановка перемещения корабля влево

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)  # При каждом проходе цикла перерисовывается экран
        self.ship.blitme()
        pygame.display.flip()  # Отображение последнего прорисованного экрана


if __name__ == '__main__':
    ai = AlienInvasion()  # Cоздание экземпляра и запуск игры
    ai.run_game()
