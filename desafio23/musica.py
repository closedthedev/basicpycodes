#reproduzindo um arquivo mp3

import pygame

# Inicialize o pygame
pygame.init()

# Carregue a música
pygame.mixer.music.load("musicahaha.mp3")

# Inicie a reprodução da música
pygame.mixer.music.play()

# Mantenha o programa em execução enquanto a música está sendo reproduzida
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)