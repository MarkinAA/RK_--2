''' program '''
CHISLO1 = int(input())
CHISLO2 = int(input())
OPERACH = str(input())
if OPERACH == '+':
    print(CHISLO1 + CHISLO2)
elif OPERACH == '-':
    print (CHISLO1 - CHISLO2)
elif OPERACH == '*':
    print (CHISLO1 * CHISLO2)
elif  OPERACH == '/':
    if (CHISLO1 / CHISLO2) > int(CHISLO1 / CHISLO2):
        print (CHISLO1 / CHISLO2)
    else:
        print (int(CHISLO1 / CHISLO2))
