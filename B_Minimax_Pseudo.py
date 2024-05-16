def minimax(node, depth, maxPlayer):
    # 기본 경우: 깊이가 0이거나 노드가 터미널 노드(종료 상태)인 경우, 노드의 평가 점수를 반환
    if depth == 0 or is_terminal(node):
        return evaluate(node)
    
    # 현재 플레이어가 최대화 플레이어인 경우
    if maxPlayer:
        maxEval = -infinity  # maxEval을 음의 무한대로 초기화
        # 현재 노드의 각 자식 노드를 순회
        for child in node.children:
            # 자식 노드에 대해 깊이를 1 줄이고 최소화 플레이어로서 minimax를 재귀 호출
            eval = minimax(child, depth - 1, False)
            # maxEval을 maxEval과 평가 점수 중 더 큰 값으로 업데이트
            maxEval = max(maxEval, eval)
        return maxEval  # 찾은 최대 평가 점수를 반환
    # 현재 플레이어가 최소화 플레이어인 경우!!
    else:
        minEval = infinity  # minEval을 무한대로 초기화
        # 현재 노드의 각 자식 노드를 순회
        for child in node.children:
            # 자식 노드에 대해 깊이를 1 줄이고 최대화 플레이어로서 minimax를 재귀 호출
            eval = minimax(child, depth - 1, True)
            # minEval을 minEval과 평가 점수 중 더 작은 값으로 업데이트
            minEval = min(minEval, eval)
        return minEval  # 찾은 최소 평가 점수를 반환

# 노드가 터미널 노드(게임 종료 상태)인지 확인하는 함수
def is_terminal(node):
    pass

# 노드(게임 상태)의 점수를 평가하는 함수
def evaluate(node):
    pass

# 노드의 자식 노드(가능한 다음 수)를 가져오는 함수
def get_children(node):
    pass
