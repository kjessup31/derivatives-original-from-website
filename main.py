import math
import sympy
from sympy import *
x = Symbol('x') 
#what will get derived
f = 2*x**2+3
#the f in f.diff(x) is from first equation
f_prime = f.diff(x)
print(f_prime)
f = lambdify(x,f)
f_prime = lambdify(x,f_prime)
a = f(3)
print(a)
b = f_prime(3)
print(b)