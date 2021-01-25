import math
from merge import ArrayMerge
import typing

class Mergesort:
    def __init__(self, A) -> None:
        self.array = A
    def mergesSort(self, p, r):
        if p < r:
            q = math.floor((p + r)/2)
            self.mergesSort(p, q)
            self.mergesSort(q + 1, r)
            ArrayMerge.merge(self.array, p, q, r)

a = Mergesort([9,8,7,6,5,4,3,2,1])
a.mergesSort(0, 8)
print(a.array)