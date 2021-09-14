#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(chaine) -> bool:
    liste = []
    for i in chaine:
        liste.append(i)
    if len(liste)%2 == 0:
        return True

    pass

def remove_third_char(chaine) -> str:
    liste = list(chaine)
    del(liste[2])
    string = "".join(liste)

    return string
    pass


def replace_char(string: str, old_char: str, new_char: str) -> str:
    liste = list(string)
    for i in range(len(liste)):
        if liste[i] == "w":
            liste[i] = "z"
    allo = "".join(liste)
    return allo



def get_number_of_char(string: str, char: str) -> int:
    liste = list(string)
    c = 0
    for i in range(len(liste)):
        if liste[i] == "l":
            c +=1
    return c

    pass


def get_number_of_words(sentence: str, word: str) -> int:
    a = sentence.split()
    c = 0
    for i in range(len(a)):
        if a[i] == "doo":
            c += 1
    return c


    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
