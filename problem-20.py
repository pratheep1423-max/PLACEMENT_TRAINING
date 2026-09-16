# Problem-20
# Product of Digits

def main():
    n = int(input('Enter a number: '))
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    print(product)

if __name__ == "__main__":
    main()
