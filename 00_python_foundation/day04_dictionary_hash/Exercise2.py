text1 = "paper"
text2 = "title"
check = True
dict = {}

if len(text1) != len(text2):
    check = False
else:
    for i in range(len(text1)):
        if text1[i] in dict and dict[text1[i]] != text2[i]:
            check = False
        else:
            dict[text1[i]] = text2[i]

print(dict, check)
