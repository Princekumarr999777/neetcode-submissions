class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_cap=0



        left_index=0
        right_index=len(height)-1
        left_highest=height[left_index]
        right_highest=height[right_index]
        while left_index < right_index:

            if height[left_index] < height[right_index]:

                if height[left_index]>=left_highest :
                    left_highest = height[left_index]
                else:
                    total_cap +=left_highest - height[left_index]
                left_index +=1
            else:
                if height[right_index] >= right_highest:
                    right_highest=height[right_index]
                else:
                    total_cap += right_highest-height[right_index]
                right_index -=1

           

                    
            
            
            
        return total_cap


            



                



                


        