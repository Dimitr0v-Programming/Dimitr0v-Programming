maze_as_dict = {

    1: ['#', '#', '#', '#', ' ', '#'],
    2: ['#', '#', ' ', ' ', 'k', '#'],
    3: {'#', '#', ' ', '#', '#', '#'},
    4: ['#', '#', ' ', '#', '#', '#']
}

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


def position_check(maze_dict: dict, kate_column: int, kate_index: int):
    # top check
    if maze_dict[kate_column + 1][kate_index] == "#":
        pass
    else:
        maze_dict[kate_column][kate_index].replace(maze_dict[kate_column][kate_index], "#")


for column in range(1, len(maze_as_dict)):
    for i in range(len(maze_as_dict[column])):
        if maze_as_dict[column][i] == 'k':
            position_check(maze_as_dict, column, i)
