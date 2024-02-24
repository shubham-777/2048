import random

import numpy as np
from tabulate import tabulate

start, end = 2, 2048
number_list = [start, ]
while number_list[-1] < end:
    number_list.append(number_list[-1] * 2)


def print_board(board):
    print(tabulate(np.where(board == 0, '', board), tablefmt='fancy_grid'))


def availabel_index(board):
    arr_idx = [0, 1, 2, 3]
    avail_idx = []
    for i in arr_idx:
        for j in arr_idx:
            if board[i, j] == 0:
                avail_idx.append((i, j))
    return avail_idx


def availabel_index_v2(board):
    x_idx, y_idx = np.where(board == 0)
    avail_idx = list(zip(x_idx, y_idx))
    return avail_idx


def choose_idx(board):
    avail_idx = availabel_index_v2(board)
    choice = random.choice(avail_idx)
    return choice


def choose_number():
    return random.choice([2, 4])


def insert_next(board):
    x_idx, y_idx = choose_idx(board)
    # print('loc selected: ', (x_idx, y_idx))
    next_int = choose_number()
    board[x_idx, y_idx] = next_int


def move_board(board, dir):
    row, col = board.shape
    row_range = range(row)
    cell_range = range(col - 1)
    if dir == 's':
        board = board.T
    if dir == 'a':
        board = np.fliplr(board)
    if dir == 'w':
        board = board.T
        board = np.fliplr(board)

    for i in row_range:
        if np.count_nonzero(board[i]) <= 0:
            continue
        # iterate from backwards
        # move all non-zero elements to right end
        for j in range(col - 1, -1, -1):
            if board[i, j] == 0 and np.count_nonzero(board[i][:j + 1]) > 0:
                while board[i, j] == 0:
                    board[i][:j + 1] = np.roll(board[i][:j + 1], 1)

        # flag on adding of two digit skip the next index
        # like 4,4 index (0,1) will become 0,8 (0,1) and skip iteration for index 1
        add_flag = False
        # ignore last element
        for j in cell_range:
            if add_flag:
                add_flag = False
                continue
            if board[i, j] != 0 and board[i, j] == board[i, j + 1]:
                board[i, j + 1] += board[i, j]
                board[i, j] = 0
                add_flag = True

        if np.count_nonzero(board[i]) <= 0:
            continue
        # iterate from backwards
        # move all non-zero elements to right end
        for j in range(col - 1, -1, -1):
            if board[i, j] == 0 and np.count_nonzero(board[i][:j + 1]) > 0:
                while board[i, j] == 0:
                    board[i][:j + 1] = np.roll(board[i][:j + 1], 1)

    if dir == 's':
        board = board.T
    if dir == 'a':
        board = np.fliplr(board)
    if dir == 'w':
        board = board.T
        board = np.fliplr(board)


def take_cmd_input():
    guide_txt = 'Options:\n\tw (UP)    |   s (DOWN)    |   a (LEFT)    |   d (RIGHT)\n\tx (EXIT)'
    x = input(guide_txt)
    while x.strip().lower() not in ['w', 's', 'a', 'd', 'x']:
        print('Plz, select supported options only.')
        x = input(guide_txt)
    return x.strip().lower()


matrix_size = 4
metrix = np.zeros((matrix_size, matrix_size), dtype=int)
# metrix = np.array([2, 0, 2, 0, 0, 16, 0, 4, 0, 8, 2, 0, 0, 0, 4, 2]).reshape((4, 4))
print(f"Lets go with:", )
insert_next(metrix)
print_board(metrix)
while True:
    ip = take_cmd_input()
    if ip == 'x':
        break
    move_board(board=metrix, dir=ip)
    insert_next(metrix)
    print_board(metrix)
