"""
Opal Peltzman
208521385
"""

import pandas as pd
from ways import load_map_from_csv
from ucs import ucs
from astar import astar
from idastar import idastar
import matplotlib.pyplot as plt
from ways.draw import plot_path


def create_2d_graph(x: list, y: list):
    plt.scatter(x, y)
    plt.xticks([1, 11, 21, 31])
    # plt.yticks([2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42])
    plt.yticks([1, 11, 21, 31, 41])
    plt.xlabel('Heuristic Time')
    plt.ylabel('Real Time')
    plt.title('Heuristic function VS Real Time')
    plt.show()


def save_results(algorithm: str):
    roads = load_map_from_csv()
    read_from_path = 'problems.csv'
    df = pd.read_csv(read_from_path, sep=',', header=None)
    save_to_path = ''
    data = []
    average_run_time = []

    if algorithm == 'ucs':
        save_to_path = 'results/UCSRuns.txt'

        for search_problem in df.values:
            path, total_time, run_time = ucs(start=search_problem.item(0), target=search_problem.item(1), roads=roads)
            path = ' '.join(map(str, path))
            total_time = f'{total_time:.5f}'[:-1]

            data.append([path, '-', total_time])
            average_run_time.append(run_time)

    elif algorithm == 'astar':
        save_to_path = 'results/AStarRuns.txt'
        heuristic_time_x_axis = []
        g_time_y_axis = []

        for search_problem in df.values:
            path, g_time, h_time, run_time = astar(start=search_problem.item(0), target=search_problem.item(1), roads=roads)
            path = ' '.join(map(str, path))
            g_time = f'{g_time:.5f}'[:-1]
            h_time = f'{h_time:.5f}'[:-1]

            data.append([path, '-', g_time, '-', h_time])
            average_run_time.append(run_time)

            heuristic_time_x_axis.append(h_time)
            g_time_y_axis.append(g_time)
        create_2d_graph(x=heuristic_time_x_axis, y=g_time_y_axis)

    elif algorithm == 'idastar':
        search_problems = [
                            [670998, 670991], [576620, 773660], [11225, 68760], [151098, 151093], [23469, 538180],
                            [601373, 601341], [514991, 514964], [744898, 744895], [445729, 445726], [324382, 324379]
                           ]

        for problem in search_problems:
            path, run_time = idastar(start=problem[0], target=problem[1], roads=roads)
            plot_path(roads=roads, path=path)
            average_run_time.append(run_time)

    if algorithm != 'idastar':
        with open(save_to_path, "w") as txt_file:
            for line in data:
                txt_file.write(" ".join(line) + "\n")

    print(f'{algorithm} average run time- {(sum(average_run_time) / len(average_run_time)): .10f}')
