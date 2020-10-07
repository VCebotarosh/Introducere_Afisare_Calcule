"""
De  la  tastatură  se  întroduce  numărul  de  rînd  al  culorii  curcubeului.  
De  afişat denumirea culorii. Convenim că culoarea roşie are numărul de rînd 1.
"""
rind=int(input("dati numarul de rind al culorii curcubeului: "))
if(rind==1):
    print("Pe rindul 1 e culoarea rosie")
if(rind==2):
    print("Pe rindul 2 e culoarea oranj")
if(rind==3):
    print("Pe rindul 3 e culoarea galben")
if(rind==4):
    print("Pe rindul 4 e culoarea verde")
if(rind==5):
    print("Pe rindul 5 e culoarea albastru")
if(rind==6):
    print("Pe rindul 6 e culoarea indigo")
if(rind==7):
    print("Pe rindul 7 e culoarea violet")
if(rind>7 or rind<1):
    print("Curcubeul are doar 7 culori.")