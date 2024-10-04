"""
author: adel.beghdadi@edu.esiee.fr
"""
#### Imports et définition des variables globales


#### Fonctions secondaires

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    c = []
    o = []
    art = []
    k = 1
    n = len(s)
    c.append(s[0])
    o.append(1)
    while k < n:
        if s[k] == s[k-1]:
            o[-1] += 1
        else:
            c.append(s[k])
            o.append(1)
        k += 1
    for d,e in enumerate(c):
        art.append((e,o[d]))
    return art

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    
    """
    art_temp = []
    n = len(s)
    buf = 255
    if n > buf:
        art_1 = artcode_r(s[buf:])
        art_2 = artcode_r(s[:buf])
        if art_2[-1][0] == art_1[0][0]:
            art_2[-1] = ((art_1[0][0],art_1[0][1]+art_2[-1][1]))
            art_1.pop(0)
        art_temp = art_2 + art_1
    else:
        if n == 1:
            return [(s,1)]
        c = s[0]
        temp = artcode_r(s[1:])
        if c == temp[0][0]:
            art_temp.append((c,temp[0][1] + 1))
            art_temp = art_temp + (temp[1:])
        else:
            art_temp.append((c,1))
            art_temp = art_temp + (temp)
    return art_temp

#### Fonction principale
def main():
    """
    Fonction principale qui lance les fonctions secondaires
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))
if __name__ == "__main__":
    main()
