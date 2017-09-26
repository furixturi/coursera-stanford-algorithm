# -*- encoding: utf-8 -*-

import sys
import random

def getVs(graph):
	vs = []
	for line in graph:
		vs.append(line[0])
	return vs

def getEs(graph):
	es = []
	for line in graph:
		u = line[0]
		for i in range(1, len(line)):
			es.append([u, line[i]])
	return es

def contract(v, e):
	#print "==========contract============"
	vs = list(v)
	es = list(e)
	while len(vs) > 2:
		#print "vertices before: ", vs
		#print "edges before: ", es

		e_to_remove = random.choice(es)
		v_keep = e_to_remove[0]
		v_delete = e_to_remove[1]

		#print "e_to_remove: ", e_to_remove
		#print "v_keep: ", v_keep
		#print "v_delete: ", v_delete

		vs.remove(v_delete)
		
		newEs = []
		
		for edge in es:

			v_from = edge[0]
			v_to = edge[1]

			if (v_from == v_keep and v_to == v_delete) or (v_from == v_delete and v_to == v_keep):
				continue

			if v_from == v_delete:
				v_from = v_keep

			if v_to == v_delete:
				v_to = v_keep

			newEs.append([v_from, v_to])

		es = newEs

	return len(es)/2

		

g = []
file = open(sys.argv[1], 'r')
for line in file:
	g.append(line.split())

v = getVs(g)
e = getEs(g)
print "g: ", g
print "v: ", v
print "e: ", e

minCut = sys.maxint
for i in range(0, 100):
	r = contract(v,e)
	print "new result: ", r	
	if(r < minCut):
		minCut = r


print "min cut: ", minCut