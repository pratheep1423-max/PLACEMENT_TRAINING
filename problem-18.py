# Problem-18
# Count Number of Digits

def main():
    n = int(input('Enter a number: '))
    count = 0
    if n == 0:
        count = 1
    while n != 0:
        count += 1
        n //= 10
    print(count)

if __name__ == "__main__":
    main()
