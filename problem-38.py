# Problem-38
# Factorial of N

def main():
    n = int(input('Enter N: '))
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)

if __name__ == "__main__":
    main()
