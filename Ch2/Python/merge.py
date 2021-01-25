'''
This file implements the auxiliary Merge Function.
This merge is based on the idea of sentinals where the values are going to be +inf.
Implemented by Lovnesh Bhardwaj
'''
import math

class ArrayMerge:
    @staticmethod
    def merge(A, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        L = [None] * (n1 + 1)
        R = [None] * (n2 + 1)
        for i in range(0, n1):
            L[i] = A[p + i]
        for j in range(0, n2):
            R[j] = A[q + j + 1]
        L[n1] = math.inf
        R[n2] = math.inf
        # We have now made two arrays and with a sentinal value at the end. Now we will merge them
        i = 0
        j = 0
        for k in range(p, r + 1):   # r + 1 because r is the final index of A and r + 1 stops at r
            if L[i] <= R[j]:        #If we fill up all the 'j's' and are at the sentinal, then the resulting A[i] will always be less than the sentinals because the sentinal is infinity.
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

