#Bài toán: Đếm số chữ cái trong chuỗi (❌ dùng count)


text = "ai product engineer"
count = 0
for i in range(len(text)):
    if text[i] != " ":
        count = count + 1

print(count)