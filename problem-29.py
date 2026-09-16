# Problem-29
# Check Whether Number Contains 0

def main():
    n = int(input('Enter a number: '))
    contains_zero = '0' in str(n)
    print('Contains 0' if contains_zero else 'Does not contain 0')

if __name__ == "__main__":
    main()
