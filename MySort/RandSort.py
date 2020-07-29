import random

def MySort(vector):
    for i in range(len(vector)):
        if i+1 == len(vector):
            break
        if vector[i] > vector[i+1]:
            vector[i], vector[i+1] = vector[i+1], vector[i]
            MySort(vector)
    return vector
vector = []

for i in range(10):
    vector.append(random.randint(1,99))

vecotr = MySort(vector)

print(vector)