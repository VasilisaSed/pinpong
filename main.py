from pygame import *


FPS = 60
window = display.set_mode((700,500))
display.set_caption('pygame window')
background = transform.scale(image.load('window.png'),(700,500))
clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_im, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_im),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
        self.height = height

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - self.width:
            self.rect.x += self.speed

class Ball(GameSprite):
    def __init__(self, player_im, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.speed_x = player_speed
        self.speed_y = player_speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y;
        if self.rect.x <= 0 or self.rect.x >= 700 - self.width:
            self.speed_x *= -1
        if self.rect.y <= 0 or self.rect.y >= 500 - self.height:
            self.speed_y *= -1


player_1 = Player('platforn.png', 300, 20, 100, 20, 5)
player_2 = Player('platforn.png', 300, 400, 100, 20,5)
ball = Ball('ballball.png', 300, 250, 40, 40, 4)

game = True
finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player_1.update()
        player_1.reset()

        player_2.update()
        player_2.reset()

        ball.update()
        ball.reset()

    display.update()
    clock.tick(FPS)
