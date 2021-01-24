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
            


a = []
s = InsertionSort()

i = 0
random.seed()
start = timeit.default_timer()
while i < 100000:
    a.append(random.randint(1, 1000000))
    i += 1 
end = timeit.default_timer()
# 
# s.insertionSort(a)
# 
print(end - start, "Seconds")
