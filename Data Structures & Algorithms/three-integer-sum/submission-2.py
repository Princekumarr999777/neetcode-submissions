class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        unique_ele=sorted(nums)

        for a in range(len(nums)):
            i=a+1
            j=len(unique_ele)-1

                
            while i< j:
                
                req_ele=(unique_ele[i]+unique_ele[j])
                if  i!=a!=j and req_ele+unique_ele[a]==0:
                    result.append([unique_ele[i],unique_ele[j],unique_ele[a]])
                    i += 1
                    j -= 1

                elif  i!=a!=j and req_ele+unique_ele[a]<0:
                    i +=1
                elif  i!=a!=j and req_ele+unique_ele[a]>0:
                    j -=1
               
        

        unique = list(set(tuple(x) for x in result))
        return unique
