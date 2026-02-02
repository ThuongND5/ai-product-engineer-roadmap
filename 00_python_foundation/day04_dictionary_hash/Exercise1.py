# Đề "ai product" → {'a':1,'i':1,'p':1,'r':1,'o':1,'d':1,'u':1,'c':1,'t':1}
text = "ai produccccccccct"
freq = {}

for i in range(len(text)):
    if text[i] in freq:
        freq[text[i]] += 1
    else:
        freq[text[i]] = 1

print(freq)