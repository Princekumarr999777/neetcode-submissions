class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd_list=sorted(zip(position,speed),reverse=True)
        stack=[]

        for i,j in pos_spd_list:
            time=(target-i)/j
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
        