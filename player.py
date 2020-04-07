import pygame, sys
from pygame.locals import *

class Player:
	def __init__(self, width = 0, height = 0, x = 0, y = 0,
				img = pygame.transform.scale(pygame.image.load('images/straight1.png'), (118, 94)),
				imgleft = pygame.transform.scale(pygame.image.load('images/left1.png'), (118, 94)),
				imgright = pygame.transform.scale(pygame.image.load('images/right1.png'), (118, 94)), dxs = 0):
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
		#original reference image (to prevent quality loss from transformations)
		self.img = img
		self.imgleft = imgleft
		self.imgright = imgright
		#image to be displayed while running
		self.image = pygame.transform.rotate(self.img, 0)
		#xadjust and yadjust are constants to make the x and y coordinates in the self.hitbox correspond with the center of the image
		self.xadjust = -width/2
		self.yadjust = -height/2
		#hitbox- simplifies boundaries for collision or eating detection
		self.hitbox = (self.x+self.xadjust, self.y+self.yadjust, self.width, self.height)
		#number of bugs the self has eaten
		self.dxs = 0
	def move(self):
		 #change x by dx
		self.x += self.dx + self.dxs
		 #change y by dy
		self.y += self.dy
		#moves the hitbox so that it always corresponds to the position
		self.hitbox = (self.x+self.xadjust, self.y+self.yadjust, self.width, self.height)
	def gameover(self):
		#stops along x axis
		self.dx = 0
		#stops along y axis
		self.dy = 0
