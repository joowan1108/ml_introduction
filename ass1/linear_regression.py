import math
import numpy as np
from numpy.polynomial import Polynomial
import sympy as sp

w_1 = sp.Symbol('w_1')
w_0 = sp.Symbol('w_0')

'''
(w_1 x + w_0 - t)^2의 거리가 모든 sample에서 최소인 w_1와 w_0 구하야 함
'''

f = Polynomial([w_0, w_1])

samples = [(-1, 1), (0, 1), (1, 1), (1, 0)]

def loss_function(samples):
    polynomials = []
    for sample in samples:
        num = sample[0]
        y = sample[1]
        fu = (y-f(num))**2
        polynomials.append(sp.expand(fu))
    result = Polynomial([0])
    for poly in polynomials:
        result = result + poly
    print(result)

loss_function(samples)






