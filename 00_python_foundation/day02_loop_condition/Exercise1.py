# Đếm số chẵn trong mảng

arr = [1, 2, 3, 4, 6, 9]
count = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count += 1

print(count)