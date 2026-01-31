# Kiểm tra chuỗi có phải palindrome

# "level" → True
# "hello" → False

text = "aaaaaa"
check = True
for i in range(len(text)//2):
  n = len(text)
  if text[i] != text[n-1-i]:
    check = False
  i += 1

print(check)