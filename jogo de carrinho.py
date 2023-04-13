import pygame
from random import randint
pygame.init()

janela = pygame.display.set_mode((980,600))
pygame.display.set_caption("Criando um jogo com developer")

x_fundo = 480 #max 653 min 321
y_fundo = 100

pos_x = 323
pos_y= 800
pos_y_a = 800
pos_y_c = 800

velocidade = 15
velocidade_outros = 20

fundo = pygame.image.load('estrada.png')
carroVermelho = pygame.image.load('carro vermelho.png')
policia = pygame.image.load('carro policia.png')
carroVerde = pygame.image.load('carro verde.png')
carroAzul= pygame.image.load('carro azul.png')

janela_aberta = True
while janela_aberta :
  pygame.time.delay(50)

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
         janela_aberta = False

  comandos = pygame.key.get_pressed()
  if comandos[pygame.K_RIGHT] and x_fundo<= 653:
      x_fundo += velocidade
  if comandos[pygame.K_LEFT] and x_fundo>= 321:
      x_fundo -= velocidade

  if (pos_y <=-180) and (pos_y_a <= -180) and (pos_y_c <= -180) :
      pos_y= randint (800,2000)
      pos_y_a = randint (800,2000) 
      pos_y_c = randint (800,2000)

  pos_y -= velocidade_outros
  pos_y_a -= velocidade_outros +2
  pos_y_c -= velocidade_outros+5    #carro verde

  janela.blit(fundo,(0,0))
  janela.blit(carroVermelho,(x_fundo - 30, y_fundo))
  janela.blit(policia, (pos_x, pos_y))
  janela.blit(carroVerde, (pos_x + 140, pos_y_c))
  janela.blit(carroAzul, (pos_x + 270, pos_y_a))
  pygame.display.update()

pygame.quit()

#%%
