import pygame

# pygame setup pieces
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PakuDex")
clock = pygame.time.Clock()
game_Running = True
dt = 0

player_Pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ground_surface = pygame.image.load("maps/town_1_1.png")
map_width = ground_surface.get_width()
map_height = ground_surface.get_height()
scaled_GS = pygame.transform.scale(ground_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))

while game_Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_Running = False

    # fill the game screen to remove anything from the last frame
    screen.fill("black")

    # render game here
    screen.blit(scaled_GS, (0, 0))
    player = pygame.draw.circle(screen, "red", player_Pos, 10)

    # screen.blit(red_surface, (200, 100))

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

    dt = clock.tick(60) / 2000

pygame.quit()
exit()
