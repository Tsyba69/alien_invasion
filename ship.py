import pygame


class Ship():
    """класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')  # Загружает изображение корабля
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

