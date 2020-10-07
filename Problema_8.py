"""
Se  introduc  de  la  tastatură  trei  cifre.  Afişaţi  pe  aceeaşi  linie  5  numere  formate  cu aceste cifre luate o singură dată. Exemplu: date de intrare: 3 4 2  Date de ieşire: 324  342   243  234  432
"""
numar=input("Dati un numar de 3 cifre: ")
print(numar[2]+numar[1]+numar[0],"",numar[0]+numar[1]+numar[2],"",numar[1]+numar[0]+numar[2],"",numar[2]+numar[0]+numar[1],"",numar[1]+numar[2]+numar[0])
