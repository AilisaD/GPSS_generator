from collections import Counter

graph1 = [
    [1, 0.6, 4], [1, 0.4, 5],
    [2, 0.5, 5], [2, 0.5, 6],
    [3, 1, 6],
    [4, 0.6, 5], [4, 0.4, 8],
    [5, 1, 8],
    [6, 0.8, 7], [6, 0.2, 8],
    [7, 0.7, 8], [7, 0.3, 4],
    [8, 0.3, 6]
]

graph = [
    [1, 0.8, 7], [1, 0.2, 5],
    [2, 0.5, 4], [2, 0.5, 5],
    [3, 0.7, 4], [3, 0.3, 6],
    [4, 0.5, 6], [4, 0.5, 7],
    [5, 1, 7],
    [6, 0.9, 8], [6, 0.1, 4],
    [7, 0.6, 6], [7, 0.4, 8],
    [8, 1, 9]
]

print(' SIMULATE')

gen = [10, 20, 10]

output_paths = Counter([graph[i][0] for i in range(len(graph))])
entrance_paths = Counter([graph[i][2] for i in range(len(graph))])
start = list(set(output_paths) - set(entrance_paths))

num_node = 0
c = 0
flag = True

while c != 3:
    if flag:
        print(f'  GENERATE {str(gen[c])}')
        c += 1
        flag = False

    if entrance_paths[graph[num_node][0]] < 2:
        print(f'  OUEUE QD{str(graph[num_node][0])}')
    else:
        print(f'LAB{str(graph[num_node][0])} OUEUE QD{str(graph[num_node][0])}')

    print(f'  SEIZE DD{str(graph[num_node][0])}\n'
          f'  DEPART QD{str(graph[num_node][0])}\n'
          f'  ADVANCE 1{str(graph[num_node][0])}\n'
          f'  RELEASE DD{str(graph[num_node][0])}')
    if output_paths[graph[num_node][0]] > 1:
        print(f'  TRANSFER {str(graph[num_node + 1][1])}'
              f',,LAB{str(graph[num_node + 1][2])}')

    if graph[num_node][0] == 8:
        print('  TERMINATE')
        flag = True
        num_node = [graph[j][0] for j in range(len(graph))].index(start[c])
    else:
        num_node = [graph[j][0] for j in range(len(graph))].index(graph[num_node][2])

print('  GENERATE 100\n'
      '  TERMINATE 1\n'
      '  START 1\n'
      ' END')
