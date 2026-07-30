class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:       
        curr_max=0
        for i in range(len(s)):
             seen=set()
             seen.add(s[i])
             for j in range(i+1,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    break
             curr_max=max(curr_max,len(seen))
        return curr_max

        