class Solution:
    def rotateString(self, a: str, b: str) -> bool:
        if len(a) == 0 and len(b) == 0:
            return True
        if len(a) != len(b):
            return False 
        
        start_index = b.find(a[0], 0)
        if start_index == -1:
            return False
        while start_index != -1:
            index = start_index
            letter_count = 0
            unrotated_b = ""
            while letter_count < len(b):
                unrotated_b += b[index]
                index += 1
                if index >= len(b):
                    index = 0
                letter_count += 1
            if a == unrotated_b:
                return True
            start_index = b.find(a[0], start_index + 1)
        
        return False
