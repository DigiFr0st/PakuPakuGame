import pygame
import spritesheet


class PlayerAnimation:
    DOWN = 0
    LEFT = 1
    UP = 2
    RIGHT = 3
    BACKGROUND_COLOR = "black"

    def __init__(self, image):
        self.player_spritesheet = spritesheet.SpriteSheet(image)
        self.player_direction = PlayerAnimation.DOWN
        self.player_animation_frame_list = []
        self.frames_per_direction = 4
        self.animation_direction_count = 4
        self.frame_number = 0
        self.animation_cooldown = 250
        self.last_update = pygame.time.get_ticks()

        # creates a list of 16 character frames for walking in cardinal directions
        for x in range(self.animation_direction_count):
            for y in range(self.frames_per_direction):
                self.player_animation_frame_list.append(
                    self.player_spritesheet.get_player_image_scaled(
                        y, x, PlayerAnimation.BACKGROUND_COLOR, 16, 32, 2
                    )
                )

    # updates the player frame during idle time
    def update_player_frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.animation_cooldown:
            if self.player_direction == PlayerAnimation.DOWN and self.frame_number >= 3:
                self.frame_number = 0
            elif self.player_direction == PlayerAnimation.LEFT and (
                self.frame_number >= 7 or self.frame_number < 4
            ):
                self.frame_number = 4
            elif self.player_direction == PlayerAnimation.UP and (
                self.frame_number >= 11 or self.frame_number < 8
            ):
                self.frame_number = 8
            elif self.player_direction == PlayerAnimation.RIGHT and (
                self.frame_number >= 15 or self.frame_number < 12
            ):
                self.frame_number = 12
            else:
                self.frame_number += 1
            self.last_update = current_time
        return self.player_animation_frame_list[self.frame_number]

    # updates the player frame when player uses w/a/s/d keys
    def update_from_key_press(self, new_direction):
        self.player_direction = new_direction
        if self.player_direction == PlayerAnimation.DOWN and self.frame_number > 3:
            self.frame_number = 0
        if self.player_direction == PlayerAnimation.LEFT and (
            self.frame_number > 7 or self.frame_number < 4
        ):
            self.frame_number = 4
        if self.player_direction == PlayerAnimation.UP and (
            self.frame_number > 11 or self.frame_number < 8
        ):
            self.frame_number = 8
        if self.player_direction == PlayerAnimation.RIGHT and self.frame_number < 12:
            self.frame_number = 12
