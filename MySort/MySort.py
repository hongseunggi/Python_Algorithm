def MySort(vector):
    for i in range(len(vector)):
        if i+1 == len(vector):
            break
        if vector[i] > vector[i+1]:
            vector[i], vector[i+1] = vector[i+1], vector[i]
            MySort(vector)
    return vector

vector = [3,1,5,6,8,9,4,2,10,20,11]
vecotr = MySort(vector)

print(vector)