#Bài toán: Đảo ngược mảng (❌ không dùng reverse())

arr = [1, 2, 3, 4, 5]

n = len(arr)
i = 0
j = n-1


while i < n/2:
  print(i)
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
  i += 1
  j -= 1

print(arr)