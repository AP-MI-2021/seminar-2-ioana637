'''
subsecvența
ex: sir [1,2,3,4,5,6,7]
subsecventa: [3,4,5]
'''

def nr_div_10(nr):
    '''
    Verifica ca nr sa fie divizbil cu 10
    :param nr: nr intreg
    :return: True daca nr e divizibil cu 10, False altfel
    '''
    return nr % 10 == 0

def test_nr_div_10():
    assert nr_div_10(130) == True
    assert nr_div_10(13) == False



def list_elem_div_10(lista):
    '''
    Verificam ca lista are doar elemente cu propr. div 10
    :param lista: lista de nr intregi
    :return: True daca lista are are doar elem div 10, False altfel
    '''
    for x in lista:
        if not nr_div_10(x):
            return False
    return True

def test_list_elem_div_10():
    assert list_elem_div_10([]) == True
    assert list_elem_div_10([10, 30, 50]) == True
    assert list_elem_div_10([10, 3, 50]) == False
    assert list_elem_div_10([1, 3, 5]) == False



def determinare_cea_mai_lunga_secv_v2(lista):
    '''
    Determinarea secventa cea mai lunga cu prop ca nr sunt divizibile cu 10
    :param lista: lista de nr intregi
    :return: rez lista care reprezinta secventa de lungime maxima
    cu prop ca nr sunt divizibile cu 10
    '''
    rez = []
    lung_lista = len(lista)
    for i in range(lung_lista):
        for j in range(i, lung_lista):
            list_de_verificat = lista[i:j+1]
            if list_elem_div_10(list_de_verificat) and len(list_de_verificat) > len(rez):
                rez = list_de_verificat[:]
    return rez



def test_determinare_cea_mai_lunga_secv_v2():
    assert determinare_cea_mai_lunga_secv_v2([]) == []
    assert determinare_cea_mai_lunga_secv_v2([1, 2, 20, 50, 70, 3, 34]) == [20, 50, 70]
    assert determinare_cea_mai_lunga_secv_v2([1, 2, 20, 50, 3, 70, 3, 34]) == [20, 50]
    assert determinare_cea_mai_lunga_secv_v2([1, 2, 20, 50, 3, 70, 340, 100, 50]) == [70, 340, 100, 50]



def determinare_cea_mai_lunga_secv(lista):
    '''
    Determinarea secventa cea mai lunga cu prop ca nr sunt divizibile cu 10
    :param lista: lista de nr intregi
    :return: rez lista care reprezinta secventa de lungime maxima
    cu prop ca nr sunt divizibile cu 10
    '''
    rez = []  # rezultatul final
    temp = []  # solutia curenta
    for x in lista:  # foreach
        if nr_div_10(x):
            temp.append(x)
        else:
            if (len(temp) > len(rez)):
                rez = temp[:]
            temp.clear()
    if (len(temp) > len(rez)):
        rez = temp[:]
    return rez


def test_determinare_cea_mai_lunga_secv():
    assert determinare_cea_mai_lunga_secv([]) == []
    assert determinare_cea_mai_lunga_secv([1, 2, 20, 50, 70, 3, 34]) == [20, 50, 70]
    assert determinare_cea_mai_lunga_secv([1, 2, 20, 50, 3, 70, 3, 34]) == [20, 50]
    assert determinare_cea_mai_lunga_secv([1, 2, 20, 50, 3, 70, 340, 100, 50]) == [70, 340, 100, 50]



def teste():
    test_nr_div_10()
    test_list_elem_div_10()
    test_determinare_cea_mai_lunga_secv()
    test_determinare_cea_mai_lunga_secv_v2()

teste()