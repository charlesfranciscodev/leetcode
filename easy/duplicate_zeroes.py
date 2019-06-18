class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = []
        for n in arr:
            new_arr.append(n)
            if n == 0:
                new_arr.append(n)
            if len(new_arr) >= len(arr):
                break
        for i in range(len(arr)):
            arr[i] = new_arr[i]
