import webbrowser
import os
print('====== EXERCÍCIO 21 ======')

# Exercício Python 21: Faça um programa em Python que abra
# e reproduza o áudio de um arquivo MP3.

webbrowser.open('audiodd.mp3') # o arquivo deve estar na mesma pasta que o ex021.py
os.system('start ' + 'audiodd.mp3')
