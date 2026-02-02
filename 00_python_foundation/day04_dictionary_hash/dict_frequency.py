arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
freq = {}

for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]] += 1
    else:
        freq[arr[i]] = 1
    
print(freq)