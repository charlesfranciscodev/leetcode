class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if (matrix[i][j] == 0):
                    rows.add(i)
                    columns.add(j)
    
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[i])):
                if (x in rows or y in columns):
                    matrix[x][y] = 0
