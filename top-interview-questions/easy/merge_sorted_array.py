class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        nums3 = []
        while (i < m and j < n):
            if (nums1[i] < nums2[j]):
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        while (i < m):
            nums3.append(nums1[i])
            i += 1

        while (j < n):
            nums3.append(nums2[j])
            j += 1
                
        for k in range(0, len(nums1)):
            nums1[k] = nums3[k]
