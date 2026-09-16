# Problem-27
# Find Smallest Digit

def main():
    n = int(input('Enter a number: '))
    min_digit = 9
    while n > 0:
        digit = n % 10
        if digit < min_digit:
            min_digit = digit
        n //= 10
    print(min_digit)

if __name__ == "__main__":
    main()
