import pygame
from time import sleep

pygame.init()  #initialize pygame

window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)  #display screen

pygame.mixer.init()  #for audio
pygame.mixer.music.load('ratsasan.mp3')   #load audio file
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()
sleep(1)

image=pygame.image.load('scr.jpg')   #image load
window.blit(image,(0,0))
pygame.display.update()
sleep(2)
