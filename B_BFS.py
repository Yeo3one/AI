# 상태를 나타내는 클래스
class State:
  def __init__(self, board, goal, depth = 0):
    self.board = board # 현재 상태의 퍼즐 보드
    self.depth = depth # 시작 상태의 깊이
    self.goal = goal # 목표 상태의 퍼즐 보드

  # i1과 i2를 교환하여서 새로운 상태를 반환
  # self를 통해 객체의 속성과 매서드에 접근 가능
  def get_new_board(self, i1, i2, depth):
    new_board = self.board[:]
    new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
    return State(new_board, self.goal, depth)

  # 자식 노드를 확장하여서 리스트에 저장하여서 반환
  def expand(self, depth):
    result = [] # 가능한 모든 자식 노드를 저장할 빈 리스트를 생성
    i = self.board.index(0)	
    if not i in [0, 3, 6] :		# LEFT 
      result.append(self.get_new_board(i, i-1, depth))
    if not i in [0, 1, 2] :		# UP 
      result.append(self.get_new_board(i, i-3, depth))
    if not i in [2, 5, 8]:		# RIGHT 
      result.append(self.get_new_board(i, i+1, depth))
    if not i in [6, 7, 8]:		# DOWN 
      result.append(self.get_new_board(i, i+3, depth))
    return result

  # 객체를 출력할 때 사용
  def __str__(self):
    return str(self.board[:3]) +"\n"+\
    str(self.board[3:6]) +"\n"+\
    str(self.board[6:]) +"\n"+\
    "------------------"

  def __eq__(self, other):			
    return self.board == other.board

  def __ne__(self, other):		
    return self.board != other.board

# 초기 상태
puzzle = [2, 8, 3, 
          1, 6, 4, 
          7, 0, 5]

# 목표 상태
goal = [1, 2, 3, 
        8, 0, 4, 
        7, 6, 5]

# open 리스트
open_queue = [ ]
open_queue.append(State(puzzle, goal))

closed_queue = [ ]
depth = 0

count = 1  
while len(open_queue) != 0: 
  current = open_queue.pop(0)		
  print(count)
  count += 1
  print(current)
  if current.board == goal:
      print("탐색 성공")
      break
  depth = current.depth+1
  closed_queue.append(current)
  if depth > 5 :
      continue
  for state in current.expand(depth):
      if (state in closed_queue) or (state in open_queue):	
          continue			
      else: 
          open_queue.append(state)
          