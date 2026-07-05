class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_cap=0


        for index  in range(len(heights)):
            bar_to_check = heights[index]
            for sec_index in range(index+1,len(heights)):
                curr_min=min(bar_to_check,heights[sec_index])
                curr_capacity=curr_min*(sec_index-index)
                if curr_capacity>max_cap:
                    max_cap=curr_capacity
        return max_cap
        