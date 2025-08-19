from pygame import *
from random import *


height = 800
w_W = 600

win = display.set_mode((height, w_W))
display.set_caption("СЪЕШ ВСЕ")
background = transform.scale(image.load("CHARLOTTE.JPG"), (height, w_W))
ground = transform.scale(image.load("FON.png"), (height, w_W))
clock = time.Clock()

mixer.init()
mixer.music.load("Ink-black-Anxiety.ogg")
mixer.music.set_volume(0.3)
mixer.music.play(loops=-1)

font.init()
font1 = font.Font(None, 30)
font2 = font.Font(None, 50)

eaten = 0
missed = 0
lives = 5

class SpriteG(sprite.Sprite):
    def __init__(self, player_img, playerx, playery, player_speed, scalex, scaley):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (scalex, scaley))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = playerx
        self.rect.y = playery
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(SpriteG):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < height - 80:
            self.rect.x += self.speed

class Food(SpriteG):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 300:
            global missed
            self.rect.y = -60
            self.rect.x = randint(80, 620)
            self.speed = randint(3,4)
            missed +=1
        if sprite.spritecollide(CARTMAN, foods, True):
            global eaten
            eaten += 1
            while len(foods) < 3:

                food = Food("NASH.png", randint(80, 620), -60, self.speed, 70, 70)
                foods.add(food) 

class XIGERIS(SpriteG):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 300:
            global missed
            self.rect.y = -60
            self.rect.x = randint(80, 620)
            self.speed = randint(5,6)
            missed +=1
        if sprite.spritecollide(CARTMAN, xigerises, True):
            global lives
            lives -= 1
            while len(xigerises) < 2:

                xigeriss = XIGERIS("NewXigeris.png", randint(80, 620), -60, randint(5, 6), 50, 50)
                xigerises.add(xigeriss)

foods = sprite.Group()
for i in range(3):
    food = Food("NASH.png", randint(80, 620), -60, randint(3,4), 70, 70)
    foods.add(food) 
xigerises = sprite.Group()
for i in range(2):
    xigeriss = XIGERIS("NewXigeris.png", randint(80, 620), -60, randint(5, 6), 50, 50)
    xigerises.add(xigeriss)

CARTMAN = Player("CARTMAN.PNG", 400, 280, 5, 80, 80)


GAME = True
FINISH = False
while GAME:
    if not FINISH:
        missed_num = font1.render("Пропущено нашатр: " + str(missed), 1, (255, 255, 255))
        win_num = font1.render("Съедено нашатр: " + str(eaten), 1, (255, 255, 255))
        livings = font1.render("Жизни: " + str(lives), 1, (255, 255, 255))
        winntext = font2.render("ПОБЕДА!!!! ВСЕ НАШАТРЫ СЪЕДЕНЫ!!", 1, (255, 0, 0))
        LOSEEtext = font2.render("ПРОИГРЫШ!!((( НАШАТРЫ УБЕЖАЛИ!!(((", 1, (255, 0, 0))
        win.blit(background, (0, 0))
        win.blit(ground, (0, 0))
        CARTMAN.reset()
        CARTMAN.update()
        foods.draw(win)
        foods.update()
        xigerises.draw(win)
        xigerises.update()
        win.blit(missed_num, (10, 10))
        win.blit(win_num, (10, 40))
        win.blit(livings, (10, 70))
        if eaten == 20:
            FINISH = True
            win.blit(winntext, (80, 280))
            mixer.music.stop()
        if missed == 50 or lives == 0:
            FINISH = True
            win.blit(LOSEEtext, (80, 280))
            mixer.music.stop()
        
    for e in event.get():
        if e.type == QUIT:
            GAME = False

        


        
    display.update()
    clock.tick(60)


