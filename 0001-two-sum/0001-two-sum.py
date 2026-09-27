class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in nums:
                for x in range(len(nums)):
                    if nums[x] == needed and x != i:
                        return[i,x]
        else:
            return None
                


            
            
            

        