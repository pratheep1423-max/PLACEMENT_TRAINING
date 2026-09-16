# Problem-36
# Sum of Even Numbers up to N

def main():
    n = int(input('Enter N: '))
    print(sum(i for i in range(2, n + 1, 2)))

if __name__ == "__main__":
    main()
