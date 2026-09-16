# Problem-28
# Count Occurrence of a Digit

def main():
    n = int(input('Enter a number: '))
    d = int(input('Enter digit to search: '))
    count = 0
    while n > 0:
        if n % 10 == d:
            count += 1
        n //= 10
    print(count)

if __name__ == "__main__":
    main()
