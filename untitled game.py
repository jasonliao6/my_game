import pygame, sys
import random
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((800, 600))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50))
##        self.image.fill(('#fccc6d'))
        scratch_pic = pygame.image.load("slime.webp")
        self.image = pygame.transform.scale(scratch_pic, (50,50))
        self.rect = self.image.get_rect()
        a = random.randint(0,800)
        b = random.randint(0,600)
        self.rect.center = (a,b)

    def update(self):
    #keypress       
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.rect.y -= 3
        if keystate[pygame.K_s]:
            self.rect.y += 3
        if keystate[pygame.K_a]:
            self.rect.x -= 3
        if keystate[pygame.K_d]:
            self.rect.x += 3
    #wall detection       
        if self.rect.x > 750:
            self.rect.x = 750
        if self.rect.y > 550:
            self.rect.y = 550
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
        

while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

        
  display.fill('#abf9ff')

  player_group.draw(display)
  player.update()
  pygame.display.update()
  clock.tick(120)
  
