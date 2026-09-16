# Problem-11
# Check Armstrong Number

def main():
    n = int(input('Enter a number: '))
    original = n
    sum_val = 0
    while n > 0:
        digit = n % 10
        sum_val += digit ** 3
        n //= 10
    print('Armstrong Number' if sum_val == original else 'Not an Armstrong Number')

if __name__ == "__main__":
    main()
