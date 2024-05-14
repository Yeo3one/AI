class State:
  def __init__(self, board, goal, depth = 0):
    self.board = board
    self.depth = depth
    self.goal = goal
 
  def get_new_board(self, i1, i2, depth):
    new_board = self.board[:]
    new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
    return State(new_board, self.goal, depth)

  def expand(self, depth):
    result = []
    if depth > 5: return result		
    i = self.board.index(0)	
    if not i in [0, 3, 6] :		
      result.append(self.get_new_board(i, i-1, depth))
    if not i in [0, 1, 2] :		
      result.append(self.get_new_board(i, i-3, depth))
    if not i in [2, 5, 8]:	
      result.append(self.get_new_board(i, i+1, depth))
    if not i in [6, 7, 8]:	
      result.append(self.get_new_board(i, i+3, depth))
    return result

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
  for state in reversed(current.expand(depth)):  # 앞까지 BFS와 똑같음, reserved가 되면서 순서를 반대로 함
      if (state in closed_queue) or (state in open_queue):	
          continue				# 이미 거쳐간 노드 버림
      else: 
          open_queue.insert(0, state)	
          # BFS -> open_queue.append(state)
          # OPEN 리스트의 첫 부분에 추가