class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [1,7,4,2,4,1,3] -> [1,7,4,2,3]
        # 4 -> [1,2,3,4]
        # Dict Could have as many keys as elements so n-keys = len(nums)
        # In this case 7
        # Values -> how many sequences
        if not nums:
            return 0
        nums.sort()
        streak = 1
        res=1
        for i in range(len(nums)-1):
            num = nums[i]
            if num == nums[i+1]:
                continue
            if num == nums[i+1] - 1:
                streak +=1
            else:
                streak = 1
            res = max(streak,res)

        return res