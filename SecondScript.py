#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from numpy import *
from matplotlib.pyplot import *

class MA:
	def __init__(self, n, delta):
		self.n = n
		self.p = len(delta)
		self.delta = delta
		
	def generateNoise(self):
		self.xsi = random.normal(size = self.n)	
		
	def getSignalAfterFilter(self):
		self.generateNoise()
		return map(lambda x: x[-1] + dot(x[:-1], self.delta), [self.xsi[k-self.p:k+1] for k in xrange(self.p, self.n)])	

class FurieMean:
	def __init__(self, signal, windowLen, dt):
		self.siganl = siganl
		self.windowLen = windowLen
		seld.dt = dt
		
	def getAverageFurie(self):
		furie = fft.rfft(signal)
		s = abs(furie)/(.5 * (self.windowLen/self.dt))
		freq = arange(.0, 1./(2*self.dt), 1./self.windowLen)
		return (freq, s[:-1])	

def main():
	
	ma = MA(100, [0.5, 0.6, .7, .2, .3, .4])
	print ma.getSignalAfterFilter()
	
	return 0

if __name__ == '__main__':
	main()

