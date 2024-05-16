def minimax(node, depth, isMaximizingPlayer, alpha, beta):
    if is_leaf(node):
        return get_node_value(node)
    
    # 현재 플레이어가 최대화하는 플레이어인 경우: -> 가장 좋은 값을 음의 무한대로 초기화
    if isMaximizingPlayer:
        bestVal = float('-inf')
        for child in get_children(node):
            value = minimax(child, depth + 1, False, alpha, beta)
            # 현재 가장 좋은 값과 자식 노드에서 반환된 값 중 더 큰 값 선택
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            # 베타 값이 알파 값보다 작거나 같은 경우 가지치기 수행
            if beta <= alpha:
                break
        return bestVal

    # 현재 플레이어가 최소화하는 플레이어인 경우: ->  가장 좋은 값을 양의 무한대로 초기화
    else:
        bestVal = float('inf')
        for child in get_children(node):
            value = minimax(child, depth + 1, True, alpha, beta)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)
            # 베타 값이 알파 값보다 작거나 같은 경우 가지치기 수ㅇ
            if beta <= alpha:
                break
        return bestVal