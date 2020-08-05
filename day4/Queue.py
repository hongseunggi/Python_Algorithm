from typing import Any
from enum import Enum


class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, value: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty

        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty

        return self.que[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx

        return -1

    def count(self, value: Any) -> bool:
        count = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                count += 1

        return count

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비어있습니다')

        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end='')
            print()


Menu = Enum('Meun', 'Enqueue Dequeue Peek Search Dump Exit')

if __name__ == "__main__":
    def select_menu() -> Menu:
        s = [f'({m.value}){m.name}' for m in Menu]
        while True:
            print(*s, sep='    ', end='')
            n = int(input(': '))
            if 1 <= n <= len(Menu):
                return Menu(n)

q = FixedQueue(64)
while True:
    print(f'현재 큐 데이터 {len(q)}/{q.capacity}')
    menu = select_menu()

    if menu == Menu.Enqueue:
        x = int(input('넣을 값 입력 : '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 Full 입니다')

    elif menu == Menu.Dequeue:
        try:
            x = q.deque()
            print(f'빼낸 값은 {x}입니다')

        except FixedQueue.Empty:
            print('큐가 비어 있습니다.')

    elif menu == Menu.Peek:
        try:
            x = q.peek()
            print(f'맨 앞 값은 {x} 입니다')
        except FixedQueue.Empty:
            print('큐가 비어 있습니다.')

    elif menu == Menu.Search:
        x = int(input('검색할 값 입력 : '))
        if x in q:
            print(f'{q.count(x)}개가 큐에 존재하며, 맨 앞 위치는 {q.find(x)}입니다.')

        else:
            print('찾는 값이 없습니다')

    elif menu == Menu.Dump:
        q.dump()

    else:
        break
