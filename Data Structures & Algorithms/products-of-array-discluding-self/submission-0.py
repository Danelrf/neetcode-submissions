class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1 :
            return []
        arr = []
        for i, p in enumerate(nums):
            res = 1
            for j, num in enumerate(nums):
                if i==j:
                    continue
                res = res*num
                
            
            arr.append(res)
        return arr