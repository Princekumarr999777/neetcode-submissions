class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        
        for ele in range(len(nums)):
            product=1
            for sec_tim_ele in range(len(nums)):
                if sec_tim_ele ==ele:
                    continue
               
                product *=nums[sec_tim_ele]
            result.append(product)
        return result
                
