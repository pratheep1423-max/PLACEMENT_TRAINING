# Problem-37
# Sum of Odd Numbers up to N

def main():
    n = int(input('Enter N: '))
    print(sum(i for i in range(1, n + 1, 2)))

if __name__ == "__main__":
    main()
