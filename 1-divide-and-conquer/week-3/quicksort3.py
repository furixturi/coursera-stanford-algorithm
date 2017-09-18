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

def choosePivot(A, l, r):
    pi = l
    fi = l
    mi = (r-1+l)/2
    la = r-1

    first = A[fi]
    middle = A[mi]
    last = A[la]

    if (first > middle):
        if (last > first): #last > first > middle
            pi = fi
        elif (middle > last): #first > middle > last
            pi = mi
        else: #first > last > middle
            pi = la
    else: #first <= middle
        if (last < first): #last < first < middle
            pi = fi
        elif (middle < last): #first < middle < last
            pi = mi
        else: #first < last < middle
            pi = la

    A[l], A[pi] = A[pi], A[l]

def quicksort(A, l, r):    
    if (l < r):
        global count
        count = count + r - l - 1

        choosePivot(A, l, r)

        q = partition(A, l, r)
        quicksort(A, l, q)
        quicksort(A, q + 1, r)        


numbers = []
file = open(sys.argv[1], 'r')
for line in file:
    numbers.append(int(line))
    
quicksort(numbers, 0, len(numbers))
print "count", str(count)
