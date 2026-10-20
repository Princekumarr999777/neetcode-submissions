class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result=[]
        hashmap={}
        required_ele=0

        for i in range( len(nums)):
            required_ele=target-nums[i]
            if required_ele in hashmap:
                if i<=hashmap.get(required_ele):
                    result.append(i)
                    result.append(hashmap.get(required_ele))
                else:
                    result.append(hashmap.get(required_ele))
                    result.append(i)



                
                return result
            else:
                hashmap[nums[i]]=i

            
        