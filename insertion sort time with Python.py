import time
from random import randint

#삽입 정렬
#array = []
#for _ in range(1000):
#    array.append(randint(1, 100))

#최악
array_b = []

for i in range(1000, 1, -1):
    array_b.append(i)

start_time = time.time()

for i in range(1, len(array_b)):
    j = i - 1
    key = array_b[i]
    while array_b[j] > key and j >= 0:
        array_b[j + 1] = array_b[j]
        j = j - 1
    array_b[j + 1] = key

end_time = time.time()
print("삽입 정렬 최악 성능 측정:", end_time - start_time)


#최선
array = []

for i in range(1, 1000):
    array.append(i)

start_time = time.time()

for i in range(1, len(array)):
    j = i - 1
    key = array[i]
    while array[j] > key and j >= 0:
        array[j + 1] = array[j]
        j = j - 1
    array[j + 1] = key

end_time = time.time()
print("삽입 정렬 최선 성능 측정:", end_time - start_time)
