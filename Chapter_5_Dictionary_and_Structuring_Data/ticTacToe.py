chess_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
               'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
               'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
	print(board['top-L'] + '|' +  board['top-M'] + '|' +  board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' +  board['mid-M'] + '|' +  board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' +  board['low-M'] + '|' +  board['low-R'])


turn = 'X'

for i in range(9):

	printBoard(chess_board)
	print('Turn for ' + turn + '. Move on which space')
	move = input()
	chess_board[move] = turn
	if turn == 'X':
		turn = '0'
	else:
		turn = 'X'
print(chess_board)