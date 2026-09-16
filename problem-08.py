# Problem-08
# Check Leap Year

def main():
    year = int(input('Enter a year: '))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print('Leap year')
    else:
        print('Not a leap year')

if __name__ == "__main__":
    main()
