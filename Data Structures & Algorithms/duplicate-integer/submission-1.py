class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             if nums[i]==nums[j]:
        #                 return True
        # return False
        visited_ele=set()
        for i in range(len(nums)):
            if nums[i] in visited_ele:
                return True
            visited_ele.add(nums[i])
        return False
        