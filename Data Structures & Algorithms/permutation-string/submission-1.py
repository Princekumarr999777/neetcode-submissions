class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        frequency_s1={}
        frequency_sub_s2={}
        left =0
        for s1_index in range(len(s1)):
            if s1[s1_index] in frequency_s1:

                frequency_s1[s1[s1_index]] +=1
            else:
                frequency_s1[s1[s1_index]] =1
            if s2[s1_index] in frequency_sub_s2:

                frequency_sub_s2[s2[s1_index]] +=1
            else:
                frequency_sub_s2[s2[s1_index]] =1
        if frequency_s1==frequency_sub_s2:
            return True
        for right in range(len(s1),len(s2)):
            frequency_sub_s2[s2[left]] -=1
            if frequency_sub_s2[s2[left]] == 0:
                del frequency_sub_s2[s2[left]]
            left +=1
            # if right-left + 1 == len(s1):
            
           
                
                
            if s2[right] in frequency_sub_s2:

                frequency_sub_s2[s2[right]] +=1
            else:
                frequency_sub_s2[s2[right]] =1
            if frequency_s1 == frequency_sub_s2:
                return True
        return False

        