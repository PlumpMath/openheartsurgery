##imports

import pygame, sys, gangster, reticule, bg
from pygame.locals import *

background=None
windowSurfaceObj=None

##initialization
def init():
  pygame.init()
  global reticuleHeartSprite
  reticuleHeartSprite = pygame.image.load('assets/reticuleheart.png')
  global reticuleSprite
  reticuleSprite = pygame.image.load('assets/reticule.png')
  global windowSurfaceObj
  windowSurfaceObj = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
  global background
  cfg = open('cfg/level1.cfg')
  numberOfGangsters = int(cfg.readline())
  global gang
  gang = gangster.gang(numberOfGangsters, cfg)
  tiles = []  
  for tile in cfg.readline().split():
    tiles.append(int(tile))
  background = bg.bg(tiles)
  pygame.display.set_caption('Heartless Killer')


##control loop
def game_loop():
  global windowSurfaceObj
  fpsClock=pygame.time.Clock()
  ret = reticule.reticule(reticuleHeartSprite, reticuleSprite, gang)
  mousex, mousey = 600,200
  while True:
    
    #Housekeeping


    #Drawing control
    #windowSurfaceObj.fill(pygame.Color(255,255,255))
    windowSurfaceObj.blit(background.get_bg(),(0,0))
    for g in gang.characters:
      g.move(background,windowSurfaceObj,gang)
      if g.y>400:
        if g.tier != gangster.Tier.Sewer:
          g.tier=gangster.Tier.Sewer
          if g.pc:
            ret.findTarget(gang)
      elif g.y<250:
        g.tier=gangster.Tier.Rooftops
      else:
        if g.tier != gangster.Tier.Street:
          g.tier=gangster.Tier.Street
          if g.pc:
            ret.findTarget(gang)
      g.draw(windowSurfaceObj)
    gang.drawHeart(windowSurfaceObj)
    if gang.player.shooting:
      ret.shoot(gang,background, windowSurfaceObj)
    ret.draw(windowSurfaceObj,gang)
    pygame.draw.rect(windowSurfaceObj,pygame.Color(73,36,0),(0,403,800,41))
    
    #Event control
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
        #move reticule between enemies
        if event.key == K_UP:
          ret.moveUp(gang)
        if event.key == K_DOWN:
          ret.moveDown(gang)
        if event.key == K_LEFT:
          ret.moveLeft(gang)
        if event.key == K_RIGHT:
          ret.moveRight(gang)
        #move left, right, ladders
        if event.key == K_w:
          #climb a ladder up
           gang.player.setYVelocity(-3)
        if event.key == K_s:
          #climb a ladder down
           gang.player.setYVelocity(3)
        if event.key == K_a:
          #move left
            gang.player.setXVelocity(-5)
        if event.key == K_d:
          #move right
            gang.player.setXVelocity(5)
        #combat 
        if event.key == K_LSHIFT:
          #shoot
          ret.shoot(gang,background, windowSurfaceObj)
        if event.key == K_SPACE:
	  #heart jump
          if ret.heartJumpCheck(gang):
            background.splatter(gang.player.x,gang.player.y)
          if ret.heartJump(gang):
            background.splatter(ret.target.x,ret.target.y)
            ret.findTarget(gang)
        if event.key == K_ESCAPE:
            sys.exit()

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
            gang.player.setYVelocity(3)
        if event.key == K_s:
           #climb a ladder down
            gang.player.setYVelocity(-3)
        if event.key == K_a:
          #move left
            gang.player.setXVelocity(5)
        if event.key == K_d:
          #move right
            gang.player.setXVelocity(-5)
         #combat 
        if event.key == K_LSHIFT:
          #shoot
          ret.stop_shooting(gang)
        if event.key == K_SPACE:
      #heart jump
	        pass
  ##Framerate control
    pygame.display.update()
    fpsClock.tick(30)

if __name__=='__main__':
	init()
	game_loop()	
