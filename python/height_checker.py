class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nb_misplaced_students = 0
        sorted_heights = sorted(heights)
        for i in range(0, len(heights)):
            if heights[i] != sorted_heights[i]:
                nb_misplaced_students += 1
        return nb_misplaced_students
