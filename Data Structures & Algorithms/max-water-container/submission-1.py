class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_p=0
        right_p=len(heights)-1
        max_arr=0

        while left_p<right_p:
            left_ele=heights[left_p]
            right_ele=heights[right_p]
            local_arr=min(left_ele,right_ele) * (right_p-left_p)
            max_arr=max(local_arr,max_arr)
            if  heights[left_p]<heights[right_p]:
                left_p +=1
            else:
                right_p -=1

        return max_arr

        