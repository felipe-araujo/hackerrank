from itertools import combinations
from collections import namedtuple

class Graph:
    def __init__(self):
        self.nodes = dict()

    def add(self, source_destination):
        source, destination = source_destination
        if source not in self.nodes:
            self.nodes[source] = set()
        self.nodes[source].add(destination)

        if destination not in self.nodes:
            self.nodes[destination] = set()
        self.nodes[destination].add(source)
    def __getitem__(self, key):
        return self.nodes[key]

    def keys(self):
        return list(self.nodes.keys())

    def __str__():
        return str(nodes)

def read_input():
    n, q = map(int, input().strip().split())
    sets = []
    graph = Graph()
    for _ in range(n-1):
        pair = map(int, input().strip().split())
        graph.add(pair)

    for _ in range(q):
        size = input()
        sets.append(list(map(int, input().strip().split())))

    return graph, sets

def f(u, v, dist):
    return (u * v * dist) % (1000000000 + 7)

# Distance between nodes u and v from lookup table
def distance(u, v, dist_lookup):
    key = tuple([u, v])
    #print(key)
    return dist_lookup[key]   

class Node:
    def __init__(self, value, adj, cost, pred):
        self.value = value
        self.adj = adj
        self.cost = cost
        self.pred = pred

def dijkstra(s, graph):
    #Node = namedtuple('Node', ['value', 'adj', 'cost','pred'])
    #d = [namedtuple('Node')]
    nodes = set()
    nodes.update(graph.keys())
    #for key in graph.keys():
    #    nodes.update(graph.nodes[key])
    #print(nodes)
    node_pool = {value: Node(value, graph[value], None, None) for value in nodes}
    convert_to_node_obj = lambda value: node_pool[value]
    for node_key in node_pool:
        node = node_pool[node_key]
        node.adj = list(map(convert_to_node_obj, node.adj))
        #node.adj = list(map(convert_to_node_obj, node.adj))

    #nodes.remove(s)
    
    #create_node = lambda value: Node(value, list(map(convert_to_node_obj(graph[value]))), None, None)
    #max = lambda arr
    visited = [node_pool.pop(s)]
    visited[0].cost = 0
    unvisited = list(list(node_pool.values()))
    current = visited.pop() # takes the one element and leaves list empty
    prev_cost = 0
    while current:
        #print(current, current.value, current.cost)
        min_path = prev_cost + 1
        for adj in current.adj:
            if adj.cost and (adj.cost + 1) < prev_cost:
                min_path = adj.cost + 1
        for adj in current.adj:
            adj.cost = min_path            
        current.cost = min_path - 1
        prev_cost = current.cost
        visited.append(current)
        if unvisited:
            current = unvisited.pop()
        else:
            current = None
    #print(visited)
    retval = {tuple([s, dest]): dist for dest, dist in map(lambda n: tuple([n.value, n.cost]), visited)}
    return retval    

def distance_lookup_table(graph):
    distances = dict()
    for source_node in graph.nodes:
        distances.update(dijkstra(source_node, graph))
    return distances


def naive():
    graph, sets = read_input()
    dist_lookup = distance_lookup_table(graph)
    print('\n'.join(map(lambda k: str(k) + ' : ' + str(dist_lookup[k]),dist_lookup)))
    results = []
    for given_set in sets:
        # trivial case
        if len(given_set) == 1:
            results.append(0)
            continue
        
        acc = 0
        for u, v in combinations(given_set, 2):
            delta = distance(u, v, dist_lookup)
            print(u,',', v, ',', 'delta:', delta)
            acc += f(u, v, delta)
        results.append(acc)
    return results


if __name__ == "__main__":
    results = naive()
    print(results)