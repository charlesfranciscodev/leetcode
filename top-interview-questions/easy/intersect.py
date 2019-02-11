class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_dict = {}
        intersection = []
        
        for num1 in nums1:
            if (num1 in num_dict):
                num_dict[num1] += 1
            else:
                num_dict[num1] = 1
                
        for num2 in nums2:
            if (num2 in num_dict):
                intersection.append(num2)
                if (num_dict[num2] == 1):
                    del num_dict[num2]
                else:
                   num_dict[num2] -= 1 
    
        return intersection
