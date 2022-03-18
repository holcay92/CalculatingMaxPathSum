import math
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


def recursive_sum(tri, i, j):

    if i == len(tri):
        return 0
    else:
        # print("max of the line:", max_of(recursive_sum(tri, i+1, j),
        #   recursive_sum(tri, i+1, j+1)), "recursive_sum(tri, i+1, j): ", recursive_sum(tri, i+1, j),
        #  "recursive_sum(tri, i+1, j+1): ", recursive_sum(tri, i+1, j+1))
        return tri[i][j] + max_of(recursive_sum(tri, i+1, j), recursive_sum(tri, i+1, j+1))


# 1
# 8 4
# 2 6 9
# 8 7 2 4


def main():
    with open('input.txt', 'r') as file:
        twoDlist = [[int(x) for x in line.split()] for line in file]

    # number of rows
    row = col = len(twoDlist)
    maxSum = 0
# filling array with zeros
#     iterColumn = 1
#     for item1 in range(0, row):
#         for item2 in range(0, row-iterColumn):
#             twoDlist[item1].append(int(0))
#         iterColumn = iterColumn + 1

#removing prime numbers
    for i in range(0, row):
        for j in range(0, i+1):
            if twoDlist[i][j] != None and is_prime(twoDlist[i][j]): twoDlist[i][j] = float('-inf')

    print(twoDlist)
# calling recursive function
    if twoDlist[0][0] == float('-inf'): return print("There is no path")
    maxSum = recursive_sum(twoDlist, 0, 0)
    print("maxSum: ", maxSum)


if __name__ == "__main__":
    main()