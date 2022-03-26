import pygame
from time import sleep
pygame.init()
window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('Ratsasan Piano BGM.mp3')
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load('haunting.mp3')
pygame.mixer.music.play()
sleep(1)
image=pygame.image.load('src.jpg')
window.blit(image,(450,40))
pygame.display.update()
sleep(3)



