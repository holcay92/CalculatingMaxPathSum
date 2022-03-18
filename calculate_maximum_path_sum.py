https://dpaste.com/BRF4S6K5H
def max_of(number1: int, number2: int):
    if number1 < number2: return number2
    else: return number1


def is_prime(number):
    if number == 1 or number == 0 or number == -1: return False
    if number == 2: return True
    if number == 4 or number == -4: return False
    is_prime_number = True
    for i in range(2, int(number / 2)):
        if number % i == 0: is_prime_number = False
    return is_prime_number


def recursive_sum(pyramid, i, j, row):
    if i == row:
        return 0
    else:
        return pyramid[i][j] + max_of(recursive_sum(pyramid, i+1, j, row), recursive_sum(pyramid, i+1, j+1, row))


def main():
    with open('input.txt', 'r') as file:
        twoDlist = [[int(x) for x in line.split()] for line in file]

    # number of rows
    row = len(twoDlist)
    maxSum = 0

    # removing prime numbers by making them infinity
    for i in range(0, row):
        for j in range(0, i+1):
            if twoDlist[i][j] != None and is_prime(twoDlist[i][j]): twoDlist[i][j] = float('-inf')

    # checking if the starting number prime or not
    if twoDlist[0][0] == float('-inf'): return print("There is no path")
    # calling recursive function
    maxSum = recursive_sum(twoDlist, 0, 0, row)
    print(maxSum)


if __name__ == "__main__":
    main()
