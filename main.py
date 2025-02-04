import pygame
import sys


pygame.mixer.init()
pygame.mixer.music.load('sounds/sounds1.mp3')
menu_sounds = pygame.mixer.Sound("sounds/menu_sounds.wav")


def show_menu(screen, menu_image):
    while True:
        screen.fill('black')
        screen.blit(menu_image, (screen.get_width() // 2 - menu_image.get_width() // 2, screen.get_height() // 2 - menu_image.get_height() // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    menu_sounds.play()
                    pygame.mixer.music.play(-1)
                    return