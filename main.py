from typing import Dict


class Node:
    def __init__(self, name: int, generate: int=None):
        self.name_id = name
        self.neighbor = {}  # type: Dict[int, float]
        self.visit = False
        self.generate = generate
        self.number_input_edges = 0

    def __str__(self):
        label = f'LAB{self.name_id} ' if self.number_input_edges > 1 else ''
        res = (
            f'{label}QUEUE QD{self.name_id}\n'
            f'SEIZE DD{self.name_id}\n'
            f'DEPART QD{self.name_id}\n'
            f'ADVANCE 1{self.name_id}\n'
            f'RELEASE DD{self.name_id}'
        )
        if self.name_id == 8:
            if len(self.neighbor) > 0:
                res += (
                    f'\nTRANSFER .{int(list(self.neighbor.values())[0]*10)},'
                    f',LAB{list(self.neighbor.keys())[0]}')
            res += '\nTERMINATE'
        return res

    def add_neighbor(self, neighbor, weight=1):
        self.neighbor[neighbor] = weight


class Graph:
    def __init__(self):
        self.vertex_list = {}  # type: Dict[int, Node]

    def add_vertex(self, item, generate=None):
        self.vertex_list[item] = Node(item, generate)

    def add_edge(self, first, second, weight):
        if first not in self.vertex_list:
            self.add_vertex(first)
        if second not in self.vertex_list:
            self.add_vertex(second)
        self.vertex_list[first].add_neighbor(second, weight)
        self.vertex_list[second].number_input_edges += 1

    def all_visit(self):
        for i in self.vertex_list:
            if not self.vertex_list[i].visit:
                return False
        return True

    def __contains__(self, item):
        return item in self.vertex_list

    def __iter__(self):
        return iter(self.vertex_list.values())

    def unvisited(self):
        return [k for k in self.vertex_list if not self.vertex_list[k].visit]


g = Graph()

with open('ver3.txt') as file:
    for line in file:
        if not line.strip():
            break
        tmp = line.split()
        g.add_vertex(int(tmp[0]), int(tmp[1]))

    for line in file:
        tmp = [
            type_(i.strip())
            for type_, i in zip((int, float, int), line.split(','))
        ]
        g.add_edge(tmp[0], tmp[2], tmp[1])

current_vertex = g.vertex_list[1]

code_lines = list()
code_lines.append('SIMULATE')

while not g.all_visit():
    if current_vertex.generate is not None:
        code_lines.append(f'GENERATE {current_vertex.generate}')

    code_lines.extend(str(current_vertex).split('\n'))
    current_vertex.visit = True

    if len(current_vertex.neighbor) == 0:
        # if vertex is last then take first unvisited vertex
        current_vertex = g.vertex_list[g.unvisited()[0]]
        continue

    # index of one from neighbors
    next_vertex = list(current_vertex.neighbor.keys())[0]
    if len(current_vertex.neighbor) == 1 and len(g.unvisited()) == 0:
        s = f'TRANSFER ,LAB{next_vertex}'
        code_lines.append(s)
    if len(current_vertex.neighbor) > 1:
        # index of other neighbor
        t_vertex = list(current_vertex.neighbor.keys())[1]

        if g.vertex_list[next_vertex].visit:
            tmp = t_vertex
            t_vertex = next_vertex
            next_vertex = tmp

        s = f'TRANSFER .{int(current_vertex.neighbor[t_vertex]*10)},'

        if g.vertex_list[next_vertex].visit:
            s += f'LAB{next_vertex}'
        s += f',LAB{t_vertex}'

        code_lines.append(s)

        if g.vertex_list[t_vertex].visit and g.vertex_list[next_vertex].visit:
            current_vertex = g.vertex_list[g.unvisited()[0]]
            continue

    current_vertex = g.vertex_list[next_vertex]

end_code = ['GENERATE 100', 'TERMINATE 1', 'START 1', 'END']
code_lines.extend(end_code)

with open('ver_code3.txt', 'w') as file:
    for line_code in code_lines:
        count = 3
        if 'LAB' in line_code and 'QUEUE' in line_code:
            count = 2
        if line_code == 'SIMULATE' or line_code == 'END':
            count = 2

        if 'GENERATE' in line_code or 'QUEUE' in line_code:
            file.write('\n')

        file.write(f'{" "*count}{line_code}\n')
