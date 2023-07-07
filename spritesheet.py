import pygame


class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    # function returns the player sprite scaled with transparent background
    def get_player_image_scaled(
        self,
        frame_value,
        direction_value,
        color_key,
        player_width,
        player_height,
        scale,
    ):
        image = pygame.Surface((player_width, player_height)).convert_alpha()
        image.blit(
            self.sheet,
            (0, 0),
            (
                (frame_value * player_width),
                (direction_value * player_height),
                player_width,
                player_height,
            ),
        )
        image = pygame.transform.scale(
            image, (player_width * scale, player_height * scale)
        )
        image.set_colorkey(color_key)
        return image
