import pygame
import pygame_gui
import ant

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600

pygame.init()

pygame.display.set_caption("Ant Sim")
main_surface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
grid_surface = pygame.display.set_mode((600, 600))
text_surface = pygame.display.set_mode((200, 600))

background = pygame.Surface((WINDOW_HEIGHT, WINDOW_WIDTH))
background.fill(pygame.Color('#123548'))

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        main_surface.blit(background, (0,0)) #sets the background color
        pygame.display.update()