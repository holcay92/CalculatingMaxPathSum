# number = int(input("enter number"))
# print(int(number / 2))
#
#
# def is_prime(number):
#     if number == 1 or number == 0 or number == -1: return False
#     if number == 2: return True
#     if number == 4: return False
#     is_prime_number = True
#     for i in range(2, int(number / 2)):
#         if number % i == 0: is_prime_number = False
#     return is_prime_number
#
#
# result = is_prime(number)
# print(result)
N = 3


# Function for finding maximum sum
def maxPathSum(tri, m, n):
    # loop for bottom-up calculation
    for i in range(m - 1, -1, -1):
        for j in range(i + 1):

            # for each element, check both
            # elements just below the number
            # and below right to the number
            # add the maximum of them to it
            if tri[i + 1][j] > tri[i + 1][j + 1]:
                tri[i][j] += tri[i + 1][j]
            else:
                tri[i][j] += tri[i + 1][j + 1]

    # return the top element
    # which stores the maximum sum
    return tri[0][0]


# Driver program to test above function

tri = [[1],
       [4, 8],
       [5, 3, 1],
       [2, 4, 1, 9]]
print(maxPathSum(tri, 3, 3))

# This code is contributed
# by Soumen Ghosh.