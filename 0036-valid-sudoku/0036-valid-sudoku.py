class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # idea: mark row, col, and sub-board appearance for each element. Check repetition at the end. 
        tags = []
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != '.':
                    tags.append(f'{ele} @ {i}th row')
                    tags.append(f'{ele} @ {j}th col') 
                    tags.append(f'{ele} @ {i//3}-{j//3}th subboard')

        return len(tags) == len(set(tags))