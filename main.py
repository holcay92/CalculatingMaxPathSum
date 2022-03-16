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


def recursive_sum(tri, m, n):
    # loop for calculation
    maxSum = tri[0][0]
    for i in range(0, m-1, 1):
        for j in range(i + 1):
            if not is_prime(tri[i + 1][j]):
                tri[i][j] += tri[i + 1][j]
            elif not is_prime(tri[i + 1][j+1]):
                tri[i][j] += tri[i + 1][j+1]
        tempSum = tri[i][j]
        if tempSum > maxSum: maxSum = tempSum

    return maxSum


def main():
    with open('input.txt', 'r') as file:
        twoDlist = [[int(x) for x in line.split()] for line in file]

    # number of rows
    row = col = len(twoDlist)
    maxSum = 0
# filling array with zeros
    iterColumn = 1
    for item1 in range(0, row):
        for item2 in range(0, row-iterColumn):
            twoDlist[item1].append(int(0))
        iterColumn = iterColumn + 1

# calling recursive function
    if is_prime(twoDlist[0][0]): return print("There is no path")
    maxSum = recursive_sum(twoDlist, row-1, col-1)
    print(maxSum)


if __name__ == "__main__":
    main()