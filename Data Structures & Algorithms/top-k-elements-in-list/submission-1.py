class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        dict={}
        visited = set()
        for no in nums:
          
            if no in dict:
                dict[no] +=1
            if no not in visited:
                dict[no]=1
                visited.add(no)

            

        sorted_list=sorted(dict.items(),key=lambda x:x[1],reverse=True)
        result=[key for key , value in sorted_list]
        return result[:k]