class Solution: # [1,2,4,6]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # [1,2,3,4]

        prefix = 1
        for i in range(len(nums)):
            # i=0 [1] , prefix = 1
            # i=1 [1,1], prefix = 2
            # i=2 [1,1,2], prefix = 8 
            # i=3 [1,1,2,8], prefix = 48
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # i=3 [1,1,2,8] , postfix = 8
            # i=2 [1,1,16,8], postfix = 32
            # i=1 [1,32,16,8], postfix = 64
            # i=0 [64,32,18,8], postfix = 64
            res[i] *= postfix
            postfix *= nums[i]
        return res