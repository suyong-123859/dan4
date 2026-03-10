s_dan = int(input("시작 단: "))
e_dan = int(input("끝 단: "))
s_mul = int(input("시작 곱: "))
e_mul = int(input("끝 곱: "))

for d in range(s_dan, e_dan + 1):
    for m in range(s_mul, e_mul + 1):
        print(f"{d} * {m} = {d * m}")
    print()
