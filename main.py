##imports
import pygame, sys, gangster, bg
from pygame.locals import *

aimingReticuleSurfaceObj=None
background=None
windowSurfaceObj=None

##initialization
def init():
  pygame.init()
  global reticuleSprite
  reticuleSprite = pygame.image.load('assets/reticule.png')
  global gangsterSprite
  gangsterSprite= pygame.image.load('assets/gangstersheet.png')
  global windowSurfaceObj
  windowSurfaceObj = pygame.display.set_mode((800, 600))
  global background
  background = bg.bg([1,0,3,2])
  pygame.display.set_caption('Heartless Killer')


##control loop
def game_loop():
  global windowSurfaceObj
  fpsClock=pygame.time.Clock()
  gang = []
  tempx = 10
  for g in range(5):
    gang.append(gangster.gangster(gangsterSprite, tempx))
    tempx += 100
  gang[0].pc = True
  player = filter(lambda g: g.pc == True, gang)[0]
  mousex, mousey = 600,200
  while True:
    
    #Housekeeping


    #Drawing control
    #windowSurfaceObj.fill(pygame.Color(255,255,255))
    windowSurfaceObj.blit(background.get_bg(),(0,0))
    for g in gang:
      g.move(background)
      g.draw(windowSurfaceObj)
    
    #Event control
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
        #move reticule between enemies
        if event.key == K_UP:
          #move reticule to nearest higher-level thug
          pass
        if event.key == K_DOWN:
          #move reticule to nearest lower-level thug
          pass
        if event.key == K_LEFT:
          #move reticule to nearest thug to the left
          pass
        if event.key == K_RIGHT:
          #move reticule to neartest thug to the right
          pass
        #move left, right, ladders
        if event.key == K_w:
          #climb a ladder up
           player.setYVelocity(-3)
        if event.key == K_s:
          #climb a ladder down
           player.setYVelocity(3)
        if event.key == K_a:
          #move left
            player.setXVelocity(-5)
        if event.key == K_d:
          #move right
            player.setXVelocity(5)
        #combat 
        if event.key == K_LSHIFT:
          #shoot
          pass
        if event.key == K_SPACE:
	  #heart jump
          pass
      elif event.type == KEYUP:
      #move reticule between enemies
        if event.key == K_UP:
          #move reticule to nearest higher-level thug
          pass
        if event.key == K_DOWN:
          #move reticule to nearest lower-level thug
          pass
        if event.key == K_LEFT:
          #move reticule to nearest thug to the left
          pass
        if event.key == K_RIGHT:
          #move reticule to neartest thug to the right
          pass
        #move left, right, ladders
        if event.key == K_w:
          #climb a ladder up
            player.setYVelocity(3)
        if event.key == K_s:
           #climb a ladder down
            player.setYVelocity(-3)
        if event.key == K_a:
          #move left
            player.setXVelocity(5)
        if event.key == K_d:
          #move right
            player.setXVelocity(-5)
         #combat 
        if event.key == K_LSHIFT:
          #shoot
          pass
        if event.key == K_SPACE:
      #heart jump
          pass


  ##Framerate control
    pygame.display.update()
    fpsClock.tick(30)

if __name__=='__main__':
	init()
	game_loop()	
