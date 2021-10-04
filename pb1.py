def is_prime(n):
    '''
    Verifica n nr prim
    :param n: nr intreg
    :return: True daca n este prim si False, altfel
    '''
    if (n<2):
        return False
    if (n>2 and n%2 == 0):
        return False
    for d in range(3, n//2 + 1, 2):
        if n % d == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(13) == True
    assert is_prime(2) == True
    assert is_prime(-5) == False
    assert is_prime(0) == False
    assert is_prime(10) == False
    assert is_prime(4) == False

test_is_prime()

def elem_prime(lista):
    '''
    Se creeaza o lista cu nr prime din lista list
    :param lista: lista de nr intregi
    :return: list cu nr prime din lista initiala
    '''
    rez = []
    # for i in range(len(lista)):
    for x in lista:
        if is_prime(x):
            rez.append(x)
    return rez

def test_elem_prime():
    assert elem_prime([])==[]
    assert elem_prime([2, 7, 13])==[2,7,13]
    assert elem_prime([2,6, 9, 101])==[2,101]
    assert elem_prime([6, 9])==[]

test_elem_prime()

def show_menu():
    print('''
    1. Citire lista
    2. Afisare numere prime
    x. Iesire
    ''')

def read_list():
    lista = []
    n = int(input("Introduceti numarul de elem din lista"))
    for i in range(n):
        x = int(input("a[{}]=".format(i+1)))
        lista.append(x)
    return lista

def run_UI():  #main
    lista = []
    while True:
        show_menu()
        cmd = input("Comanda:")
        if cmd == '1':
            lista = read_list()
        else:
            if cmd == '2':
                list_nr_prime = elem_prime(lista)
                print(list_nr_prime)
            elif cmd == 'x':
                break
            else:
                print("Comanda invalida")

                
run_UI()

