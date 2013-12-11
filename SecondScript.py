#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from numpy import *
from matplotlib.pyplot import *
from matplotlib.gridspec import *

class MA:
	def __init__(self, n, delta, omega):
		self.n = n
		self.p = len(delta)
		self.delta = delta
		self.q = len(omega)
		self.omega = omega
		
	def generateNoise(self):
		self.xsi = random.normal(size = self.n)	
		return self.xsi
		
	def getSignalAfterFilter(self):
		self.generateNoise()
		return map(lambda x: x[-1] + dot(x[:-1], self.delta), [self.xsi[k-self.p:k+1] for k in xrange(self.p, self.n)])	
		
	def getAutoRegression(self):
		self.generateNoise()
		x = empty(self.n)
		x[:self.q] = self.omega
		for i in xrange(self.q, self.n):
			x[i] = self.xsi[i] + dot(self.omega, x[i-self.q:i])
		return x	
			
			

class FurieMean:
	def __init__(self, signal, windowCount, dt):
		self.signal = signal
		self.windowLen = len(signal) / windowCount
		self.windowCount = windowCount
		self.dt = dt
		
	def getFurieModule(self, currentSignal):
		furie = fft.rfft(currentSignal)
		s = abs(furie)/(.5 * (self.windowLen/self.dt))
		freq = linspace(.0, 1./(2*self.dt), s.shape[0])
		return (freq, s)	
		
	def getAverageFurie(self):
		result = []
		for i in range(self.windowCount):
			currentSignal = self.signal[i*self.windowLen:(i+1)*self.windowLen]
			currentFurie = self.getFurieModule(currentSignal)
			result.append(currentFurie[1])
		return (currentFurie[0], mean(require(result), 0))	

			

def main():
	signalLen = 10000;
	ma = MA(signalLen, [0.5, 0.6, .7, .2, .3, .4], [.03, -.02, .07, 0.5, -0.06, 0.1, -0.04, .09, .1, -.03])
	print ma.getAutoRegression()
	fmClearNoise = FurieMean(ma.generateNoise(), 10, 1)
	fmAfterFilter = FurieMean(ma.getSignalAfterFilter(), 10, 1)
	fmAuto = FurieMean(ma.getAutoRegression(), 10, 1)
	gs = GridSpec(3, 1)
	subplot(gs[0, 0])
	xxx = fmClearNoise.getAverageFurie()
	plot(xxx[0], xxx[1])
	subplot(gs[1, 0])
	xxx = fmAfterFilter.getAverageFurie()
	plot(xxx[0], xxx[1])
	subplot(gs[2, 0])
	xxx = fmAuto.getAverageFurie()
	plot(xxx[0], xxx[1])
	show()
	
	return 0

if __name__ == '__main__':
	main()

