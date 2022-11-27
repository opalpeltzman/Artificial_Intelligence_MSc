'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.

Opal Peltzman
208521385

'''

#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions

from astar import huristic, astar
from ucs import ucs
from save_results import save_results
from random_search_problems import create_random_search_problems
from idastar import idastar


def huristic_function(lat1, lon1, lat2, lon2):
    huristic(lat1=lat1, lon1=lon1, lat2=lat2, lon2=lon2)


def find_ucs_rout(source, target):
    """
     @param source: int type that represents node index
     @param target: int type that represents node index
    """
    'call function to find path, and return list of indices'
    ucs(start=source, target=target)


def find_astar_route(source, target):
    'call function to find path, and return list of indices'
    astar(start=source, target=target)


def find_idastar_route(source, target):
    'call function to find path, and return list of indices'
    idastar(start=source, target=target)
    

def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv
    # dispatch(argv)

    """
    create 100 random search problems. 
    uncomment to run
    """
    # create_random_search_problems()

    """
        run UCS algorithm on a specific search problem.
        problems available at 'problems.txt'
        uncomment to run
    """
    # find_ucs_rout(source=52830, target=52834)

    """
        run UCS algorithm on all 100 problems from 'problems.txt'
        and save results to results/UCSRuns.txt.
        uncomment to run
    """
    # save_results(algorithm='ucs')

    """
        run astar algorithm on a specific search problem.
        problems available at 'problems.txt'
        uncomment to run
    """
    # find_astar_route(source=52830, target=52834)

    """
        run A* algorithm on all 100 problems from 'problems.txt'
        and save results to results/AStarRuns.txt. show scatter plot representing
        huristic time VS real time.
        uncomment to run
    """
    # save_results(algorithm='astar')

    """
        run idastar algorithm on a specific search problem.
        problems available at 'problems.txt'
        uncomment to run
    """
    # find_idastar_route(source=514991, target=514964)

    """
        run idastar algorithm on 10 problems from 'problems.txt'
        and create map using draw.plot_path
        uncomment to run
    """
    # save_results(algorithm='idastar')
