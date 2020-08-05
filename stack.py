from typing import Any
from enum import Enum


class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> bool:
        count = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                count += 1

        return count

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> None:
        if self.is_empty():
            print("스택이 비어있습니다")
        else:
            print(self.stk[:self.ptr])

Menu = Enum('Menu', 'Push Pop Peek Search Dump Exit')
if __name__ == "__main__":

 def select_menu() -> Menu:
        s = [f'({m.value}){m.name}' for m in Menu]
        while True:
            print(*s, sep='  ', end='')
            n = int(input(': '))
            if 1 <= n <= len(Menu):
                return Menu(n)

s = FixedStack(64)
while True:
    print(f'현재 데이터 수 : {len(s)}/{s.capacity}')
    menu = select_menu()
    if menu == Menu.Push:
        x = int(input('데이터 입력 : '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')

    elif menu == Menu.Pop:
        try:
            x = s.pop()
            print(f'꺼낸 데이터는 {x}')
        except FixedStack.Empty:
            print('스택이 비어있습니다.')

    elif menu == Menu.Peek:
        try:
            x = s.peek()
            print(f'피크 데이터는 {x}')
        except FixedStack.Empty:
            print('스택이 비어있습니다.')

    elif menu == Menu.Search:
        x = int(input('검색할 값을 입력 하시오 : '))
        if x in s:
            print(f'{s.count(x)}개가 스택에 존재하며 , 맨 처음 위치는 {s.find(x)}입니다')
        else:
            print('검색할 값이 없습니다.')

    elif menu == Menu.Dump:
        s.dump()

    else:
        break