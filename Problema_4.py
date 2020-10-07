"""
Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. Numărul globuleţelor albe se citeşte de la tastatură. Câte globuleţe are brăduţul, ştiind că numărul de globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, iar globuleţele albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. Exemplu: Date de intrare: 12 Date de ieşire: 52.
"""
globulete_albe=int(input("Dati nr de globulete able: "))
globulete_rosii=globulete_albe+3
globulete_albastre =(globulete_albe+globulete_rosii)-2
total=globulete_albe+globulete_albastre+globulete_rosii
print("Bradutul are",total,"globulete")
