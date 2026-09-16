# Problem-13
# Check Strong Number

def main():
    n = int(input('Enter a number: '))
    original = n
    sum_fact = 0
    while n > 0:
        digit = n % 10
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        sum_fact += fact
        n //= 10
    print('Strong Number' if sum_fact == original else 'Not a Strong Number')

if __name__ == "__main__":
    main()
