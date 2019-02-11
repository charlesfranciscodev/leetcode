class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # rows
        for i in range(0, 9):
            digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            for j in range(0, 9):
                digit = board[i][j]
                if (digit != '.'):
                    if (digit in digits):
                        digits.remove(digit)
                    else:
                        return False
        
        # columns
        for j in range(0, 9):
            digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            for i in range(0, 9):
                digit = board[i][j]
                if (digit != '.'):
                    if (digit in digits):
                        digits.remove(digit)
                    else:
                        return False
        
        # sub-boxes
        for i in range(0, 9, 3):
            for j in range (0, 9, 3):
                if (not self.isValidSubBox(board, i, i + 3, j, j + 3)):
                    return False    
        
        return True

    def isValidSubBox(self, board, min_i, max_i, min_j, max_j):
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for i in range(min_i, max_i):
            for j in range(min_j, max_j):
                digit = board[i][j]
                if (digit != '.'):
                    if (digit in digits):
                        digits.remove(digit)
                    else:
                        return False
        return True
