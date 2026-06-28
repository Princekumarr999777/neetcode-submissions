class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_ele=set(nums)
        
        longest=0
    
        for nums in set_of_ele:

             if nums - 1 not in set_of_ele:

                current=nums
                len=1

                while current +1 in set_of_ele:
                    current +=1
                    len +=1
                longest=max(longest,len)

        return longest
                
            
            
             

        