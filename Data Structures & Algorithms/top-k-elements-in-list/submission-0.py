class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        

        dict={}
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                 dict[nums[i]]=1
            visited.add(nums[i])

           
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] :
                    dict[nums[i]] +=1


        sorted_list=list(sorted(dict.items(),key= lambda x: x[1],reverse=True)  )
        result=[]
        for key,value in sorted_list:
            result.append(key)

        return result[:k]
                


     
        