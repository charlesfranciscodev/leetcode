class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if (numRows == 0):
            return []
        if (numRows == 1):
            return [[1]]
        triangle = [[1], [1,1]]
        for i in range(2, numRows):
            triangle.append([])
            for j in range(0, i + 1):
                triangle[i].append(1)
            for k in range(1, len(triangle[i]) - 1):
                triangle[i][k] = triangle[i - 1][k - 1] + triangle[i - 1][k]
        return triangle
