import pandas as pd
from ways import load_map_from_csv
from ucs import ucs


def save_results(algorithm: str):
    roads = load_map_from_csv()
    read_from_path = 'problems.csv'
    save_to_path = ''
    data = []

    if algorithm == 'ucs':
        save_to_path = 'results/UCSRuns.txt'

        df = pd.read_csv(read_from_path, sep=',', header=None)

        for search_problem in df.values:
            path, total_time, run_time = ucs(start=search_problem.item(0), target=search_problem.item(1), roads=roads)
            path = ' '.join(map(str, path))
            total_time = f'{total_time:.5f}'[:-1]

            print(path, total_time, run_time)
            data.append([path, '-', total_time])

    elif algorithm == 'astar':
        pass

    elif algorithm == 'ida':
        pass

    with open(save_to_path, "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(line) + "\n")
