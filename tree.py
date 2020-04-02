import pygame, sys
from pygame.locals import *
from road import Road

WIDTH = 800
HEIGHT = 500
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)

class Tree:
	def __init__(self, width = 0, height = 0, x = WIDTH/2, y = HEIGHT/2, img = pygame.transform.scale(pygame.image.load('images/tree.png'), (90, 120))):
		#hitbox width
		self.width = width
		#hitbox height
		self.height = height
		#x position
		self.x = x
		#y position
		self.y = y
		#change in x (if moving)
		self.dx = 0
		#change in y (if moving)
		self.dy = 0
		self.scaleby = 1
		#original reference image (to prevent quality loss from transformations)
		self.img = img
		#image to be displayed while running
		self.image = pygame.transform.scale(self.img, (9,12))
		#xadjust and yadjust are constants to make the x and y coordinates in the self.hitbox correspond with the center of the image
		self.xadjust = -width/2
		self.yadjust = -height/2
		#hitbox- simplifies boundaries for collision or eating detection
		self.hitbox = (self.x+self.xadjust, self.y+self.yadjust, self.width, self.height)
		#number of bugs the self has eaten
		self.dscaleby = 0
	def update(self):
		 #change x by dscaleby
		self.x += 4*self.dscaleby
		 #change y by dscaleby
		self.y += 6*self.dscaleby
		self.scaleby += self.dscaleby
		#moves the hitbox so that it always corresponds to the position
		self.hitbox = (self.x+self.xadjust, self.y+self.yadjust, self.width, self.height)
		DISPLAY.blit(self.image, (self.x,self.y))
		self.image = pygame.transform.scale(self.img, (int(9*self.scaleby),int(12*self.scaleby)))

	def gameover(self):
		#stops along x axis
		self.dx = 0
		#stops along y axis
		self.dy = 0
