class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
         result = []
         i = 0
         while i < len(temperatures):
            j = i + 1
            
            found=False       
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    # append answer
                    result.append(j-i)
                    # stop searching
                    found=True
                    break                               
                j += 1
            if not found :
                result.append(0)

            i += 1
         return result