class Solution:
    def secondHighest(self, s: str) -> int:
        nums = []
        for char in s:
            if char.isdigit():
                nums.append(int(char))
        new = set(nums)
        if len(new) < 2:
            return -1
        x = max(new)
        new = [x for x in new if x != max(new)]
        if len(new) == 0: 
            return -1
        else:
            return int(max(new))