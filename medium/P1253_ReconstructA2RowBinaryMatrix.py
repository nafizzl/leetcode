# Given the following details of a matrix with n columns and 2 rows :

# The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
# Your task is to reconstruct the matrix with upper, lower and colsum.

# Return it as a 2-D integer array.

# If there are more than one valid solution, any of them will be accepted.

# If no valid solution exists, return an empty 2-D array.

class P1253_ReconstructA2RowBinaryMatrix:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []                                       # if upper and lower don't sum to colsum, then reconstruction of matrix isn't possible
        
        ans = [[],[]]
        upperCurrent = 0
        lowerCurrent = 0                                    # make variables for answer and limit checker

        for index in colsum:
            ans[0].append(0)
            ans[1].append(0)                                # fill in matrix with dummies
        
        for i in range(len(colsum)):
            if colsum[i] == 0:
                ans[0][i] = 0
                ans[1][i] = 0
            elif colsum[i] == 2:
                ans[0][i] = 1
                ans[1][i] = 1
                upperCurrent += 1
                lowerCurrent += 1                           # place the values when colsum[i] == 0 or 2
        
        if (upperCurrent > upper or lowerCurrent > lower):
            return []                                       # if a limit is violated here, return empty
        
        for i in range(len(colsum)):
            if colsum[i] == 1:
                if (upperCurrent != upper):
                    ans[0][i] = 1
                    upperCurrent += 1
                elif (lowerCurrent != lower):
                    ans[1][i] = 1
                    lowerCurrent += 1                       # at this point, matrix is possible, so just place the 1s in either upper or lower row, wherever appropriate

        
        return ans
