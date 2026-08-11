def main():
    for i in range(2, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        if i < 9:
            print()

if __name__ == "__main__":
    main()
