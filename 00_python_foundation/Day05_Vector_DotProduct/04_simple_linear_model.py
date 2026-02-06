features = [8, 7, 9]
weights = [0.4, 0.3, 0.3]
bias = 1

score = 0

for i in range(len(features)):
    score += features[i] * weights[i]

score += bias

print("Score:", score)

if score >= 7:
    print("PASS")
else:
    print("FAIL")
