class Solution:
    def twoSum(nums, target):
        temp = [0] * len(nums)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]
solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))