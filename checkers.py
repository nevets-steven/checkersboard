from numpy import random, count_nonzero, repeat, resize

if __name__ != '__main__':

    def build_board(size):
        cells = ['Empty', 'Black', 'Red']
        board = random.choice(cells, size=(size,size))
        return board

    def get_count(board, search):
        count = count_nonzero(board==search)
        return count

    def resize_board(board, new_size):
        new_board = resize(board, (new_size,new_size))
        return new_board


# board = build_board(4)
# print(board)
# new_size = int(input('Enter new size: '))
# new_board = resize_board(board, new_size)
# print(new_board)

else:
    print('File not meant to be run as main')


