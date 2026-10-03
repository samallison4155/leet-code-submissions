class Solution:
    def containsDuplicate(self, nums: list[int]):
        if len(set(nums)) != len(nums):
            return True
        else:
            return False    