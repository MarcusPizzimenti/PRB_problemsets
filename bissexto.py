#!/usr/bin/env python3
def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):  # se o ano for divisível por 4, o resto será igual a zero (ano % 4 == 0) 
        return True
    else:
        return False

anos_para_testar = [1912, 2003, 2020, 2024, 2100] 

for ano in anos_para_testar:
    if bissexto(ano):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")

