from random import randrange
import doctest


def list_generator():
    """This function generate a list with ten dictionaries.
    Each dictionary has an Id and Age.

    Returns:
        list: List whit ten dictionaries
    """
    return [{"id":i,"edad":randrange(1,100)} for i in range(10)]


def order(ls):
    '''This function sorts dictionaries according to age.

    Args:
        ls (list): List with dictionaries.

    Examples:
    >>> order([{"id": 1, "edad":25}, {"id":2,"edad":14}, {"id":3,"edad":55}])
    [{'id': 3, 'edad': 55}, {'id': 1, 'edad': 25}, {'id': 2, 'edad': 14}]
    >>> order([{"id": 1, "edad":12}, {"id":2,"edad":14}, {"id":3,"edad":2}])
    [{'id': 2, 'edad': 14}, {'id': 1, 'edad': 12}, {'id': 3, 'edad': 2}]
    '''
    def by_age(e):
        return e["edad"]
    
    ls.sort(reverse=True, key=by_age)
    return ls


lista = order(list_generator())
print(f'ID Mas joven: {lista[-1]["id"]}')
print(f'ID Mas viejo: {lista[0]["id"]}')
print(f'Ordenada: {lista}')

if __name__ == "__main__":
    doctest.testmod()