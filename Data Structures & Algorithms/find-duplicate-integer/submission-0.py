class Solution:
    def findDuplicate(self, nums: List[int]) -> int:



        visited=set()
        for index in nums:
            if index in visited :
                return index
            else:

                visited.add(index)

            