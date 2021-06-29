class Solution:
    def dfs(self, board, x, y):
        
        # terminal pt
        if board[x][y] != 'O': 
            # print(f'{board[x][y]}, {x}, {y}')
            return
        
        board[x][y] = "#"
        # print(board)
        
        #上下左右
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        for i in range(4):
            if(y + dy[i] >= 0 and y + dy[i] < self.col and x + dx[i]>= 0 and x + dx[i]< self.row):
                self.dfs(board, x + dx[i], y + dy[i])
            
            
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        想法：只有連到邊邊的圈不會被flip-> dfs
        1. find boarder 'O's and dfs each
        2. flip captured #->O uncaptured O-> X
        
        """
        
        self.row = len(board)
        self.col = len(board[0])
        
        # 左右boarder
        for i in range(self.row):
            if board[i][0] == 'O': self.dfs(board, i, 0)
            if board[i][self.col-1] == 'O': self.dfs(board, i, self.col-1)
        
        # 上下boarder
        for j in range(self.col):
            if board[0][j] == 'O': self.dfs(board, 0, j)
            if board[self.row-1][j] == 'O': self.dfs(board, self.row-1, j)
        
        
        
        # flip captured
        for i in range(self.row):
            for j in range(self.col):
                if (board[i][j] == "#"): board[i][j] = "O"
                elif (board[i][j] == "O"): board[i][j] = "X"
                
        # print(board)
        
        
        
