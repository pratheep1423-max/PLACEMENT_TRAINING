# Problem-15
# Check Neon Number

def main():
    n = int(input('Enter a number: '))
    square = n * n
    sum_digits = sum(int(d) for d in str(square))
    print('Neon Number' if sum_digits == n else 'Not a Neon Number')

if __name__ == "__main__":
    main()
