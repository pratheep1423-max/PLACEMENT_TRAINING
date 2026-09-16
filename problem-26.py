# Problem-26
# Find Largest Digit

def main():
    n = int(input('Enter a number: '))
    max_digit = 0
    while n > 0:
        digit = n % 10
        if digit > max_digit:
            max_digit = digit
        n //= 10
    print(max_digit)

if __name__ == "__main__":
    main()
