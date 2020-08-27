############################################################
# Connect 4 By Jack Donofrio                               #
# I'll get around to making a GUI for this one eventually  #
# 2:58 PM August 27 2020                                   #
############################################################

class Piece:
    EMPTY = 0
    RED = 1
    YELLOW = 2

class ConnectFour:
    # 7 slots in each of the 6 rows
    def __init__(self):
        self.grid = [[Piece.EMPTY for x in range(7)] for y in range(6)]

    def move_is_valid(self, column):
        return column >= 0 and column < 7 and self.grid[0][column] == Piece.EMPTY

    def make_move(self, piece_value, column):
        row = -1
        while row < 5 and self.grid[row + 1][column] == Piece.EMPTY:
            row += 1
        self.grid[row][column] = piece_value

        winner = self.check_for_winner(row, column, piece_value)
        if winner:
            return True

    # pivot from most recently made move to scan for winning order
    # rather than iterating through the entire grid.
    def check_for_winner(self, pivot_row, pivot_column, value):
        
        current_column = pivot_column
        left_streak = 0
        while current_column >= 0 and self.grid[pivot_row][current_column] == value:
            left_streak += 1
            current_column -= 1

        current_column = pivot_column
        right_streak = 0
        while current_column < 7 and self.grid[pivot_row][current_column] == value:
            right_streak += 1
            current_column += 1
    
        # must subtract 1 because both streaks count the starting piece 
        if left_streak + right_streak - 1 >= 4:
            return value # value is winner

        current_row = pivot_row
        up_streak = 0
        while current_row >= 0 and self.grid[current_row][pivot_column] == value:
            up_streak += 1
            current_row -= 1
        
        current_row = pivot_row
        down_streak = 0
        while current_row < 6 and self.grid[current_row][pivot_column] == value:
            down_streak += 1
            current_row += 1
        
        if up_streak + down_streak - 1 >= 4:
            return value
        
        up_left_streak = 0
        current_row = pivot_row
        current_column = pivot_column
        while current_row >= 0 and current_column >= 0 and self.grid[current_row][current_column] == value:
            up_left_streak += 1
            current_column -= 1
            current_row -= 1
        
        down_right_streak = 0
        current_row = pivot_row
        current_column = pivot_column
        while current_row < 6 and current_column < 7 and self.grid[current_row][current_column] == value:
            down_right_streak += 1
            current_column += 1
            current_row += 1
        
        if up_left_streak + down_right_streak - 1 >= 4:
            return value
        
        up_right_streak = 0
        current_row = pivot_row
        current_column = pivot_column
        while current_row >= 0 and current_column < 6 and self.grid[current_row][current_column] == value:
            up_right_streak += 1
            current_row -= 1
            current_column += 1
        
        down_left_streak = 0
        current_row = pivot_row
        current_column = pivot_column
        while current_row < 6 and current_column >= 0 and self.grid[current_row][current_column] == value:
            down_left_streak += 1
            current_row += 1
            current_column -= 1
        
        if up_right_streak + down_left_streak - 1 >= 4:
            return value
        
        return 0 # no winner
    
    def show_board(self):
        for x in self.grid:
            for y in x:
                print(y,end='')
            print()

if __name__ == '__main__':
    game = ConnectFour()
    while True:
        game.show_board()
        # Red
        column = -1
        while not game.move_is_valid(column):
            column = int(input('Red Column: '))
        if game.make_move(Piece.RED, column):
            print('Red Wins!')
            break
        game.show_board()
        # Yellow
        column = -1
        while not game.move_is_valid(column):
            column = int(input('Yellow Column: '))
        if game.make_move(Piece.YELLOW, column):
            print('Yellow Wins!')
            break
