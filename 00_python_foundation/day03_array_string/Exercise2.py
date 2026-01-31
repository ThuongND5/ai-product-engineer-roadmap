# Kiểm tra 2 chuỗi có cùng pattern

# start → tarts ✅
# start → tastr ❌

text1 = "start"
text2 = "statr"

check = True
for i in range(len(text1)):
  if len(text1) != len(text2):
    check = False
  if text1[i] != text2[i]:
    check = False

print(check)

