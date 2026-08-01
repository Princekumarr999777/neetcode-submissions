class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ans=0
        left=0
        right=0
        frequency={} 
         
        for right in range(len(s)):
            
            
            
            if s[right] in frequency:
                frequency[s[right]] +=1
            else:
                frequency[s[right]]=1
            max_frequency=max(frequency.values())
            len_substring=right-left+1
            changes=len_substring-max_frequency
            if changes<=k:
                

                
                ans=max(ans,len_substring)
                
            else:


                while changes>k:
                    
                        
                    frequency[s[left]] -=1
                    left +=1
                    max_frequency=max(frequency.values())
                    len_substring=right-left+1
                    changes=len_substring-max_frequency
                ans=max(ans,len_substring)

        return ans

                
