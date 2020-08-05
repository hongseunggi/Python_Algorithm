from typing import Any, Sequence
import copy

def Search_sentinel(a: Sequence, key: Any) -> int:
    index = copy.deepcopy(a)
    index.append(key)

    i = 0
    while True:
        if index[i] == key:
            break
        i += 1
    return -1 if i == len(a) else i

if __name__ == "__main__":
    num = int(input('원소 수를 입력 : '))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    key = int(input('검색할 값 :'))

    index = Search_sentinel(x, key)
    if index == -1 :
        print("검색 실패")
    else :
        print(f'검색한 {key}는 x[{index}]에 있습니다')
