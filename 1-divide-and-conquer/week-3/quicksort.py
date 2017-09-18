# -*- encoding: utf-8 -*-

import sys

count = 0

def partition(A, l, r):
    
    p = A[l]
    i = l + 1
    
    for j in range(l + 1, r):
        if (A[j] < p):
            A[i], A[j] = A[j], A[i]
            i = i + 1        
        
    A[l], A[i-1] = A[i-1], A[l]

    return i-1

def quicksort(A, l, r):    
    if (l < r):
        global count
        count = count + r - l - 1

        q = partition(A, l, r)
        quicksort(A, l, q)
        quicksort(A, q + 1, r)        
    return A


numbers = []
file = open(sys.argv[1], 'r')
for line in file:
    numbers.append(int(line))
    
quicksort(numbers, 0, len(numbers))
print count
