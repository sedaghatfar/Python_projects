#!/usr/bin/env python

import random
import Image
import os
os.chdir('/home/matthew/Pictures')
heads = Image.open('heads.jpg')
tails = Image.open('tails.jpg')

def CoinFlip(size):
	for x in xrange(size):
		flip = random.randint(0,1)
		if flip == 1:
			heads.show()
		else:
			tails.show()
	return "You really should have used a physical coin"
		

flips = input("How Many Flips?\n")
print CoinFlip(flips)
