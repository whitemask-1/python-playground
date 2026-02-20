from typing import List

def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)] # Gives a list of sets from range 0-8
        column = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        # row, column, boxes = ([set() for _ in range(9)] for _ in range(3))
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                if val in row[i]:
                    return False
                if val in column[j]:
                    return False
                if val in boxes[(i // 3) * 3 + (j // 3)]:
                    return False
                
                row[i].add(val)
                column[j].add(val)
                boxes[(i // 3) * 3 + (j // 3)].add(val)

        return True

# First instict was to try dictionary mapping the row and column to the value and then check the dictionary for validity
# Then I realized that this would be many operations to set up the dictionary and then use it so I pivoted into using sets
# Right after realizing that I needed to use sets I assigned a list of sets from 0-8 to each the row, column, and boxes variable
# Which I now after solving realize could be a single line to assign all of those variables as done in the comment
# We obviously accept empty squares ('.') as duplicates and continue
# Then check against the row column and boxes algorithm for each row/column pair
# If no match is found the value is added to the row column and boxes and then run the for loop until all values are exhausted or a duplicate is found