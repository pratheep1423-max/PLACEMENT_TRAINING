# Problem-34
# Print Odd Numbers from 1 to N

def main():
    n = int(input('Enter N: '))
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)

if __name__ == "__main__":
    main()
