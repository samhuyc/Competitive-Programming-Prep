from collections import deque
from copy import deepcopy


def solve():
    R, C = 6, 7
    P = ['C', 'F']
    _ = input()
    mat = [list(input()) for _ in range(6)]
    mat = mat[::-1]

    def check_win(grid, player):
        for row in range(R):
            for col in range(C):
                if grid[row][col] != player:
                    continue
                if col + 3 < C and all(grid[row][col + i] == player for i in range(4)):
                    return True
                if row + 3 < R and all(grid[row + i][col] == player for i in range(4)):
                    return True
                if row + 3 < R and col + 3 < C and all(grid[row + i][col + i] == player for i in range(4)):
                    return True
                if row + 3 < R and col - 3 >= 0 and all(grid[row + i][col - i] == player for i in range(4)):
                    return True
        return False


    C_WINNING = False
    F_WINNING = False

    columns = [[] for _ in range(C)]
    for col in range(C):
        for row in range(R):
            piece = mat[row][col]
            if piece in P:
                columns[col].append(piece)

    initial_player = 'F'

    queue = deque()
    visited_states = set()


    initial_state = (columns, initial_player)
    queue.append(initial_state)
    visited_states.add(tuple(tuple(col) for col in columns))

    while queue:
        print(C_WINNING, F_WINNING)
        current_columns, current_player = queue.popleft()
        grid_state = [['.' for _ in range(C)] for _ in range(R)]
        for col in range(C):
            col_pieces = current_columns[col]
            for row in range(len(col_pieces)):
                grid_state[row][col] = col_pieces[row]
        C_wins = check_win(grid_state, 'C')
        F_wins = check_win(grid_state, 'F')

        if C_wins and not F_wins:
            C_WINNING = True
            if C_WINNING and F_WINNING:
                return '?'
            continue
        elif F_wins and not C_wins:
            F_WINNING = True
            if C_WINNING and F_WINNING:
                return '?'
            continue 
        elif not C_wins and not F_wins:
            continue 
        else: 
            next_player = 'C' if current_player == 'F' else 'F'
            player_pieces_on_top = []
            for col in range(C):
                if current_columns[col]:
                    if current_columns[col][-1] == current_player:
                        player_pieces_on_top.append(col)
            for col in player_pieces_on_top:
                new_columns = deepcopy(current_columns)
                new_columns[col] = new_columns[col][:-1]
                state_key = tuple(tuple(col) for col in columns)
                if state_key not in visited_states:
                    visited_states.add(state_key)
                    queue.append((new_columns, next_player))
            if not player_pieces_on_top:
                continue
        if C_WINNING and F_WINNING:
            return '?'

    if C_WINNING and F_WINNING:
        return '?'
    elif C_WINNING:
        return 'C'
    elif F_WINNING:
        return 'F'
    else:
        return '0'


def main():
    t = int(input())
    for case in range(t):
        ans = solve()
        print(f"Case #{case+1}: {ans}")

main()