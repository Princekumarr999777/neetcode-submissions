class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set=set(nums)
        longest_sequence=0


        for num in num_set:

            current_no=0
            count=0
            if num - 1 not in num_set:

                current_no=num
                count=1

                while current_no + 1 in num_set:
                    current_no +=1
                    count +=1

                longest_sequence=max(longest_sequence,count) 

        return longest_sequence

            


        