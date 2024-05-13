# 깊이 우선 탐색 (DFS)
# open 리스트는 아직 탐색하지 않은 노드들을 저장하고, 
# closed 리스트는 이미 탐색한 노드들을 저장
# DFS 알고리즘은 open 리스트에서 첫 번째 노드를 선택하고, 
# 해당 노드를 closed 리스트에 추가 후 선택한 노드의 인접 노드들을 open 리스트에 추가

open = [A]; closed = []
open = [B, C]; closed = [A]
open = [C, D, E]; closed = [B, A]
open = [D, E, F, G]; closed = [C, B, A]
open = [E, F, G, H, I]; closed = [D, C, B, A]
open = [F, G, H, I]; closed = [E, D, C, B, A]
open = [G, H, I, U]; closed = [F, E, D, C, B, A]
open = [H, I, U]; closed = [G, F, E, D, C, B, A]
open = [I, U]; closed = [H, G, F, E, D, C, B, A]
open = [I, U]; closed = [H, G, F, E, D, C, B, A]
open = [U]; closed = [I, H, G, F, E, D, C, B, A]

