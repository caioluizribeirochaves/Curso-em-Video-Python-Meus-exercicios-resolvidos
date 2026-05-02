def valores(lst):
    pos = 0
    while pos < len(lst):
        print(lst[pos] * 2, end=' ')
        pos += 1


valores([1, 2, 3, 4, 5])


def soma(* valores):
    s = 0
    for v in valores:
        s += v
    print(f'\nA soma dos valores {valores} é {s}')


soma(5, 6, 7, 8)

