def unimod(L):
    '''Hilfsfunktion, was eine Liste von Integers
    zu eine Liste von Symbole(+,-,=) umwandelt bzw.
    wenn die Folge steigt +, falls es sinkt - 
    oder wenn die Zahlen Gleich sind ='''
    lessgreater_than = ['+'] # Fuer unimodular Folgen sucher wir immer wo es zuerst Steigt
    for i in range(1,len(L)):
        if L[i-1] < L[i]:
            lessgreater_than.append('+') # Steigt
        elif L[i-1] > L[i]:
            lessgreater_than.append('-') # Sinkt
        else:
            lessgreater_than.append('=') # Gleichheit
    return lessgreater_than

def maxunimod(L):
    if len(L) == 1:
        return 1
    longest_unimod = 0 # Laenge unimodulare Sub-Folge
    if L: # Wenn Liste nicht leer
        og_unimod = unimod(L)
        for i in range(len(L)):
            l_updown = og_unimod[:]
            l_updown[i] = '+' # s.o
            length = 1 # Zaehlt die Laenge
            for j in range(i+1,len(L)):
                if l_updown[j] == '=':
                    length += 1
                    l_updown[j] = l_updown[j-1]
                elif l_updown[j-1] == '+':
                    if l_updown[j] == '+':
                        length += 1
                    else:
                        length += 1
                elif l_updown[j-1] == '-':
                    if l_updown[j] == '-':
                        length += 1
                    else: # Ende unimodularen Sub-Folge
                        if longest_unimod < length:
                            longest_unimod = length
                        break
                if j == len(L)-1: # Ende
                    if longest_unimod < length:
                        longest_unimod = length
    else: # falls die Liste leer ist, longest_unimod = 0
        return longest_unimod
    return longest_unimod