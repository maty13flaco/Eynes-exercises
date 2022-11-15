from random import randrange


def list_generator():
    return [{"id":i,"edad":randrange(1,100)} for i in range(10)]


def order(ls):
    def by_age(e):
        return e["edad"]
    
    ls.sort(reverse=True, key=by_age)
    return ls


lista = order(list_generator())
print(f'ID Mas joven: {lista[-1]["id"]}')
print(f'ID Mas viejo: {lista[0]["id"]}')
print(f'Ordenada: {lista}')
