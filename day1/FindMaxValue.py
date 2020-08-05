import random
from typing import Sequence, Any

def Max_of(list : Sequence) -> Any:
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max :
            max = list[i]
    return max

vector = []
for _ in range(10):
    vector.append(random.randint(1,99))

print(vector)
Max = Max_of(vector)
print(Max)
