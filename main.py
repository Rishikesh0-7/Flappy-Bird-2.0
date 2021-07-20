import pygame, sys , random
from pygame import *
import time
pygame.init()

class FlappyBird():
    def __init__(self):
        super().__init__()
        self.clock = pygame.time.Clock()
        self.width = 300
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.icon = pygame.image.load("assets/favicon.ico")
        pygame.display.set_caption("Flappy Bird")
        pygame.display.set_icon(self.icon)
        self.base_x = 0
        self.base_y = 400
        self.bird_y = 30
        self.bird_x = 0
        self.pipe_gap = 90
        self.pipe_x = self.width
        self.text = text = pygame.font.Font(None, 50)
        self.score = 0
        self.pipe_y = 200
        self.pipe_height = random.randint(100,200)
        self.gravity = 0.25
        self.move = 0
        self.bg_image = pygame.image.load("assets/background-day.png") #Bg image
        self.bg_image = pygame.transform.scale(self.bg_image, (self.width, self.height))
        self.base_image = pygame.image.load("assets/base.png")
        self.game_over = pygame.image.load("assets/gameover.png")
        self.flap_sound = pygame.mixer.Sound("sounds/wing.wav") #Game sounds
        self.hit_sound = pygame.mixer.Sound("sounds/hit.wav")
        self.point_sound = pygame.mixer.Sound("sounds/point.wav")
        self.down = pygame.image.load("assets/yellowbird-downflap.png") #Bird animations
        self.mid = pygame.image.load("assets/yellowbird-midflap.png")
        self.up = pygame.image.load("assets/yellowbird-upflap.png")
        self.bird_anim = [self.down, self.mid, self.up]
        
        self.ind = 0  #for bird animation!
        self.bird_width =  self.bird_anim[self.ind].get_width()
        

    def start(self):
        self.ind = 0
        while True:
            if self.ind < 2:
                self.ind +-1 
                time.sleep(0.1)
            else:
                self.ind = 0

            self.screen.blit(self.bg_image, (0, 0))
            message = pygame.image.load("assets/message.png")
            self.screen.blit(message, (50, 50))
            self.screen.blit(self.base_image , (self.base_x , self.base_y))
               #bird(bx,by)
            self.screen.blit(self.bird_anim[self.ind], (125, 217))
            pygame.display.update()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()
                    break
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.main()
                    
            self.clock.tick(60)
    def main(self):
        self.bird_y = 40
        self.pipe_x = self.width
        self.score = 0
        while True:
            self.pipe_x -= 2
            self.base_x -= 2
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()
                    break
                if ev.type == pygame.KEYDOWN: 
                    if ev.key == pygame.K_SPACE:
                        self.flap_sound.play()
                        self.move = 0
                        self.move -= 5     
                        if self.ind < 2:
                            self.ind += 1   
                        else:
                            self.ind = 0
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.flap_sound.play()
                    self.move = 0
                    self.move -= 5     
                    if self.ind < 2:
                        self.ind += 1   
                    else:
                        self.ind = 0
            if self.base_x <= -300:
                self.base_x = 0

            
            self.move += self.gravity
            self.bird_y += self.move
            if self.bird_y > self.base_y - 20:
                
                self.screen.blit(self.game_over, (50, 60))
                pygame.display.update()
                self.hit_sound.play()
                time.sleep(2)
                self.main()


            if self.pipe_x <= -50:
                self.point_sound.play()
                self.pipe_x = 300
                self.score += 1
                self.pipe_height = random.randint(100, 200)
                
            if self.pipe_x <= self.bird_x + self.bird_width and self.bird_x <= self.pipe_x + 52:
                if self.bird_y <= self.pipe_height or self.bird_y >= self.pipe_height + self.pipe_gap:
                    self.screen.blit(self.game_over, (50, 60))
                    pygame.display.update()
                    self.hit_sound.play()
                    time.sleep(2)
                    self.main()
            score_txt = self.text.render(f"{self.score}", True, (255, 255, 255))
            
            self.screen.blit(self.bg_image, (0, 0))
            pygame.draw.rect(self.screen, (160, 82, 45), (self.pipe_x, 0, 50, self.pipe_height))
            pygame.draw.rect(self.screen,	(160,82,45) , (self.pipe_x , self.pipe_height + self.pipe_gap , 50,500))
            self.screen.blit(self.base_image , (self.base_x , self.base_y))
            self.screen.blit(self.base_image, (self.base_x + 300, self.base_y))
            self.screen.blit(self.bird_anim[self.ind], (self.bird_x, self.bird_y))
            self.screen.blit(score_txt,(self.width // 2,50))
            pygame.display.update()
            self.clock.tick(60)


game = FlappyBird()
game.start()
game.clock.tick(60)