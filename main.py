s = int(input("시작 단: "))
e = int(input("끝 단: "))
for i in range(s, e + 1):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()
