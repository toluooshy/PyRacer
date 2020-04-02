import pygame, sys
from pygame.locals import *
import numpy as np
from trackgenerator import TrackGenerator
import time

WIDTH = 800
HEIGHT = 500
DGRAY = (50,50,50)
LGRAY = (100,100,100)
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)

trackgen = TrackGenerator()
trackgen.generate()

class Road:
	def __init__(self, width = 1000, height = 2.5, x = 0, y = 0):
		self.roadwidth = width
		self.roadheight = height
		self.road = np.zeros(100, dtype=object)
		self.tilt = 0
		self.distance = 0
		self.accelerate = False
		self.reverse = False
		self.speed = 0
		self.sp = 0
		self.linecolor = 0

	def update(self):
		for roadslice in range(100):
			if self.linecolor % 2 != 0:
				self.road[roadslice] = pygame.draw.rect(DISPLAY, DGRAY, (((WIDTH/2)-(self.roadwidth/2) + (self.tilt*((roadslice*roadslice)/1000))), HEIGHT-2*(roadslice), int(self.roadwidth), int(self.roadheight)))
			if self.linecolor % 2 == 0:
				self.road[roadslice] = pygame.draw.rect(DISPLAY, LGRAY, (((WIDTH/2)-(self.roadwidth/2) + (self.tilt*((roadslice*roadslice)/1000))), HEIGHT-2*(roadslice), int(self.roadwidth), int(self.roadheight)))
			self.roadwidth-=10
			roadslice+=1
			self.linecolor += 1
		self.roadwidth=1000

	def readtrack(self):
		if self.distance >= len(trackgen.track):
			self.distance = 0
			print('lap')
		self.speed += self.sp
		if self.speed <= 0:
			self.speed = 0
		elif self.speed >= .07:
			self.speed = .07

		time.sleep(.1 - self.speed)
		if self.speed > 0:
			if trackgen.track[self.distance] == 0:
				self.tilt += 0
				self.linecolor += 1
				self.update()
			if trackgen.track[self.distance] == -1:
				self.tilt -= 1
				self.linecolor += 1
				self.update()
			if trackgen.track[self.distance] == 1:
				self.tilt += 1
				self.linecolor += 1
				self.update()
			if trackgen.track[self.distance] == -2:
				self.tilt -= 0
				self.linecolor += 1
				self.update()
			if trackgen.track[self.distance] == 2:
				self.tilt += 0
				self.linecolor += 1
				self.update()

			if self.distance < len(trackgen.track):
				self.distance += 1
