#! /usr/bin/env python

#
# two_springs.py
#
"""
This module defines the vector field for a spring-mass system
consisting of two masses and two springs.

The function vectorfield is equivalent to this:

x1' = y1
y1' = (-b1 y1 - k1 (x1 - L1) + k2 (x2 - x1 - L2))/m1
x2' = y2
y2' = (-b2 y2 - k2 (x2 - x1 - L2))/m2

"""

#
# The vector field.
#

def vectorfield(w,t,p):
	"""
	This arguments are shaped such that the function can
	be used as input to odeint.

	Arguments:
		w :  vector of the state variables: 
				w = [x1,y1,x2,y2]
		t :  time
		p :  vector of the parameters: 
				p = [m1,m2,k1,k2,L1,L2,b1,b2]
	"""
	# Are this tuples in python wordings ?
	x1, y1, x2, y2 = w
	m1, m2, k1, k2, L1, L2, b1, b2 = p

	# Create f = (x1',y1',x2',y2'):
	f = [y1, 
		(-b1*y1 - k1*(x1-L1) + k2*(x2-x1-L2))/m1, 
		y2, 
		(-b2*y2 - k2*(x2-x1-L2))]

	return f
