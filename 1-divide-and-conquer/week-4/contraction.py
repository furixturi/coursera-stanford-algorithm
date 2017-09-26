# -*- encoding: utf-8 -*-

import sys
import random
import math

def contraction(graph):
	while(len(graph) > 2):
		u = random.choice(graph)
		uIdx = u[0]
		vIdx = random.choice(u[1:])
		#print "u: ", u, " uIdx: ", uIdx, " vIdx: ", vIdx
		v = None

		for i in range(0, len(graph)):
			if graph[i][0] == vIdx:
				v = graph.pop(i)
				break

		if v is not None:
			#print "v: ", v
			newU = []
			for line in graph:
				if line[0] == uIdx: # first line (u line)
					for edgeUIndex in line:
						if edgeUIndex != vIdx:
							newU.append(edgeUIndex)
					for edgeVIndex in v:
						if edgeVIndex != uIdx and edgeVIndex != vIdx:
							newU.append(edgeVIndex)
					graph[0] = newU
				else: # other lines
					for j in range(1, len(line)):
						if line[j] == vIdx:
							line[j] = uIdx
					for edgeVIndex in v:
						if edgeVIndex == j:
							line.append(uIdx)
		#print "after merge ", uIdx, " and ", vIdx, ":"
		#print graph
	#print "final u degree: ", len(graph[0])
	#print "final v degree: ", len(graph[1])			
	return len(graph[0])-1


minCut = sys.maxint


for i in range(0, 100):
	g = []
	file = open(sys.argv[1], 'r')
	for line in file:
		g.append(line.split())
	#print "g: ", g
	r = contraction(g)
	print "new result: ", r	
	if(r < minCut):
		minCut = r


print "min cut: ", minCut