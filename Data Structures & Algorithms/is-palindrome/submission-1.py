class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        Stri_with_al_nu="".join(ele.lower() for ele in s if ele.isalnum())
        lenofs=len(Stri_with_al_nu)
        while i<lenofs//2:
            if Stri_with_al_nu[i] !=Stri_with_al_nu[-(i+1)]:
                return False
            i +=1

        return True
            

        

        