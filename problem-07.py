# Problem-07
# Check Divisibility by 5 and 11

def main():
    num = int(input('Enter a number: '))
    if num % 5 == 0 and num % 11 == 0:
        print('Divisible by 5 and 11')
    else:
        print('Not divisible by 5 and 11')

if __name__ == "__main__":
    main()
