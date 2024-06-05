import sys


def get_parent(x, graph):
    if x == graph[x]:
        return x
    graph[x] = get_parent(graph[x], graph)
    return graph[x]


V, E = map(int, input().split())
data = []

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    data.append([c, b, a])
data.sort()

ans, graph = 0, [i for i in range(V + 1)]
for c, a, b in data:
    aP, bP = get_parent(a, graph), get_parent(b, graph)
    if aP != bP:
        graph[bP] = aP
        ans += c

print(ans)
