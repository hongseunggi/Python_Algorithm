"""Normal Calculation"""
counter = 0
ptr = 0
prime = []
prime.append(2)
ptr += 1
prime.append(3)
ptr += 1
for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i ==0:
            break
        #else :
         #  print(n)
print(f'counter = {counter}')
"""First Optimization Normal Calculation"""
counter = 0
prime = []
ptr = 0
prime.append(2)
ptr+=1
for n in range(3, 1001, 2):
    for i in range(1, ptr):
        counter+=1
        if n % prime[i] == 0:
            break

    else:
        prime.append(n)
        ptr += 1
#for i in range(ptr):
 #   print(prime[i])
print(f'Optimization counter1 = {counter}')
"""Second Optimize Optimization improve First Optimization"""
counter = 0
ptr = 0
prime = []
prime.append(2)
ptr += 1
prime.append(3)
ptr += 1
for n in range(5, 1001, 2):
    i = 1
    while prime[i]*prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i+=1
    else :
        prime.append(n)
        ptr += 1
        counter += 1
#for i in range(ptr):
 #   print(prime[i])
print(f'Final Optimization counter = {counter}')