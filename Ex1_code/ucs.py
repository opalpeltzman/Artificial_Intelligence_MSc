"""
Opal Peltzman
208521385
"""

from ways import load_map_from_csv
from ways.graph import Link
from ways.info import SPEED_RANGES
import time


class Node:
    def __init__(self, index=None, parent_node=None, cost=None):
        self.index = index
        self.parent_node = parent_node
        # the g cost
        self.cost = cost

    def update_parent_node(self, new_parent_node):
        self.parent_node = new_parent_node

    def update_cost(self, new_cost):
        self.cost = new_cost


def path_cost(s_node: Node, a_node: Link) -> int:
    cost = (a_node.distance / 1000) / SPEED_RANGES[a_node.highway_type][1]
    return s_node.cost + cost


def ucs(start, target, roads=None):
    """
    opened_dict - holds all nodes that were found but not expanded yet
    sorted_opened_dict - opened_list sorted by cost ascending order
    closed_dict - to track nodes we visit already
    """
    path = []
    if not roads:
        roads = load_map_from_csv()

    # seconds
    start_time = time.time()
    closed_dict = {}
    opened_dict = {start: Node(index=start, parent_node=None, cost=0)}
    sorted_opened_dict = {k: v for k, v in sorted(opened_dict.items(), key=lambda item: item[1].cost)}

    while sorted_opened_dict:
        #  remove and selecting the node with the minimum cost

        selected_node_key = list(sorted_opened_dict.keys())[0]
        selected_node_object = sorted_opened_dict[selected_node_key]
        del sorted_opened_dict[selected_node_key]
        del opened_dict[selected_node_key]

        if selected_node_object.index == target:
            tmp = selected_node_object
            total_time = tmp.cost
            while tmp.parent_node is not None:
                path.insert(0, tmp.index)
                tmp = closed_dict[tmp.parent_node]
            path.insert(0, start)
            # seconds
            end_time = time.time()
            print(f'{path}')
            return path, total_time, end_time - start_time

        closed_dict.update({selected_node_object.index: selected_node_object})
        if roads[selected_node_object.index].links is not None:

            # iterate over current node available paths ('children')
            for link in roads[selected_node_object.index].links:

                # calculating the distance value of link
                cost = path_cost(selected_node_object, link)
                if link.target not in closed_dict and link.target not in sorted_opened_dict:
                    child_node = Node(index=link.target, parent_node=link.source, cost=cost)
                    opened_dict.update({child_node.index: child_node})
                    sorted_opened_dict = {k: v for k, v in sorted(opened_dict.items(), key=lambda item: item[1].cost)}

                elif link.target in sorted_opened_dict and cost < sorted_opened_dict[link.target].cost:
                    sorted_opened_dict[link.target].update_parent_node(new_parent_node=link.source)
                    sorted_opened_dict[link.target].update_cost(new_cost=cost)

