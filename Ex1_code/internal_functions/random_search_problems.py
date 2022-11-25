from Ex1_code.ways.graph import load_map_from_csv
import numpy as np


def create_random_search_problems():

    rng = np.random.default_rng()
    start_junctions = rng.choice(944799, size=100, replace=False)
    search_problem_lengths = np.random.randint(low=5, high=19, size=100)

    roads = load_map_from_csv()
    search_problems_array = np.array([])
    route = []

    for index, start_junction in enumerate(start_junctions):
        route.append(start_junction)
        current_junction = start_junction

        while len(route) < search_problem_lengths[index]:
            print(len(roads[current_junction].links))
            random_link = np.random.randint(low=0, high=len(roads[current_junction].links) + 1, size=1)
            print(roads[current_junction].links[random_link[0]])
            current_junction = (roads[current_junction].links[random_link[0]]).target
            route.append(current_junction)

        search_problems_array = np.append([start_junction, current_junction])

