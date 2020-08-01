import random
from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1


if __name__ == "__main__":
    index = []
    for _ in range(10):
        index.append(random.randint(1,99))

    s = index[random.randint(0,9)]
    result = seq_search(index, s)
    print(index)
    print(f'검색한 값 = {s}, 해당 값은 index[{result}]에 있습니다')