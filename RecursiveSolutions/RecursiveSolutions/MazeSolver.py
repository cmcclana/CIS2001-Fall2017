maze = [
    [ "S", "W", "W", "W", "W" ],
    [ " ", "W", " ", " ", "W" ],
    [ " ", " ", " ", "W", "W" ],
    [ " ", "W", "W", " ", " " ],
    [ " ", " ", " ", " ", " " ]
    ]

class Maze():
    def __init__(self, maze):
        self.unsolved = True
        self.maze = maze

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
        #print( "trying x: %d y: %d" % ( x, y ) )
        if self.maze[y][x] == "E":
            self.unsolved = False
            print("Found ending at X: %d - Y:%d" % (x,y) )
       
        # left
        if self.unsolved and x - 1 >= 0 and self._can_move_to(y,x-1):
            self.maze[y][x] = "."
            self.FindNextMove(x-1, y)
    
        # right
        if self.unsolved and x + 1 < len(self.maze[x]) and self._can_move_to(y,x+1):
            self.maze[y][x] = "."
            self.FindNextMove(x+1, y)
    
        #down
        if self.unsolved and y + 1 < len(self.maze) and self._can_move_to(y+1,x):
            self.maze[y][x] = "."
            self.FindNextMove( x, y+1)

        #up
        if self.unsolved and y - 1 >= 0 and self._can_move_to(y-1,x):
            self.maze[y][x] = "."
            self.FindNextMove( x, y-1)

        if self.unsolved:
            self.maze[y][x] = "X"


mazeToSolve = Maze(maze)
mazeToSolve.SolveMaze()

