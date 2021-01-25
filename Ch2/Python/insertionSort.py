import timeit
import random

class InsertionSort:
    def insertionSort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            i = 1
            while i < len(arr):             ## CAN BE USED WITH :  for i in range(1, len(arr) [EXCLUSIVE]) THEN 'i' IS JUST NUMBERS
                j = i - 1
                key = arr[i]
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
                i += 1
    
    def insertionSortNonDecreasing(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            for i in range(1, len(arr)):
                j = i - 1
                key = arr[i]
                while j >= 0 and key > arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
