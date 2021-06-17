# import pygame


class Maps:
    def __init__(self, sprite, tile_x_distance, tile_y_distance, screen):
        self._screen = screen
        self._sprite = sprite
        self._width = self._sprite.get_width()
        self._height = self._sprite.get_height()
        self._tile_x_distance = tile_x_distance
        self._tile_y_distance = tile_y_distance
        self._new_rect = self._sprite.get_rect()
        self._reduce_distance = self._tile_y_distance / 2

        self._game_scene_one_map = """





wwwwwwwwww  ww""".splitlines()

    # def build_map(self, sprite2):
    #     for line in self._game_scene_one_map:
    #         for character in line:
    #             if character == "w":
    #                 self._screen.blit(self._sprite,
    #                                   (self._tile_x_distance, self._tile_y_distance))
    #                 self.new_rect = pygame.Rect(self._tile_x_distance, self._tile_y_distance,
    #                                             self._width, self._height)

    # pygame.draw.rect(self._screen, (0, 0, 255), self.new_rect)
