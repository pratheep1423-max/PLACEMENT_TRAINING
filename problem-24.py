# Problem-24
# Sum of Even Digits

def main():
    n = int(input('Enter a number: '))
    sum_even = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            sum_even += digit
        n //= 10
    print(sum_even)

if __name__ == "__main__":
    main()
