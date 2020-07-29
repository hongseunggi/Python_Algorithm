import random
from typing import Any, MutableSequence

def Reverse_Sort(list : MutableSequence) -> Any:
    for i in range(len(list)):
        if i + 1 == len(list):
            break
        if list[i] < list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            Reverse_Sort(list)
    return list

list = []
for _ in range(10):
    list.append(random.randint(1,99))
print(list)
list = Reverse_Sort(list)
print(list)