import numpy as np
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

arr_rg = gen(pcg())
normal = arr_rg.normal(size=(4,4))
# print(normal)

integers = arr_rg.integers(low=1, high=10, size=(4,4))
# print(integers)

random = arr_rg.random(size=(4,4))
print(random)