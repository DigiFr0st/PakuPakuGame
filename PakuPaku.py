import pygame

pygame.init()

# constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
BACKGROUND_COLOR = "black"

# initalization pieces
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PakuDex")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_Running = True
dt = 0
player_Pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# images for game
ground_image = pygame.image.load("maps/town_1_1.png")
# building_foreground_image = pygame.image.load("maps/building_foreground_layer.png")
player_sprite_sheet_image = pygame.image.load("sprites/character.png").convert_alpha()

# surfaces for game
ground_surface = pygame.transform.scale(ground_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
text_surface = test_font.render("Paku-Paku", False, "white")


def get_player_image_scaled(
    sheet,
    color_key,
    scale,
    player_width,
    player_height,
    sprite_x1,
    sprite_y1,
    sprite_x2,
    sprite_y2,
):
    image = pygame.Surface((player_width, player_height)).convert_alpha()
    image.blit(sheet, (0, 0), (sprite_x1, sprite_y1, sprite_x2, sprite_y2))
    image = pygame.transform.scale(image, (player_width * scale, player_height * scale))
    image.set_colorkey(color_key)
    return image


frame_0 = get_player_image_scaled(
    player_sprite_sheet_image, BACKGROUND_COLOR, 2, 16, 32, 0, 0, 16, 32
)


while game_Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_Running = False

    # fill the game screen to remove anything from the last frame
    screen.fill(BACKGROUND_COLOR)

    # render game here
    screen.blit(ground_surface, (0, 0))
    screen.blit(text_surface, (580, 0))
    # player = pygame.draw.circle(screen, "red", player_Pos, 10)
    screen.blit(frame_0, player_Pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_Pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_Pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_Pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_Pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1500

pygame.quit()
exit()
