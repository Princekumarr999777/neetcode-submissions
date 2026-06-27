class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_ele={}
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                check_ele=board[i][j]
                # lets check in rows
               
                row_key=f"row_{i}"
                col_key=f"col_{j}"
                box_key=f"box_{i//3}_{j//3}"
                
                if check_ele in seen_ele.get(row_key,[]):
                    return False
                
                # let's check in column
              
                    
                if check_ele in seen_ele.get(col_key,[]):
                    return False
            
                if check_ele in  seen_ele.get(box_key,[]):
                    return False
                


                if row_key not in seen_ele:
                    seen_ele[row_key]=[check_ele]
                else:
                    seen_ele[row_key].append(check_ele)
                

                if col_key not in seen_ele:
                    seen_ele[col_key]=[check_ele]
                else:
                    seen_ele[col_key].append(check_ele)

                if box_key not in seen_ele:
                    seen_ele[box_key]=[check_ele]
                else:
                    seen_ele[box_key].append(check_ele)
        return True




        