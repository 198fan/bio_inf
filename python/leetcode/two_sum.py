#My initial answer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j: # change to j>i, too much duplication
                    if nums[i]+nums[j] == target:
                        ans.append(i)
                        ans.append(j)
                        return ans

# Optimal solution
class Solution(object):
    def twoSum(self, nums, target):
        seen = {} #initiate dictionary/hash table for lookup
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i #key=value; value=position