import pygame, sys
import random
import math
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.font.init()
my_font = pygame.font.SysFont('comicsans', 50)
SCREEN_X, SCREEN_Y = display.get_size()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50))
##        self.image.fill(('#fccc6d'))
        scratch_pic = pygame.image.load("slime.jpeg")
        self.image = pygame.transform.scale(scratch_pic, (50,50))
        self.rect = self.image.get_rect()
        a = random.randint(0,800)
        b = random.randint(0,600)
        self.rect.center = (a,b)


    def update(self):
    #keypress       
##        keystate = pygame.key.get_pressed()
##        if keystate[pygame.K_w]:
##            self.rect.y -= 3
##        if keystate[pygame.K_s]:
##            self.rect.y += 3
##        if keystate[pygame.K_a]:
##            self.rect.x -= 3
##        if keystate[pygame.K_d]:
##            self.rect.x += 3
        self.rect.center = pygame.mouse.get_pos()
    #wall detection       
        if self.rect.x > SCREEN_X-50:
            self.rect.x = SCREEN_X-50
        if self.rect.y > SCREEN_Y-50:
            self.rect.y = SCREEN_Y-50
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a1 = random.randint(-300, 0)
        a2 = random.randint(SCREEN_X,SCREEN_X+400)
        if random.randint(0,1) == 1:
            a = a1
            self.k = random.randint(1,5)
        else:
            a = a2
            self.k = random.randint(-5, -1)
        b1 = random.randint(-300, 0)
        b2 = random.randint(SCREEN_Y, SCREEN_Y+300)
        if random.randint(0,1) == 1:
            b = b1
            self.o = random.randint(1, 5)
        else:
            b = b2
            self.o = random.randint(-5,-1)

        enemy = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(enemy, (50,50))
        x = self.k
        y = self.o
        angle = -180/math.pi*math.sin(x*y)*math.atan((abs(x)-abs(y))/(abs(x)+abs(y))) -135

##        print(angle)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = (a,b)

    def update(self):
        self.rect.x += self.k
        self.rect.y += self.o

        ##UNDERNEATH HERE YOU WILL BE ABLE TO MAKE CHEAT BUTTON
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            if keystate[pygame.K_b]:
                if keystate[pygame.K_c]:
                    self.k = 0
                    self.o = 0
##      something
##      somwthing else
        



def Game_over(rScore):
    text = my_font.render('Press r to restart', False, ('#f7ce5c'))
    quitT = my_font.render('Press q to quit', False, ('#f7ce5c'))
    scoreT = my_font.render(f'Score: {rScore}', False, ('#f7ce5c'))
    ma = 0
    mb = 0
    x=3
    y=3
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        
        ma += x
        mb += y
        if ma > SCREEN_X-400:
            x /= -1
        if mb > SCREEN_Y-50:
            y /= -1
        if ma < 0:
            x /= -1
        if mb < 0:
            y /= -1 
##        
        display.fill('#abf9ff')
        display.blit(text,(ma,mb))
        display.blit(quitT,(0,50))
##        display.blit(text, (200,250))
        display.blit(scoreT, (0,0))
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_r]:
            break
        if keystate[pygame.K_q]:
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(120)
    game_loop()

        
def game_loop():
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    num = 0
    hardest = 5
    score = 0
    dif = 30
    enemy_group = pygame.sprite.Group()

    while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            
      display.fill('#abf9ff')
      num += 1
      score += 1/120
      if num >= dif:
          enemy_group.add(Enemy())#adding an enemy
          num = 0
          dif -= 0.3
          if dif <= hardest:
              dif = hardest

    ##  if num % 5 == 0:
    ##     image = pygame.transform.rotate(Enemy, 5)

      player_group.draw(display)
      enemy_group.draw(display)
      player.update()
      for enemy in enemy_group:
          enemy.update()

      if pygame.sprite.spritecollideany(player, enemy_group) != None:
          print("Game Over")
          
          break

      roundedScore = round(score, 1)
      text = my_font.render(f'Score: {roundedScore}', False, ('#f7ce5c'))
      display.blit(text, (0, 0))    
      pygame.display.update()
      clock.tick(120)
      
    Game_over(roundedScore)
game_loop()

