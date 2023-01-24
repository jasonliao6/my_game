import pygame, sys
import random
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
        scratch_pic = pygame.image.load("slime.webp")
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
        
        enemy = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(enemy, (50,50))
        self.rect = self.image.get_rect()
        a = random.randint(SCREEN_X,SCREEN_X+400)
        b = random.randint(0, SCREEN_Y)
        self.rect.center = (a,b)

        self.k = random.randint(2, 5)           
        self.o = random.randint(-3, 3)

    def update(self):
        self.rect.x -= self.k
        self.rect.y += self.o
##      something
        



def Game_over(rScore):
    text = my_font.render('Press r to restart', False, ('#f7ce5c'))
    scoreT = my_font.render(f'Score: {rScore}', False, ('#f7ce5c'))
    ma = 0
    mb = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        
        ma += 1
        mb += 1
##        if ma >= 500:
##            print('hi')
##        
        display.fill('#abf9ff')
        display.blit(text,(ma,mb))
##        display.blit(text, (200,250))
        display.blit(scoreT, (0,0))
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_r]:
            break

        pygame.display.update()
        clock.tick(120)
    game_loop()

        
def game_loop():
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    num = 0
    hardest = 20
    score = 0
    dif = 50
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
          dif -= 0.5
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

