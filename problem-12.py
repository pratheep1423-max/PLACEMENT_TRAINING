# Problem-12
# Check Palindrome Number

def main():
    n = int(input('Enter a number: '))
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    print('Palindrome' if rev == original else 'Not a palindrome')

if __name__ == "__main__":
    main()
