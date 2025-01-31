import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

DIRECTS = [[0,-1], [1,0], [0,1], [-1,0]]

class Tank:
    def __init__(self, color, px, py, direct, keysList):
        objects.append(self)
        
        self.color = color
        self.rect = pygame.Rect(px, py, 50, 50)
        self.direct = direct
        self.moveSpeed = 2

        self.keyLEFT = keysList[0]
        self.keyRIGHT = keysList[1]
        self.keyUP = keysList[2]
        self.keyDOWN = keysList[3]
        self.keySHOT = keysList[4]

    def update(self):
        if keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2
        elif keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        
        x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        y = self.rect.centery + DIRECTS[self.direct][1] * 30
        pygame.draw.line(window, 'white', self.rect.center, (x, y), 4)


objects = []
Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
Tank('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RETURN))
        
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    for obj in objects: obj.update()

    window.fill('black')
    for obj in objects: obj.draw()
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
