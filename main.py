import checkers as ck
def main():
    try:
        size = int(input('What size board would you like? '))
        board = ck.build_board(size)
        print(board)
        print('Count "Empty": ', ck.get_count(board, 'Empty'))
        print('Count "Red": ', ck.get_count(board, 'Red'))
        print('Count "Black": ', ck.get_count(board, 'Black'))
    except ValueError:
        print('Please input an integer value greater than zero`')
def resized(board):
    try:
        new_size = int(input('Enter new size: '))
        new_board = ck.resize_board(board, new_size)
        print("Here is your new board:")
        print(new_board)
    except ValueError:
        print('Please enter an integer.')

switch = True
while switch == True:
    if __name__ == '__main__':
        current = main()
        while switch == True:
            print('Would you like to resize the board? (y/n)')
            resize_input = input('> ').lower()
            if resize_input == 'y':
                resized_board = resized(current)
                continue
            elif resize_input == 'n':
                break
            else:
                print('Incorrect value given')
                break
        print('<END PROGRAM>')
        break
    else:
        print('file meant to be run as main.')
        break