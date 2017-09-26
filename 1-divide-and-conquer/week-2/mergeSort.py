# -*- encoding: utf-8 -*-

import sys

def mergeSort(numbers):
	if len(numbers) == 0 or len(numbers) == 1:
		return numbers
	else:
		mid = len(numbers) // 2
		left = mergeSort(numbers[:mid])
		right = mergeSort(numbers[mid:])
		print "left: ", left
		print "right: ", right
		
		merged = merge(left, right)
		print "merged: ", merged

		return merged


def merge(left, right):
	merged = []
	while len(left) != 0 and len(right) != 0:
		if left[0] < right[0]:
			merged.append(left[0])
			left.remove(left[0])
		else:
			merged.append(right[0])
			right.remove(right[0])
	if len(left) == 0:
		merged += right
	else:
		merged += left
	return merged


num = []
file = open(sys.argv[1], 'r')
for line in file:
	num.append(int(line))

print mergeSort(num)