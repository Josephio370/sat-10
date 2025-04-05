#Create your own shooter
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 445:
            self.rect.y += self.speed
            
class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed  
            
                    
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'   
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):        
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        
        self.image = Surface([self.width,self.height])
        self.image.fill((color_1,color_2,color_3))
        
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        
    def draw_wall(self):
        draw.rect(window,(self.color_1,self.color_2,self.color_3),(self.rect.x,self.rect.y,self.width,self.height))
        
        
        
        
#create game window
init()
font.init()

win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption('Maze')

#set scene background
background = transform.scale(image.load('background.jpg'),(700,500))

w1 = Wall(154,205,50,100,20,450,10)
w2 = Wall(154,205,50,100,480,350,10)
w3 = Wall(154,205,50,100,20,10,380)
w4 = Wall(154,205,50,200,130,10,350)
w5 = Wall(154,205,50,450,130,10,360)
w6 = Wall(154,205,50,300,20,10,350)
w7 = Wall(154,205,50,390,120,130,10)

player = Player('hero.png',5,win_height-80,4)
player2 = Player2('hero2.png',5,win_height-80,4)
monster = Enemy('cyborg.png',win_width - 80,280,2)
goal = GameSprite('treasure.png',win_width - 120,win_height-80,0)

#FONT
typefont = font.Font(None,70)
p1win = typefont.render("P1 Win!!",True,(255,215,0))
p2win = typefont.render("P2 Win!!",True,(255,215,0))
p1lose = typefont.render("P1 Lose!!",True,(255,215,0))
p2lose = typefont.render("P2 Lose!!",True,(255,215,0))


#Music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
#handle "click on the "Close the window"" event 
run = True
clock = time.Clock()
FPS = 60
score = 0
finish =False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))        
        player.update()
        player.reset()
        player2.update()
        player2.reset()
        monster.update()
        monster.reset()
        goal.reset()
        
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        
        if sprite.collide_rect(player,monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3)\
            or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6 or sprite.collide_rect(player,w7)):
                finish = True
                window.blit(p1lose,(200,200))
                kick.play()
        if sprite.collide_rect(player,goal):
            finish = True
            window.blit(p1win,(200,200))
            money.play()
        
        if sprite.collide_rect(player2,monster) or sprite.collide_rect(player2,w1) or sprite.collide_rect(player2,w2) or sprite.collide_rect(player2,w3)\
            or sprite.collide_rect(player2,w4) or sprite.collide_rect(player2,w5) or sprite.collide_rect(player2,w6 or sprite.collide_rect(player2,w7)):
                finish = True
                window.blit(p2lose,(200,200))
                kick.play()
        
        if sprite.collide_rect(player2,goal):
            finish = True
            window.blit(p2win,(200,200))
            money.play()
    display.update()
    clock.tick(FPS)