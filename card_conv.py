import random

def card_conv(x : int , r : int) -> str:
    answer = ''
    ch = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        answer += ch[x%r]
        x //= r

    return answer[::-1]

num = random.randint(1,99)

print(f'{num} 2진수 = {card_conv(num, 2)} ')
print(f'{num} 8진수 = {card_conv(num, 8)} ')
print(f'{num} 10진수 = {card_conv(num, 10)} ')
print(f'{num} 16진수 = {card_conv(num, 16)} ')