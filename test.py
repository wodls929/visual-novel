import pygame

background = pygame.image.load("image/교실1.png")
background = pygame.transform.scale(background, (1000, 600))
pygame.image.save(background, '교실1(변경).png')