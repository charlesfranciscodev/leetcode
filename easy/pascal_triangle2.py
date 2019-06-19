class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        previous_row = [1,1]
        for i in range(2, rowIndex + 1):
            current_row = [1]
            previous_row.append(1)
            for k in range(1, len(previous_row) - 1):
                current_row.append(previous_row[k - 1] + previous_row[k])
            current_row.append(1)
            previous_row = current_row
        return previous_row
