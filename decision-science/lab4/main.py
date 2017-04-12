#!/usr/bin/env python
from algorithms import FlowNetwork

if __name__ == '__main__':
    # task1
    inp = file('task1.in', 'r')
    g = FlowNetwork('out/task1.md')
    map(g.add_vertex, inp.readline().split())
    m = int(inp.readline())
    for _ in range(m):
        x, y, w = inp.readline().split()
        g.add_edge(x, y, int(w))
    print 'task1 max flow = {}'.format(g.ford_fulkerson('s', 't'))
    g.draw('task1')

    # task2
    inp = file('task2.in', 'r')
    g = FlowNetwork('out/task2.md')
    map(g.add_vertex, inp.readline().split())
    m = int(inp.readline())
    for _ in range(m):
        x, y, w = inp.readline().split()
        g.add_edge(x, y, float(w))
    print 'task2 max flow = {}'.format(g.edmonds_karp('s', 't'))
    g.draw('task2')