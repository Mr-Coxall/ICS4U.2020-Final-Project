import pygame


class Sprites:
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        self._sprite = sprite
        self._sprite_x = sprite_x
        self._sprite_y = sprite_y
        self._x_speed = x_speed
        self._y_speed = y_speed
        self._screen = screen
        self.width = self._sprite.get_width()
        self.height = self._sprite.get_height()
        self.moving_rect = pygame.Rect(
            self._sprite_x, self._sprite_y, self.width, self.height
        )
        self.current_sprite = 0

    def sprite_upload(self):
        self._screen.blit(self._sprite, (self.moving_rect.x, self.moving_rect.y))

    def flip_sprite(self):
        self._sprite = pygame.transform.flip(self._sprite, True, False)

    def set_moving_rect(self, new_rect):
        self.moving_rect = new_rect

    def modify_sprite_size(self, multiplier):
        # get sprite's size
        sprite_size = self._sprite.get_size()
        # increase size of sprite and rect
        self._sprite = pygame.transform.scale(
            self._sprite, (sprite_size[0] * multiplier, sprite_size[1] * multiplier)
        )
        self.moving_rect.size = self._sprite.get_size()

    def check_collision(self, sprite1, sprite2):
        if sprite1.colliderect(sprite2):
            return True
        else:
            return False

    def sprite_move(self, x_change, y_change):
        self.moving_rect.x += x_change
        self.moving_rect.y += y_change

    def sprite_animation(self, sprite_list):
        self.current_sprite += 1
        if self.current_sprite >= len(sprite_list):
            self.current_sprite = 0

    def get_rect(self):
        return self.moving_rect

    def get_sprite_x(self):
        return self._sprite_x

    def set_sprite_x(self, new_sprite_x):
        self._sprite_x = new_sprite_x

    def get_sprite_y(self):
        return self._sprite_y

    def set_sprite_y(self, new_sprite_y):
        self._sprite_y = new_sprite_y

    def get_x_speed(self):
        return self._x_speed

    def set_x_speed(self, new_x_speed):
        self._x_speed = new_x_speed

    def get_y_speed(self):
        return self._y_speed

    def set_y_speed(self, new_y_speed):
        self._y_speed = new_y_speed

    def get_sprite(self):
        return self._sprite

    def set_sprite(self, new_sprite):
        self._sprite = new_sprite

    def draw_rect(self):
        pygame.draw.rect(self._screen, (255, 0, 0), self.moving_rect)
