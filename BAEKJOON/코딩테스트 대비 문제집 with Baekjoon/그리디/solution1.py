board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

print(board if 'X' not in board else -1)