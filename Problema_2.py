"""
Într-o tabără numărul de băieţi este cu 10 mai mare decât cel al fetelor. Dacă se citeşte de la tastatură numărul de fete, să se spună câţi elevi sunt în tabără. Exemplu: date de intrare: 50  date de ieşire: 110
"""
nr_fete=int(input("Dati numarul de fete care sunt in tabara: "))
nr_baieti=nr_fete+10
total_copii=nr_fete+nr_baieti
print("In tabara sunt",total_copii,"copii")
