import pygame
import playeranimation

pygame.init()

# constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
BACKGROUND_COLOR = "black"
DOWN = 0
LEFT = 1
UP = 2
RIGHT = 3

# initalization pieces
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PakuPaku")
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
# text_surface = test_font.render("Paku-Paku", True, "white")

# player animation
player_animation = playeranimation.PlayerAnimation(player_sprite_sheet_image)


while game_Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_Running = False

    # fill the game screen to remove anything from the last frame
    screen.fill(BACKGROUND_COLOR)

    # update animations
    current_frame = player_animation.update_player_frame()

    # render game here
    screen.blit(ground_surface, (0, 0))
    screen.blit(current_frame, player_Pos)

    # change player_pos based on key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        player_Pos.y += 300 * dt
        player_animation.update_from_key_press(DOWN)
    if keys[pygame.K_d]:
        player_Pos.x += 300 * dt
        player_animation.update_from_key_press(LEFT)
    if keys[pygame.K_w]:
        player_Pos.y -= 300 * dt
        player_animation.update_from_key_press(UP)
    if keys[pygame.K_a]:
        player_Pos.x -= 300 * dt
        player_animation.update_from_key_press(RIGHT)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 3000

pygame.quit()
exit()
