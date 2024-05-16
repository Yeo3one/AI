game_board = [' ', ' ', ' ',
              ' ', ' ', ' ',
              ' ', ' ', ' ']
              

# 비어 있는 칸을 찾아서 리스트로 반환
def empty_cells(board):
    cells = []
    for x, cell in enumerate(board):
            if cell == ' ':
                cells.append(x)
    return cells

# 비어 있는 칸에 수를 둠
def valid_move(x):
    return x in empty_cells(game_board)

def move(x, player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False

# 현재 게임 보드
def draw(board):
    for i, cell in enumerate(board):
        if i%3 == 0: 
            print('\n----------------')
        print('|', cell , '|', end='')
    print('\n----------------')

# 보드의 상태 평가
def evaluate(board):
    if check_win(board, 'X'):
        score = 1
    elif check_win(board, 'O'):
        score = -1
    else:
        score = 0
    return score

# 1차원 리스트에서 동일한 문자가 수직선이나 수평선, 대각선으로 나타나면 승리🥇
def check_win(board, player):
    win_conf = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conf

def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O')

def minimax(board, depth, maxPlayer):
    pos = -1
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)

    if maxPlayer:
        value = -10000 
        for p in empty_cells(board):
            board[p] = 'X'		# 보드의 p 위치에 'X'

            # 경기자를 교체 후 minimax()를 순환 호출
            x, score = minimax(board, depth-1, False)
            board[p] = ' '	
            if score > value:
                value = score 	
                pos = p		
    else:
        value = +10000  
        for p in empty_cells(board):
            board[p] = 'O'		# 보드의 p 위치에 'O'

            # 경기자를 교체 후 minimax()를 순환호출
            x, score = minimax(board, depth-1, True)
            board[p] =  ' '		
            if score < value:
                value = score 	
                pos = p		
    return pos, value	

player='X'

while True:
    draw(game_board)
    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break
    i, v = minimax(game_board, 9, player=='X')
    move(i, player)
    if player=='X': 
        player='O'
    else: 
        player='X'

if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')