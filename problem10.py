#!/usr/bin/env python3
import math

class erastophanes:
	def __init__(self,ceiling):
		self.plist                 = []
		self.pmap                  = [True] * ceiling
		self.pmap[0], self.pmap[1] = False, False
		self.floor                 = 0
		for i in self.sieve(ceiling):
			self.plist.append(i)
		self.floor = ceiling
	def sieve(self,ceiling):
		for i, j in enumerate(self.pmap,start=self.floor):
			if j:
				yield i
				for k in range(i*i,ceiling,i):
					self.pmap[k] = False
	def expand(self,ceiling):
		self.pmap = [True] * (ceiling-self.floor)
		for i in self.plist:
			if i * i < ceiling:
				j = int(math.ceil(self.floor/i))
				while i * j < ceiling:
					try:
						self.pmap[(i*j)-self.floor] = False
					except:
						pass
					j = j + 1
		for i, j in enumerate(self.pmap,start=self.floor):
			print(i,j)
	
if __name__ == '__main__':
	test = erastophanes(100)
	test.expand(110)
