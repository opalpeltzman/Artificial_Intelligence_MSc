'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''

from collections import namedtuple, Counter
from ways import load_map_from_csv


def branching_factor(links: tuple, max_links: int, min_links: int, number_links: int) -> dict:
    """
        @param links: a tuple of Link Class
        @param max_links: max links
        @param min_links: min links
        @param number_links: sum the number of links appears in Roads
    """
    link_count = len(links)
    number_links += link_count
    max_links = link_count if link_count > max_links else max_links
    min_links = link_count if link_count < min_links else min_links

    return {'max': max_links, 'min': min_links, 'Number_of_links': number_links}


def distance_factor(links: tuple, max_dist: int, min_dist: int, dist_count: int) -> tuple:
    """
    @param links: a tuple of Link Class
    @param max_dist: max distance
    @param min_dist: min distance
    @param dist_count: sum of all distance param in Link objects appears in Roads
    """

    highway_type_list = []

    if links is not None:
        for link in links:
            dist_count += link.distance
            max_dist = link.distance if link.distance > max_dist else max_dist
            min_dist = link.distance if link.distance < min_dist else min_dist

            highway_type_list.append(link.highway_type)

        return {'max': max_dist, 'min': min_dist, 'dist_count': dist_count}, highway_type_list


def info_extract(roads) -> dict:
    links_info = {'max': 0, 'min': 100, 'Number_of_links': 0}
    links_distance = {'max': 0, 'min': 100, 'dist_count': 0}
    highway_type_list = []

    for road in roads.items():
        links_info = branching_factor(links=road[1].links, max_links=links_info['max'], min_links=links_info['min'], number_links=links_info['Number_of_links'])
        links_distance, temp_highway_type_list = distance_factor(links=road[1].links, max_dist=links_distance['max'], min_dist=links_distance['min'], dist_count=links_distance['dist_count'])

        highway_type_list.extend(temp_highway_type_list)

    return {'links': links_info, 'distance': links_distance, 'highway_type': highway_type_list}


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])

    info = info_extract(roads=roads)

    return {
        'Number of junctions': len(roads.keys()),
        'Number of links': info['links']['Number_of_links'],
        'Outgoing branching factor': Stat(max=info['links']['max'], min=info['links']['min'], avg=(info['links']['Number_of_links']) / len(roads.keys())),
        'Link distance': Stat(max=info['distance']['max'], min=info['distance']['min'], avg=(info['distance']['dist_count']) / info['links']['Number_of_links']),
        # value should be a dictionary
        # mapping each info.ROAD_TYPES to the no' of links of this type
        'Link type histogram': Counter(info['highway_type'])  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))

        
if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()

