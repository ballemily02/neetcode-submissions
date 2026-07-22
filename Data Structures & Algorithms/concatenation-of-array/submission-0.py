class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        rot = 0
        while rot < 2:
            for i in range(0, len(nums)):
                ans.append(nums[i])
            rot += 1
        return ans

