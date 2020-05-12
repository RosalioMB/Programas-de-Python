print('¿ESCRIBE UN PALINDROMO?')
palindromo = input()

palindromo1 = palindromo.upper()

ver_palindromo = palindromo1[:: - 1 ]

if ver_palindromo.replace(" ", "") == palindromo1.replace(" ", ""):
    print("Es un palindromo")
else:
    print("No es un palindromo")
    


        
