class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_index=0
        right_index=(len(matrix))*(len(matrix[0]))-1
        no_col=len(matrix[0])
        
        
        while left_index <= right_index:
            mid_index=(left_index+right_index)//2
            
            if target < matrix[mid_index //no_col][mid_index % no_col]:

                right_index=mid_index-1
                
            elif target > matrix[mid_index //no_col][mid_index % no_col]:
                
                left_index=mid_index+1
               
            else:
                if target==matrix[mid_index // no_col][mid_index % no_col]:

                    return True
        return False    

            
        