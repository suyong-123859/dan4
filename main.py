dan = int(input("단을 입력하세요: "))
limit = int(input("어디까지 출력할까요?: "))
for i in range(1, limit + 1):
    print(f"{dan} * {i} = {dan * i}")
