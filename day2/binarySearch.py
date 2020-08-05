from MySort import MySort
from typing import Any, Sequence
import random

def binary_search(a: Sequence, Key: Any) -> int:
    first = 0
    last = len(a)-1
    while True:
        try1 = (first+last)//2
        if a[try1] == Key:
            return try1
        elif a[try1] < Key:
            first = try1+1
        else:
            last = try1-1
        if first > last:
            break
    return -1

if __name__ == "__main__":
    x = []
    for _ in range(10):
        x.append(random.randint(1,99))

    print(x)
    x = MySort.MySort(x)
    print(x)
    while True:
        key = random.randint(1,99)
        print(key)
        index = binary_search(x,key)
        if index == -1:
            print("찾기 실패")
        else :
            print(f'찾는 값 {key}는 x[{index}]에 있습니다')
            break
