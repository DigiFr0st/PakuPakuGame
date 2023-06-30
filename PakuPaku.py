import pygame

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('PakuDex')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
