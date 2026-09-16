# Problem-19
# Sum of Digits

def main():
    n = int(input('Enter a number: '))
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    print(sum_digits)

if __name__ == "__main__":
    main()
