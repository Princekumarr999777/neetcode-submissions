class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen={}
        for i in range(len(nums)):
            new_target=target-nums[i]
            if new_target in seen:
            
                return [seen[new_target],i]
             
            else:
                seen[nums[i]]=i
     