class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)+1
        answer=0
        
        
        while left <= right:
            total=0
            mid=(left+right)//2
            for ele in piles:

                k=(ele+mid-1)//mid
                total +=k
           
            if  h < total:
                left=mid+1
            elif h >= total:
                right=mid-1
                answer=mid
            
                

            

            
          

                    
        return answer
                



            
            


