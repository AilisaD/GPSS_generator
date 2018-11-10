from collections import Counter
import queue


class Node:
    def __init__(self, name):
        self.name_id = name
        self.neighbor_list = {}
        self.visit = False

#    def __str__(self):
#        return str(self.name_id) + ' connectedTo: ' + str([x.name_id for x in self.neighbor_list])
#    def __str__(self):
#        res = f'  OUEUE QD{self.name_id:.0f}\n'\
#              f'  SEIZE DD{self.name_id:.0f}\n' \
#              f'  DEPART QD{self.name_id:.0f}\n' \
#              f'  ADVANCE 1{self.name_id:.0f}\n' \
#              f'  RELEASE DD{self.name_id:.0f}\n'
#        return res

    def add_neighbor(self, neighbor, weight=1):
        self.neighbor_list[neighbor] = weight


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.size = 0

    def add_vertex(self, item):
        self.size += 1
        self.vertex_list[item] = Node(item)

    def add_edge(self, first, second, weight):
        if first not in self.vertex_list:
            self.add_vertex(first)
        if second not in self.vertex_list:
            self.add_vertex(second)
        self.vertex_list[first].add_neighbor(second, weight)

    def all_visit(self):
        for i in self.vertex_list:
            if not self.vertex_list[i].visit:
                return False
        return True

    def __contains__(self, item):
        return item in self.vertex_list

    def __iter__(self):
        return iter(self.vertex_list.values())


g = Graph()

with open('ver8.txt') as file:
    for line in file:
        tmp = [float(i.strip()) for i in line.split(',')]
        g.add_edge(tmp[0], tmp[2], tmp[1])

stack = queue.LifoQueue()





def main():
    graph = []
    with open('ver8.txt') as f:
        for l in f:
            graph.append([float(i) for i in l.split(', ')])
    result = ' SIMULATE\n'
    generate_transacts = [10, 20, 10]
    output_paths = Counter([graph[i][0] for i in range(len(graph))])
    entrance_paths = Counter([graph[i][2] for i in range(len(graph))])
    start = list(set(output_paths) - set(entrance_paths))
    num_node = 0
    points_entrance = 0
    flag = True

    while points_entrance != 3:
        if flag:
            result += f'  GENERATE {generate_transacts[points_entrance]}\n'
            points_entrance += 1
            flag = False

        if entrance_paths[graph[num_node][0]] < 2:
            result += f'  OUEUE QD{graph[num_node][0]}\n'
        else:
            result += f'LAB{graph[num_node][0]} OUEUE QD{graph[num_node][0]}\n'\
                      f'  SEIZE DD{graph[num_node][0]}\n' \
                      f'  DEPART QD{graph[num_node][0]}\n' \
                      f'  ADVANCE 1{graph[num_node][0]}\n' \
                      f'  RELEASE DD{graph[num_node][0]}\n'

        if output_paths[graph[num_node][0]] > 1:
            result += f'  TRANSFER {graph[num_node + 1][1]}' \
                      f',,LAB{graph[num_node + 1][2]}\n'

        if graph[num_node][0] == 8:
            result += '  TERMINATE\n'
            flag = True
            num_node = [graph[i][0] for i in range(len(graph))].index(start[points_entrance])
        else:
            num_node = [graph[i][0] for i in range(len(graph))].index(graph[num_node][2])
    result += '  GENERATE 100\n' \
              '  TERMINATE 1\n' \
              '  START 1\n' \
              ' END'
    print(result)
