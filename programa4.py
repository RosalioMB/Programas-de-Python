print('ESCRIBE UN NUMERO ')
palindromo1 = input()

ver_palindromo = palindromo1[:: - 1 ]

if ver_palindromo.replace(" ", "") == palindromo1.replace(" ", ""):
    print("Es capicua")
else:
    print("No es capicua")
    


        
