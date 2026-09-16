# Problem-40
# Count Multiples of 3 from 1 to N

def main():
    n = int(input('Enter N: '))
    count = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
