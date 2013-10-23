#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from ffnet import ffnet, mlgraph
from numpy import *
from matplotlib.pyplot import *

def main():
	conec = mlgraph((1, 4 ,1))
	net = ffnet(conec)
	
	patterns = 16
	input = [[ k * 2 * pi / patterns] for k in xrange(patterns + 1)]
	target = [[sin(x[0])] for x in input]
	
	print "training"
	net.train_genetic(input, target, individuals=20, generations=500)
	print "simple trainig"
	net.train_tnc(input, target, maxfun = 5000, messages = 1)
	
	print "test"
	output, regression = net.test(input, target, iprint = 2)
	
	# draw it
	points = 128
	xaxis = [[ k * 2 * pi / patterns] for k in xrange(patterns + 1)]
	sine = [sin(x) for x in xaxis]
	cosine = [cos(x) for x in xaxis]
	netsine = [net([x])[0] for x in xaxis]
	netcosine = [net.derivative([x])[0][0] for x in xaxis]
	
	subplot(211)
	plot(xaxis, sine, 'b--', xaxis, netsine, 'k-')
	legend(('sine', 'network output'))
	grid(True)
	title('Outputs of trained network.')

	subplot(212)
	plot(xaxis, cosine, 'b--', xaxis, netcosine, 'k-')
	legend(('cosine', 'network derivative'))
	grid(True)
	show()
	
	return 0

if __name__ == '__main__':
	main()

