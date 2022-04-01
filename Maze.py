maze_as_dict = {}

maze_rows = int(input())

# adding the maze pattern splt
for rows in range(1, maze_rows + 1):
    current_row = input()
    temp_list = [x for x in current_row]
    maze_as_dict[rows] = temp_list

"""
x = column
y = index
k = kate's position
' ' = free space
# = wall

    To check UP index: x + 1[y]
    To check DOWN index: x- 1[y]
    
    To check RIGHT index: x[y - 1]
    To check LEFT index: x[y + 1]
    
"""


def top_check(maze_dict: dict, kate_column: int, kate_index: int, is_open):
    # top check

    if maze_dict[kate_column - 1][kate_index] == "#":
        # top position is wall
        return maze_dict, is_open
    else:
        # top position is open
        maze_dict[kate_column - 1][kate_index] = 'k'
        maze_dict[kate_column][kate_index] = '#'
        is_open = True
        kate_position = maze_dict[kate_column - 1][kate_index]
        return maze_dict, is_open, kate_position


def bot_check(maze_dict: dict, kate_column: int, kate_index: int, is_open: bool):
    # bot check

    if maze_dict[kate_column + 1][kate_index] == "#":
        # bot position is wall
        return maze_dict, is_open
    else:
        # bot position is open
        maze_dict[kate_column + 1][kate_index] = 'k'
        maze_dict[kate_column][kate_index] = '#'
        is_open = True
        kate_position = maze_dict[kate_column + 1][kate_index]
        return maze_dict, is_open, kate_position


def right_check(maze_dict: dict, kate_column: int, kate_index: int, is_open: bool):
    # right check

    if maze_dict[kate_column][kate_index + 1] == "#":
        # right position is wall
        return maze_dict, is_open
    else:
        # right position is open
        maze_dict[kate_column][kate_index + 1] = 'k'
        maze_dict[kate_column][kate_index] = '#'
        is_open = True
        kate_position = maze_dict[kate_column][kate_index + 1]
        return maze_dict, is_open, kate_position


def left_check(maze_dict: dict, kate_column: int, kate_index: int, is_open: bool):
    # left check

    if maze_dict[kate_column][kate_index - 1] == "#":
        # left position is wall
        return maze_dict, is_open
    else:
        # left position is open
        maze_dict[kate_column][kate_index - 1] = 'k'
        maze_dict[kate_column][kate_index] = '#'
        is_open = True
        kate_position = maze_dict[kate_column][kate_index - 1]
        return maze_dict, is_open, kate_position


count = 2
reset = False

row_adder = 1


while True:
    for column in range(1, len(maze_as_dict)):
        for i in range(len(maze_as_dict[column])):
            if maze_as_dict[column][i] == 'k':

                open_top = False
                open_bot = False
                open_right = False
                open_left = False

                info = top_check(maze_as_dict, column, i, open_top)
                maze_as_dict = info[0]
                open_top = info[1]
                # kate_current_position = info[2]
                if open_top:
                    for index_1 in range(len(maze_as_dict[1])):
                        if maze_as_dict[1][index_1] == 'k':
                            print(f"Kate get out in {count} moves")



                info = right_check(maze_as_dict, column, i, open_right)
                maze_as_dict = info[0]
                open_right = info[1]
                # kate_current_position = info[2]
                if open_right:
                    if 'k' == maze_as_dict[column][0] or 'k' == maze_as_dict[column][-1]:
                        print(f"Kate got out in {count} moves")
                        exit()


                info = left_check(maze_as_dict, column, i, open_left)
                maze_as_dict = info[0]
                open_left = info[1]
                # kate_current_position = info[2]
                if open_left:
                    if 'k' == maze_as_dict[column][0] or 'k' == maze_as_dict[column][-1]:
                        print(f"Kate got out in {count} moves")
                        exit()


                info = bot_check(maze_as_dict, column, i, open_bot)
                maze_as_dict = info[0]
                open_bot = info[1]
                # kate_current_position = info[2]
                if open_bot:
                    for index_2 in range(len(maze_as_dict[1])):
                        if maze_as_dict[maze_rows][index_2] == 'k':
                            print(f"Kate got out in {count} moves")
                            exit()

                if open_top:
                    count += 1
                    reset = True
                elif open_bot:
                    count += 1
                    reset = True
                elif open_right:
                    count += 1
                    reset = True
                elif open_left:
                    count += 1
                    reset = True
                else:
                    print(f"Kate cannot get out!")
                    exit()


