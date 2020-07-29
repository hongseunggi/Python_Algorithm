import random
from typing import MutableSequence, Any

def Reverse_Array(vector : MutableSequence) -> None:
    n = len(vector)
    for i in range(n//2):
        vector[i], vector[n-i-1] = vector[n-i-1], vector[i]

vector = []
for _ in range(10):
    vector.append(random.randint(1,99))

print(vector)
Reverse_Array(vector)
print(vector)