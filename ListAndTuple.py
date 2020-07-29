x1 = ['John', 'George', 'Paul', 'Ringo']
x2 = ('John', 'George', 'Paul', 'Ringo')
"""List"""
for i in range(len(x1)):
    print(f'x1[{i}] = {x1[i]}')
print()
for i, name in enumerate(x1):
    print(f'x1[{i}] = {name}')
print()
for i, name in enumerate(x1, 1):
    print(f'{i} 번째 = {name}')
print()
for i in x1:
    print(i)
print()
"""Tuple"""
for i in range(len(x2)):
    print(f'x2[{i}] = {x2[i]}')
print()
for i, name in enumerate(x2):
    print(f'x2[{i}] = {name}')
print()
for i, name in enumerate(x2, 1):
    print(f'{i} 번째 = {name}')
print()
for i in x2:
    print(i)