# -*- encoding: utf-8 -*-
import sys

def countInv(nums):
	if (len(nums) == 1):
		return 0

	else:
		n2 = len(nums)/2
		left = nums[:n2]
		right = nums[n2:]
		
		x = countInv(left)
		y = countInv(right)
		z = countSplitInv(left, right)

	# print "countInv: ", nums, ", x: ", x, ", y: ", y, " ,z: ", z

	return x+y+z
	

def countSplitInv(left, right):
	left.sort()
	right.sort()
	i = 0
	j = 0
	k = 0
	z = 0
	while (i < len(left) and j < len(right)):
		if (left[i] < right[j]):
			i += 1
		else:
			j += 1
			z += len(left) - i
	return z


numbers = []
file = open(sys.argv[1], 'r')
for line in file:
	numbers.append(int(line))

# print numbers
print countInv(numbers)


