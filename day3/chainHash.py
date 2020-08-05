from __future__ import annotations
from typing import Any, Sequence
import hashlib


class Node:

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainHash:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'   -> {p.key}({p.value})', end='')
                p = p.next
            print()


if __name__ == "__main__":
    hash = ChainHash(13)
    for _ in range(10):
        key = int(input('추가할 키 입력 : '))
        val = input('추가할 값 입력 : ')
        if not hash.add(key, val):
            print('추가 실패')

    for _ in range(5):
        key = int(input('검색할 키 입력'))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색 결과 없습니다.')
    hash.dump()
