class MinStack:

    def __init__(self):
        self.stack=[]
        self.curr_min_stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.curr_min_stack:
                if self.curr_min_stack[-1]<val:
                         self.curr_min_stack.append(self.curr_min_stack[-1])

                else:
                        self.curr_min_stack.append(val)

               
        else:

                self.curr_min_stack.append(val)
               
        
                

        

    def pop(self) -> None:
        self.stack.pop()
        self.curr_min_stack.pop()
        

    def top(self) -> int:
        if self.stack :


                peek=self.stack[-1]
                return peek
        return -1
        

    def getMin(self) -> int:

        return self.curr_min_stack[-1]
        

        
