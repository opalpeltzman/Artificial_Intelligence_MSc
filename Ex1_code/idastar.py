"""
Opal Peltzman
208521385
"""

from ways import load_map_from_csv
from astar import Node, path_cost, huristic
import time

path = []
found_goal = False
limits = []


def idastar(start, target, roads=None) -> tuple:
    global limits
    global path
    global found_goal
    found_goal = False
    path = []

    if not roads:
        roads = load_map_from_csv()

    start_time = time.time()
    visited = {}

    start_node = Node(index=start, parent_node=None, g_cost=0, h_cost=huristic(lat1=roads[start].lat, lon1=roads[start].lon,
                                                                               lat2=roads[target].lat, lon2=roads[target].lon))
    new_limit = 10000000
    f_limit = start_node.total_cost
    while not found_goal:
        new_limit = dfs_with_limit(node=start_node, target=target, f_limit=f_limit, new_limit=new_limit, visited=visited, roads=roads)
        f_limit = new_limit
        visited = {}
        limits = []

    end_time = time.time()
    print(f'{path}')
    return path, (end_time - start_time)


def dfs_with_limit(node: Node, target, f_limit, new_limit, visited: dict, roads):
    global found_goal
    global limits
    global path

    if node.index == target:
        tmp = node

        while tmp.parent_node is not None:
            path.insert(0, tmp.index)
            tmp = visited[tmp.parent_node]
        path.insert(0, tmp.index)
        found_goal = True
        return new_limit

    if node.index not in visited:
        visited.update({node.index: node})

        if roads[node.index].links is not None:

            # iterate over current node available paths ('children')
            for link in roads[node.index].links:
                if link.target not in visited:
                    g_cost = path_cost(node, link)
                    h_cost = huristic(lat1=roads[target].lat, lon1=roads[target].lon,
                                      lat2=roads[link.target].lat, lon2=roads[link.target].lon)
                    cost = g_cost + h_cost

                    if cost <= f_limit:
                        new_node = Node(index=link.target, parent_node=link.source, g_cost=g_cost, h_cost=h_cost)
                        dfs_with_limit(node=new_node, target=target, f_limit=f_limit, new_limit=new_limit, visited=visited, roads=roads)
                    else:
                        limits.append(cost)
    if not limits:
        new_limit = new_limit
    else:
        new_limit = min(limits)
    return new_limit
