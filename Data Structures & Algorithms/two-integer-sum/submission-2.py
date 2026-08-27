class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for count_i, i in enumerate(nums):
            for count_j, j in enumerate(nums):
                if i + j == target and count_i != count_j:
                    return [count_i, count_j]