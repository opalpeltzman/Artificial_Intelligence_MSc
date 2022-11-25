import pandas as pd
from Ex1_code.internal_functions.ucs import ucs


def save_results(algorithm: str):
    read_from_path = 'problems.csv'
    save_to_path = ''
    data = []
    # data = [[[796317, 796318, 796319], '-', 0.0003333333333333333]]

    if algorithm == 'ucs':
        save_to_path = 'results/UCSRuns.txt'

        df = pd.read_csv(read_from_path, sep=',', header=None)

        # for search_problem in df.values:
        #     path, total_time, run_time = ucs(start=search_problem.item(0), target=search_problem.item(1))
        #     print(path, total_time, run_time)
        #     data.append([path, '-', total_time])

        path, total_time, run_time = ucs(start=796317, target=796319)
        print(path, total_time, run_time)
        data.append([path, '-', total_time])
        print(data)

    elif algorithm == 'A_star':
        pass

    elif algorithm == 'ida':
        pass

    with open(save_to_path, "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(line) + "\n")
