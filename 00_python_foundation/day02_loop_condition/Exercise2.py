# Tìm số xuất hiện nhiều nhất
arr = [1, 2, 2, 3, 3, 3, 4]
exist = True
arr_set = []
arr_count = []

for i in range(len(arr)):
    for j in range(len(arr_set)):
        if arr[i] == arr_set[j]:
            exist = False
            arr_count[j] = arr_count[j] + 1
        else:
            exist = True
            
    if exist:
        arr_set.append(arr[i])
        arr_count.append(1)
    
print(arr_set)
print(arr_count)

max = 0
for i in range(len(arr_count)):
  if arr_count[i] > max:
    max = arr_count[i]

print(max)