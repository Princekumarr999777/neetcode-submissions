class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        total = 0
        for ele in tokens:


            if ele in {"+","-","*","/"}:
                if ele == "+":
                    second_ele=stack.pop()
                    
                    
                    first_ele=stack.pop()
                    

                    total = first_ele+second_ele
                    stack.append(total)
                elif ele == "-":

                    second_ele=stack.pop()
                    
                    
                    first_ele=stack.pop()
                   

                    total = first_ele-second_ele
                    stack.append(total)
                elif ele == "*":
                    second_ele=stack.pop()
                    
                    
                    first_ele=stack.pop()
                    

                    total = first_ele*second_ele
                    stack.append(total)
                elif ele == "/":
                    second_ele=stack.pop()
                    
                    
                    first_ele=stack.pop()
                    

                    total = int(first_ele/second_ele)
                    stack.append(total)
            else:
                stack.append(int(ele))
        return stack[-1]




        