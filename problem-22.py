# Problem-22
# Count Even Digits

def main():
    n = int(input('Enter a number: '))
    count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n //= 10
    print(count)

if __name__ == "__main__":
    main()
