from collections import deque

def process_case(grid):
    ROWS, COLS = 6, 7
    PLAYERS = ['C', 'F']

    def check_win(grid, player):
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] != player:
                    continue

                if col + 3 < COLS and all(grid[row][col + i] == player for i in range(4)):
                    return True

                if row + 3 < ROWS and all(grid[row + i][col] == player for i in range(4)):
                    return True

                if row + 3 < ROWS and col + 3 < COLS and all(grid[row + i][col + i] == player for i in range(4)):
                    return True

                if row + 3 < ROWS and col - 3 >= 0 and all(grid[row + i][col - i] == player for i in range(4)):
                    return True
        return False


    C_WINNING = False
    F_WINNING = False


    columns = [[] for _ in range(COLS)]
    for col in range(COLS):
        for row in range(ROWS):
            piece = grid[row][col]
            if piece in PLAYERS:
                columns[col].append(piece)

    initial_player = 'F'


    from copy import deepcopy
    queue = deque()
    visited_states = set()


    def get_state_key(columns):
        return tuple(tuple(col) for col in columns)

    initial_state = (columns, initial_player)
    queue.append(initial_state)
    visited_states.add(get_state_key(columns))

    while queue:
        current_columns, current_player = queue.popleft()
        grid_state = [['.' for _ in range(COLS)] for _ in range(ROWS)]
        for col in range(COLS):
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
            for col in range(COLS):
                if current_columns[col]:
                    if current_columns[col][-1] == current_player:
                        player_pieces_on_top.append(col)
            for col in player_pieces_on_top:
                new_columns = deepcopy(current_columns)
                new_columns[col] = new_columns[col][:-1]
                state_key = get_state_key(new_columns)
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
        grid = []
        _ = input()
        grid = [list(input()) for _ in range(6)]
        grid = grid[::-1]

        result = process_case(grid)
        print(f"Case #{case+1}: {result}")

main()
