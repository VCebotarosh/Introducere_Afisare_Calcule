"""
Maria vrea să verifice dacă greutatea şi înălţimea ei corespund vârstei pe care o are. Ea a găsit într-o carte următoarele formule de calcul ale greutăţii şi înălţimii unui copil, v fiind vârsta : greutate=2*v+8 (în kg), înălţime=5*v+80 (în cm). Realizaţi un program care să citească vârsta unui copil şi să afişeze greutatea şi înălţimea ideală, folosind aceste formule.
"""
virsta=int(input("Dati virsta dumneavoastra: "))
greutate=2*virsta+8
inaltime=5*virsta+80
print("Greutate ideala este",greutate,"kg iar inaltimea ideala este",inaltime,"cm")
