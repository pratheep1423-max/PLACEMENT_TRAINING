# Problem-25
# Sum of Odd Digits

def main():
    n = int(input('Enter a number: '))
    sum_odd = 0
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            sum_odd += digit
        n //= 10
    print(sum_odd)

if __name__ == "__main__":
    main()
