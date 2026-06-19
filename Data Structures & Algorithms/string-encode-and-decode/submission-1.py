class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for ele in strs:
            string +=str(len(ele))+"#"+ele



        return string
        
        
   
    def decode(self, s: str) -> List[str]:
        # my string = "3#hii5#world"
        result=[]
        i=0
        lengthofword=""
        while i < len(s):
            while s[i]!="#":
                lengthofword += s[i]
                i +=1
            
            word=s[i+1:i+int(lengthofword)+1]
            result.append(word)
            
            i = i +int(lengthofword)+1
            lengthofword= "" 

            
        return result   

            

       
       
                    


       
