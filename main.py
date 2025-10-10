import pygame
import random
import asyncio

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Shootout Night")
icon_image = pygame.image.load("Assets/ShootoutNightIcon.png")
pygame.display.set_icon(icon_image)
clock = pygame.time.Clock()

async def game():
    dt = 0
    baseTime = 1000
    shotCD = 0
    enemySpawnCD = 150
    enemyCount = 0
    score = 0
    level = 1
    levelTimer = 500
    levelMult = 1
    ambientTune = pygame.mixer.music.load("Assets/ShootoutNightAmbience.ogg")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    enemy_pos = pygame.Vector2(0,0)

    class player(object):
            def __init__(self, x, y, width, height):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.speed = 200
            def draw(self,player_pos):
                pygame.draw.circle(screen, "white", player_pos, 15)

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

        def draw(self):
                pygame.draw.circle(screen, "gray", pygame.Vector2(self.x,self.y), self.radius)

    def redrawGameScreen():
        screen.fill("black")
        protagonist.draw(player_pos)
        for bullet in bullets:
            bullet.draw(screen)
        for thug in enemies:
            thug.draw()
        #show_score()
        pygame.display.flip()

    #def show_score():
    #    score_obj = pygame.font.SysFont('comicsans',50,True)
    #    score_txt = score_obj.render("Score: " +str(score) ,1, (255,255,255))
    #    screen.blit(score_txt,(30,5))



    # MainLoop
    protagonist = player(screen.get_width() / 2, screen.get_height() / 2,0,0)
    running = True
    bullets = []
    enemies = []
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        pygame.display.set_caption("Shootout Night"+"      Score: "+str(score)+"        Level: "+str(level)+"     Level Timer: "+str(levelTimer))


        # Movimentação dos Disparos
        for bullet in bullets:
            if bullet.x < 1280 and bullet.x > 0 and bullet.y < 720 and bullet.y > 0:
                bulletCollisionRect = pygame.Rect(bullet.x-bullet.radius,bullet.y-bullet.radius,bullet.radius*2,bullet.radius*2)
                match bullet.party:
                    case 1: #Disparos do Player
                        bullet.x += bullet.direction.x*10
                        bullet.y += bullet.direction.y*10
                        for thug in enemies:
                            enemyCollisionRect = pygame.Rect(thug.x-thug.radius,thug.y-thug.radius,thug.radius*2,thug.radius*2)
                            if bulletCollisionRect.colliderect(enemyCollisionRect):
                                enemies.pop(enemies.index(thug))
                                bullets.pop(bullets.index(bullet))
                                score +=1
                    case 2: #Disparos dos Inimigos
                        bullet.x += (bullet.direction.x-bullet.spawnX)/25
                        bullet.y += (bullet.direction.y-bullet.spawnY)/25
                        playerCollisionRect = pygame.Rect(player_pos.x-15,player_pos.y-15,30,30)
                        if bulletCollisionRect.colliderect(playerCollisionRect):
                            bullets.pop(bullets.index(bullet))
                            running = False
            else: bullets.pop(bullets.index(bullet))


        keysPress = pygame.key.get_pressed()
        run = pygame.key.get_mods()

        #Controle do Level
        if levelTimer > 0 and level < 4:
            levelTimer-=1
        elif level != "MAX":
            if level < 4:
                level +=1
                if level == 2:
                    levelMult = 0.8
                if level == 3:
                    levelMult = 0.6
            else:
                levelMult = 0.4
            if level < 4:
                levelTimer = int(500/levelMult)
            if level == 4:
                level = "MAX"

        #Inimigos Spawnando
        if enemySpawnCD > 0:
            enemySpawnCD -=1
        elif level != "MAX":
            enemySpawnSide = random.randint(1, 4)
            match enemySpawnSide:
                case 1:
                    enemies.append(enemy(random.randint(50, 1230), -50,15,15,15,1,random.randint(50, 1230),50))
                case 2:
                    enemies.append(enemy(random.randint(50, 1230), 770,15,15,15,1,random.randint(50, 1230), 670))
                case 3:
                    enemies.append(enemy(-50, random.randint(50,670),15,15,15, 1, 50,random.randint(50,670)))
                case 4:
                    enemies.append(enemy(1330, random.randint(50, 670),15,15,15,1, 1230,random.randint(50, 670)))
            enemySpawnCD = 150*levelMult
        elif level == "MAX":
            enemySpawnSide = random.randint(1, 4)
            match enemySpawnSide:
                case 1:
                    enemies.append(enemy(random.randint(50, 1230), -50,15,15,15, 3,random.randint(50, 1230),random.randint(50, 670)))
                case 2:
                    enemies.append(enemy(random.randint(50, 1230), 770,15,15,15, 3,random.randint(50, 1230), random.randint(50, 670)))
                case 3:
                    enemies.append(enemy(-50, random.randint(50,670),15,15,15, 3,random.randint(50, 1230), random.randint(50,670)))
                case 4:
                    enemies.append(enemy(1330, random.randint(50, 670),15,15,15, 3,random.randint(50, 1230), random.randint(50, 670)))
            enemySpawnCD = 150*levelMult

        #Inimigos Andando e Disparando
        for thug in enemies:
            thug.thugShotCD -=1
            if thug.thugShotCD == 0:
                bullets.append(projectile(round(thug.x),round(thug.y),round(thug.x),round(thug.y),3,"gray",pygame.Vector2(player_pos.x,player_pos.y),2))
                #print (str(player_pos.x)+" "+str(player_pos.y))
                thug.thugShotCD = 100
            if (thug.x < thug.targetStopX):
                thug.x +=thug.speed
            elif (thug.x > thug.targetStopX):
                thug.x -=thug.speed
            if (thug.y < thug.targetStopY):
                thug.y +=thug.speed
            elif (thug.y > thug.targetStopY):
                thug.y -=thug.speed


        #for thug in enemies:

        # Player Atirando
        if shotCD > 0:
            shotCD -= 1
        else:
            if keysPress[pygame.K_LEFT]:
                bullets.append(projectile(round(player_pos.x-6),round(player_pos.y),round(player_pos.x-6),round(player_pos.y),3,"white",-pygame.Vector2(1,0),1))
            elif keysPress[pygame.K_RIGHT]:
                bullets.append(projectile(round(player_pos.x+6),round(player_pos.y),round(player_pos.x+6),round(player_pos.y),3,"white",pygame.Vector2(1,0),1))
            elif keysPress[pygame.K_UP]:
                bullets.append(projectile(round(player_pos.x),round(player_pos.y-6),round(player_pos.x),round(player_pos.y-6),3,"white",-pygame.Vector2(0,1),1))
            elif keysPress[pygame.K_DOWN]:
                bullets.append(projectile(round(player_pos.x),round(player_pos.y+6),round(player_pos.x),round(player_pos.y+6),3,"white",pygame.Vector2(0,1),1))
            shotCD = 40


        # Player Andando
        if keysPress[pygame.K_w] and player_pos.y > 20:
            if keysPress[pygame.K_LSHIFT] or keysPress[pygame.K_RSHIFT]:
                player_pos.y -= (2*protagonist.speed) * dt
            else : player_pos.y -= protagonist.speed * dt
        if keysPress[pygame.K_s] and player_pos.y < 702:
            if keysPress[pygame.K_LSHIFT] or keysPress[pygame.K_RSHIFT]:
                player_pos.y += (2*protagonist.speed) * dt
            else : player_pos.y += protagonist.speed * dt
        if keysPress[pygame.K_a] and player_pos.x > 20:
            if keysPress[pygame.K_LSHIFT] or keysPress[pygame.K_RSHIFT]:
                player_pos.x -= (2*protagonist.speed) * dt
            else : player_pos.x -= protagonist.speed * dt
        if keysPress[pygame.K_d] and player_pos.x < 1262:
            if keysPress[pygame.K_LSHIFT] or keysPress[pygame.K_RSHIFT]:
                player_pos.x += (2*protagonist.speed) * dt
            else : player_pos.x += protagonist.speed * dt


    # DrawScreen


        #//run = pygame.key.get_mods()
        #if run [pygame.KMOD_SHIFT]:

        # flip() the display to put your work on screen


        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / baseTime
        redrawGameScreen()
        await asyncio.sleep(0)  # Yield control to the event loop

    pygame.quit()

asyncio.run(game())
