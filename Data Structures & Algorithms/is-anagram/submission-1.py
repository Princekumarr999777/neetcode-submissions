class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the  strings
        sorted_s=sorted(s)
        sorted_t=sorted(t)

        # if len(sorted_s) == len(sorted_t):
        #     for i in range(len(s)):
        #         if sorted_s[i] != sorted_t[i]:
        #             return False
        #     return True
        # else:
        #     return False
        return sorted_s==sorted_t