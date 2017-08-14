# -*- encoding: utf-8 -*-
# i = 0

def karatsuba(x, y):
	global i
	i = i + 1

	# print "=========================Enter karatsuba=========================="
	# print "x: ", x, ", y: ", y

	if (x < 10 or y < 10):
		# print "x < 10 or y < 10, return x * y: %i" % (x*y)
		# print "======================= Exit karatsuba 1 ========================"
		return x * y

	else:

		n = max(len(str(x)), len(str(y)))

		# if odd digits, pad it with a 0
		# e.g. 123 should be devided like 0123
		if n % 2 != 0:
			n = n + 1
		n2 = n/2

		# print "!!!!split!!!!"
		# print " n: ", n, ", n/2: ", n2

		a = x / (10**n2)
		b = x % (10**n2)
		c = y / (10**n2)
		d = y % (10**n2)
		
		# print "a: ", a, ", b: ", b, ", c: ", c, ", d: ", d
		# print "a+b: %i, c+d: %i" % ((a+b), (c+d))

		# print "*********recursion*********"
		# print "recursion a, c"
		ac = karatsuba(a, c)
		# print "recursion b, d"
		bd = karatsuba(b, d)
		# print "recursion (a+b), (c+d)"
		a_bc_d = karatsuba((a+b), (c+d))
		# print "######## recursion ended ######"

		# print "ac: ", ac, ", bd: ", bd, ", (a+b) * (c+d) [a_bc_d]: ", a_bc_d

		ad_bc = a_bc_d - bd - ac
		
		# print "ad + bc(=(a+b)*(c+d)-ac-bd)[ad_bc]: ", ad_bc

		r = 10 ** n * ac + 10 ** n2 * (a_bc_d - bd - ac) + bd
		# print "10^n * ac + 10^(n/2) * ((a+b)*(c+d) - bd - ac) + bd: ", r
		# print "======================== Exit karatsuba 2 ========================"
		return r


x = input("First integer: ")
y = input("Second integer: ")

print karatsuba(x, y)
# print i