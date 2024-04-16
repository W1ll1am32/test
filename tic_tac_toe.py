import random


class Game:
    field = []
    user_input = []
    idx = 0
    win_points = 0
    size = 0
    numbers_conversion = {1: 'O', 0: ' ', -1: 'X'}   # 1 - Program, 0 - Empty cell, -1 - Player

    def __init__(self, size):
        self.size = size
        self.win_points = size * size + 1
        self.field = [[0 for _ in range(size)] for _ in range(size)]

    def set_input(self, move_list):
        self.user_input = move_list

    def set_size(self, size):
        self.size = size
        self.field = [[0 for _ in range(size)] for _ in range(size)]

    def draw_field(self):
        for i in range(self.size):
            print(' ' * 5 + ('|' + ' ' * 5) * (self.size - 1))

            for j in range(self.size):
                if j != self.size - 1:
                    print("  {}  ".format(self.numbers_conversion[self.field[i][j]]), end='|')
                else:
                    print("  {}  ".format(self.numbers_conversion[self.field[i][j]]))

            if i != self.size - 1:
                print('_' * 5 + ('|' + '_' * 5) * (self.size - 1))
            else:
                print(' ' * 5 + ('|' + ' ' * 5) * (self.size - 1))

    def get_turns(self):   # Finds all available cells and then shuffles them
        turns = []

        for i in range(self.size):
            for j in range(self.size):
                if not self.field[i][j]:   # if field[i][j] == 0 - Cell is empty
                    turns.append((i, j))

        random.shuffle(turns)
        return turns

    def check_winning_state(self, last_move):   # Checks if last move sets all n figures in line (row, column, diagonal)
        start_x, start_y = last_move
        directions = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)], [(1, 1), (-1, -1)], [(-1, 1), (1, -1)]]

        for d in directions:
            figures_in_line = 1
            for dx, dy in d:
                x, y = start_x, start_y
                while 1:
                    x += dx
                    y += dy
                    if x == self.size or y == self.size or x == -1 or y == -1:
                        break

                    if self.field[x][y] == self.field[start_x][start_y]:
                        figures_in_line += 1
                    else:
                        break

                    if figures_in_line == self.size:
                        return 1
        return 0

    def calculate_next_move(self, whose_turn, depth):   # Recursive minimax algorithm
        best_move = -1, -1                              # whose_turn: 1 - Program, -1 - Player
        best_value = -self.win_points * whose_turn

        if self.size != 3:                              # Shortens depth of recursion if size is big
            if 3 < self.size < 6:
                if depth > 4:
                    return depth, best_move
            elif 5 < self.size < 10:
                if depth > 3:
                    return depth, best_move
            elif 9 < self.size < 26:
                if depth > 2:
                    return depth, best_move
            else:
                if depth > 1:
                    return depth, best_move

        for x, y in self.get_turns():
            self.field[x][y] = whose_turn

            if self.check_winning_state((x, y)):
                best_move = x, y
                best_value = depth + self.win_points * whose_turn
                self.field[x][y] = 0
                return best_value, best_move
            else:
                new_value, new_move = self.calculate_next_move(whose_turn=-whose_turn, depth=depth + 1)
                if whose_turn == 1:
                    if new_value > best_value:
                        best_value = new_value
                        best_move = x, y
                else:
                    if new_value < best_value:
                        best_value = new_value
                        best_move = x, y

            self.field[x][y] = 0

        if best_move == (-1, -1):
            return depth, best_move
        else:
            return best_value, best_move

    def player_input(self):
        if not len(self.user_input):     # if len(user_input) != 0
            x, y = list(map(int, input("Enter your turn: ").split()))
            while self.field[x - 1][y - 1] != 0:
                x, y = list(map(int, input("This cell is already used, try another one: ").split()))
        else:
            print("Your turn:")
            x, y = self.user_input[self.idx]
            while self.field[x - 1][y - 1] != 0:
                self.idx += 1
                x, y = self.user_input[self.idx]
            self.idx += 1
        return x, y

    def start(self):
        turns_left = self.size * self.size
        is_players_turn = 1
        self.draw_field()

        while turns_left:
            if is_players_turn:
                x, y = self.player_input()
                self.field[x - 1][y - 1] = -1
                self.draw_field()
                if self.check_winning_state((x - 1, y - 1)):
                    print("You win!")
                    return -1
                is_players_turn = 0
                turns_left -= 1
            else:
                value, move = self.calculate_next_move(whose_turn=1, depth=1)
                x, y = move
                self.field[x][y] = 1
                print("My turn:")
                self.draw_field()
                if self.check_winning_state((x, y)):
                    print("I win!")
                    return 1
                is_players_turn = 1
                turns_left -= 1

        print("It's a draw!")
        return 0


if __name__ == '__main__':
    n = int(input("Input the size of the field: "))

    while n < 3 or n < 0:
        if n < 0:
            n = int(input("Size can't be a negative number: "))
        if n < 3:
            n = int(input("Please enter a value >= 3, otherwise the game will not be interesting: "))

    game = Game(n)
    print("\nYou can have a first turn\n"
          "Rows and columns are numbered starting from 1\n"
          "On your turn, input row and then column of the cell\n")
    game.start()
