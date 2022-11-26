'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions

from astar import huristic, astar
from ucs import ucs


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
    raise NotImplementedError
    

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

    # random_search_problems.create_random_search_problems()
    find_ucs_rout(source=52830, target=52834)
    # save_results.save_results(algorithm='ucs')
    find_astar_route(source=52830, target=52834)
    # save_results.save_results(algorithm='astar')
