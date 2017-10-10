maze = [
    [ "S", "W", "W", "W", "W" ],
    [ " ", "W", " ", " ", "E" ],
    [ " ", " ", " ", "W", " " ],
    [ " ", "W", "W", " ", " " ],
    [ " ", " ", " ", " ", " " ]
    ]

class Maze():
    def __init__(self, maze):
        self.unsolved = True
        self.maze = maze
        self.number_of_moves = 0
        self.least_number_of_moves = len(maze)**2

    def SolveMaze(self):
        start_x = 0
        start_y = 0
        for row in range(len(self.maze)):
            if "S" in maze[row]:
                start_x = row
                start_y = self.maze[row].index("S")
        self.FindNextMove(start_x, start_y)
        if self.unsolved:
            print("No solution!")
        for row in self.maze:
            print(row)

    def _can_move_to(self,y, x):
        return self.maze[y][x] == " " or self.maze[y][x] == "E"

    def FindNextMove(self, x, y):
        self.number_of_moves += 1
        #print( "trying x: %d y: %d" % ( x, y ) )
        if self.maze[y][x] == "E":
            if self.number_of_moves < self.least_number_of_moves:
                self.least_number_of_moves = self.number_of_moves
            self.unsolved = False
            print("Found ending at X: %d - Y:%d - in %d moves" % (x,y, self.number_of_moves) )
        else:
            # left
            if x - 1 >= 0 and self._can_move_to(y,x-1):
                self.maze[y][x] = "."
                self.FindNextMove(x-1, y)
                self.number_of_moves -= 1
                self.maze[y][x] = " "
    
            # right
            if x + 1 < len(self.maze[x]) and self._can_move_to(y,x+1):
                self.maze[y][x] = "."
                self.FindNextMove(x+1, y)
                self.number_of_moves -= 1
                self.maze[y][x] = " "
    
            #down
            if y + 1 < len(self.maze) and self._can_move_to(y+1,x):
                self.maze[y][x] = "."
                self.FindNextMove( x, y+1)
                self.number_of_moves -= 1
                self.maze[y][x] = " "

            #up
            if y - 1 >= 0 and self._can_move_to(y-1,x):
                self.maze[y][x] = "."
                self.FindNextMove( x, y-1)
                self.number_of_moves -= 1
                self.maze[y][x] = " "

            if self.unsolved:
                self.maze[y][x] = "X"


mazeToSolve = Maze(maze)
mazeToSolve.SolveMaze()
print("Least number of moves to solve:", mazeToSolve.least_number_of_moves)

