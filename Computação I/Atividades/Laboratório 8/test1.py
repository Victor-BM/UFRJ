def multiplica(a, b, c):
    return (a*b*c)

def main():
    media = 0
    lista1 = list(map(multiplica, (1, 2, 3), (4, 5, 6), (7, 8, 9)))
    for i in lista1:
        media += i
    media = media/3
    lista2 = list(filter(lambda x: x > media, lista1))
    print(f'{lista1}\n{media}\n{lista2}')
main()