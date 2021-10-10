# Problema 7
# Functia care verifica un numar daca este antipalindrom
def is_antipalindrome(n):
    """
    Verificam daca n este antipalindromic
    :param n: numar intreg
    :return: True sau False
    """
    lista = []
    while n > 0:
        lista.append(n % 10)
        n //= 10
    i = 0
    k = len(lista) - 1
    while i < k:
        if lista[i] == lista[k]:
            return False
        i = i + 1
        k = k - 1
    return True


# Functia de test pentru is_palindrome
def test_is_antipalindrome(n):
    assert is_antipalindrome(2773) is False
    assert is_antipalindrome(2783) is True
    assert is_antipalindrome(1223) is False
    assert is_antipalindrome(664) is True
    if is_antipalindrome(n) is True:
        return "Numarul introdus este antipalindrom"
    return "Numarul introdus nu este antipalindrom"


# Problema 8
def get_base_2(n):
    """
    Transformam un numar din baza 10 in baza 2
    :param n: numar intreg
    :return: string
    """
    lista = []
    while n > 0:
        lista.append(n % 2)
        n = n // 2
    lista.reverse()
    listToStr = ''.join([str(elem) for elem in lista])
    return listToStr

# Functia de test pentru problema 8
def test_get_base_2(n):
    assert get_base_2(3) == 11
    assert get_base_2(7) == 111

# meniu
def menu():
    print("1. Verifica daca numarul n este antipalindrom")
    print("2. Transforma un numar n, din baza 10, in baza 2")


menu()
option = int(input("Introduceti optiunea dumneavoastra: "))

while option != 0:
    if option == 1:
        n = int(input("Introduceti n = "))
        print(test_is_antipalindrome(n))
        print()
    elif option == 2:
        n = int(input("Introduceti n = "))
        print("Numarul convertit in baza 2 este: " , get_base_2(n))
        print()
    if option == 1 or option == 2:
        a = input("Doriti sa mai introduceti optiuni? ")
        if a == "DA" or a == "da" or a == "Da" or a == "dA":
            print()
            menu()
            option = int(input("Introduceti optiunea dumneavoastra: "))
            print()
        elif a == "NU" or a == "nu" or a == "Nu" or a == "nU":
            break
        else:
            print()
            print("Raspundeti cu DA sau NU")
            print()
            a = input("Doriti sa mai introduceti optiuni? ")
            if a == "DA" or a == "da" or a == "Da" or a == "dA":
                print()
                menu()
                option = int(input("Introduceti optiunea dumneavoastra: "))
                print()
            elif a == "NU" or a == "nu" or a == "Nu" or a == "nU":
                break
            else:
                print()
                print("Programul se va inchide deoarece s-au introdus raspunsuri indescriptibile")
                break
    elif option != 1 or option != 2:
        print()
        print("Introduceti optiuni valide!")
        print()
        option = int(input("Introduceti optiunea dumneavoastra: "))
        print()

