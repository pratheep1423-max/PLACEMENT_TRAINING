# Problem-14
# Check Automorphic Number

def main():
    n = int(input('Enter a number: '))
    sq = n * n
    print('Automorphic' if str(sq).endswith(str(n)) else 'Not Automorphic')

if __name__ == "__main__":
    main()
