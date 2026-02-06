# 1️⃣ Có 3 học sinh
# 2️⃣ Mỗi học sinh được biểu diễn bằng 1 vector đặc trưng:
# [gio_hoc, bai_tap, diem_thu]
# 3️⃣ Trọng số cố định cho AI:
# weights = [0.4, 0.3, 0.3]
# bias = 1
# 4️⃣ Cách tính điểm:
# score = dot(student, weights) + bias
# 5️⃣ Luật:
# Nếu score >= 7 → PASS
# Ngược lại → FAIL

duong = [4, 3, 8.5]
thuong = [5, 5, 6.5]
phong = [4, 6, 7.7]


def dot_product(hocsinh):
    weights = [0.4, 0.3, 0.3]
    bias = 1
    score = 0
    for i in range(len(hocsinh)):
        score += hocsinh[i]*weights[i]

    score += bias
    status = False
    if score >= 7:
        status = True

    return hocsinh, status

students = [duong, thuong, phong]
for i in range(len(students)):
    print(dot_product(students[i]))


        