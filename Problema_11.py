"""
Măriuca  ţine  evidenţa  iepurilor  din  crescătorie.  
Ea  îşi  notează  câţi  iepuri  sunt  la începutul fiecărei luni, 
câţi au murit şi câţi s-au născut în cursul fiecăei luni. 
Puteţi să realizaţi un program care, primind aceste date, 
să afişezela sfârşitul fiecărei luni câţi iepuri suntîn crescătorie?
 Exemplu: Date de intrare: nr. Iepuri la început de luna 10  
 nr. iepuri morti 2  nr. iepuri nascuti 6  Date de ieşire: 14 iepuri.  
"""
initial=int(input("Dati numarul de iepuri la inceput de luna: "))
morti=int(input("Citi iepuri au murit: "))
nascuti=int(input("Citi s-au nascut: "))
print("In total in crescatorie sunt",initial-morti+nascuti,"iepuri")
