# Problem-10
# Check Perfect Number

def main():
    n = int(input('Enter a number: '))
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    print('Perfect Number' if sum_div == n else 'Not a Perfect Number')

if __name__ == "__main__":
    main()
