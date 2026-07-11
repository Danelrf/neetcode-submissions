class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or target < nums[0] or target > nums[-1]:
            return -1

        i = 0
        j = len(nums) - 1
        print(f"Looking for {target}, starting at {i}")

        while i <= j:
            center = (i + j) // 2
            if nums[center] == target:
                print(f"Looking for {target}, found at i:{center}")
                return center
            if target > nums[center]:
                i = center + 1
            else:
                j = center - 1

        return -1