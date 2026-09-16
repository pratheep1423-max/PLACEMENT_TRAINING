# Problem-17
# Find First Digit

def main():
    n = int(input('Enter a number: '))
    while n >= 10:
        n //= 10
    print(n)

if __name__ == "__main__":
    main()
