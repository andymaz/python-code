

class LatinSqrSolution(object):

    def __init__(self, size):
        self.size = size**2
        self.board = [0 for _ in range(self.size)]

    def __str__(self):
        temp = ''
        for n in range(self.size):
            if n % 3 == 0:
                temp += '\n' 
            temp += '   ' + str(self.board[n])
        return temp                  

    def solved(self):
        temp = self.board[0] + self.board[1] + self.board[2]
        if self.board[3] + self.board[4] + self.board[5] != temp:
            return False
        elif self.board[6] + self.board[7] + self.board[8] != temp:
            return False
        elif self.board[0] + self.board[3] + self.board[6] != temp:
            return False  
        elif self.board[1] + self.board[4] + self.board[7] != temp:
            return False
        elif self.board[2] + self.board[5] + self.board[8] != temp:
            return False
        elif self.board[0] + self.board[4] + self.board[8] != temp:
            return False
        elif self.board[2] + self.board[4] + self.board[6] != temp:
            return False
        else:
            return True                                         

    def to_be_placed(self):
        return [x for x in range(1, 10) if x not in self.board]        

    def latin_square(self, n):
        if n < self.size:
            sf = self.to_be_placed()          
            for x in sf:                                
                self.board[n] = x
                self.latin_square(n + 1)
                if n+1 == self.size and self.solved():
                    print(self)                        
                self.board[n] = 0

if __name__ == '__main__':        
    s = LatinSqrSolution(3)
    s.latin_square(0)


