import time
import webbrowser
import os
import pygame
print('====== EXERCÍCIO 21 ======')

# Exercício Python 21: Faça um programa em Python que abra
# e reproduza o áudio de um arquivo MP3.

pygame.init()
pygame.mixer.music.load('audiodd.mp3') # o arquivo deve estar na mesma pasta que o ex021.py
pygame.mixer.music.play()
while True:
    print("Aperte 'p' para pausar, 'r' para retomar")
    print("Aperte 'f' para fechar")
    query = input("Sua opcão: ")

    if query == 'p':
        pygame.mixer.music.pause()
    elif query == 'r':
        pygame.mixer.music.unpause()
    elif query == 'f':
        pygame.mixer.music.stop()
        break

# Outra forma
# webbrowser.open('audiodd.mp3') # o arquivo deve estar na mesma pasta que o ex021.py
# os.system('start ' + 'audiodd.mp3')


