import pygame

class enemy(object):
    def __init__(self, x, y, radius, width, height, speed, targetStopX,targetStopY,thugShotCD=200):
            self.x = x
            self.y = y
            self.radius = radius
            self.width = width
            self.height = height
            self.targetStopX = targetStopX
            self.targetStopY = targetStopY
            self.speed = speed
            self.thugShotCD = thugShotCD

    def draw(self, threat, screen):
        if threat != "MAX":
            enemyColor = "gray"
        else: enemyColor = "red"
        pygame.draw.circle(screen, enemyColor, pygame.Vector2(self.x,self.y), self.radius)

class player(object):
        def __init__(self, x, y, width, height, screen):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.speed = 200
            self.screen = screen

        def draw(self, player_pos):
            pygame.draw.circle(self.screen, "white", player_pos, 15)

class projectile(object):
    def __init__(self,x,y,spawnX,spawnY,radius,color,direction,party):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.party = party

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
