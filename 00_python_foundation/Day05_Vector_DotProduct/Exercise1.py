#Viết hàm:

def dot_product(a, b):
    arr_dot = []
    for i in range(len(a)):
        arr_dot.append(a[i]*b[i])
    return arr_dot


arr1 = [2, 3, 4]
arr2 = [0.2, 0.5, 0.3]

print(dot_product(arr1, arr2))
