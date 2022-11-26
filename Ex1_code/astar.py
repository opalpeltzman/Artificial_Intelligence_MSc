"""
Opal Peltzman
208521385
"""

from ways import load_map_from_csv
from ways.graph import Link
from ways.info import SPEED_RANGES
from ways.tools import compute_distance
import time


class Node:
    def __init__(self, index=None, parent_node=None, g_cost=0, h_cost=0):
        self.index = index
        self.parent_node = parent_node
        self.g_cost = g_cost                # distance between current node and start node
        self.h_cost = h_cost                # estimated distance from current node to the end node
        self.total_cost = g_cost + h_cost   # total cost of the node

    def update_parent_node(self, new_parent_node):
        self.parent_node = new_parent_node

    def update_cost(self, g_cost, h_cost):
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.total_cost = self.g_cost + self.h_cost


def path_cost(s_node: Node, a_node: Link) -> int:
    cost = (a_node.distance / 1000) / SPEED_RANGES[a_node.highway_type][1]
    return s_node.g_cost + cost


def huristic(lat1, lon1, lat2, lon2) -> int:
    return compute_distance(lat1=lat1, lon1=lon1, lat2=lat2, lon2=lon2) / 110


def astar(start, target, roads=None):
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
    opened_dict = {start: Node(index=start, parent_node=None, g_cost=0,
                               h_cost=huristic(lat1=roads[start].lat, lon1=roads[start].lon,
                                               lat2=roads[target].lat, lon2=roads[target].lon))}
    sorted_opened_dict = {k: v for k, v in sorted(opened_dict.items(), key=lambda item: item[1].total_cost)}

    while sorted_opened_dict:
        #  remove and selecting the node with the minimum cost
        selected_node_key = list(sorted_opened_dict.keys())[0]
        selected_node_object = sorted_opened_dict[selected_node_key]
        del sorted_opened_dict[selected_node_key]
        del opened_dict[selected_node_key]

        if selected_node_object.index == target:
            tmp = selected_node_object
            g_time = tmp.total_cost
            while tmp.parent_node is not None:
                path.insert(0, tmp.index)
                tmp = closed_dict[tmp.parent_node]
            path.insert(0, start)
            if not closed_dict:
                h_time = selected_node_object.total_cost
            else:
                h_time = closed_dict[start].total_cost
            # seconds
            end_time = time.time()
            print(f'{path} - {end_time - start_time}')
            # print(path)
            return path, g_time, h_time, end_time - start_time

        closed_dict.update({selected_node_object.index: selected_node_object})
        if roads[selected_node_object.index].links is not None:

            # iterate over current node available paths ('children')
            for link in roads[selected_node_object.index].links:

                # calculating the distance value of link
                g_cost = path_cost(selected_node_object, link)
                h_cost = huristic(lat1=roads[target].lat, lon1=roads[target].lon,
                                  lat2=roads[link.target].lat, lon2=roads[link.target].lon)
                cost = g_cost + h_cost

                if link.target not in closed_dict and link.target not in sorted_opened_dict:
                    child_node = Node(index=link.target, parent_node=link.source, g_cost=g_cost, h_cost=h_cost)
                    opened_dict.update({child_node.index: child_node})
                    sorted_opened_dict = {k: v for k, v in sorted(opened_dict.items(), key=lambda item: item[1].total_cost)}

                elif link.target in sorted_opened_dict and cost < sorted_opened_dict[link.target].total_cost:
                    sorted_opened_dict[link.target].update_parent_node(new_parent_node=link.source)
                    sorted_opened_dict[link.target].update_cost(g_cost=g_cost, h_cost=h_cost)

