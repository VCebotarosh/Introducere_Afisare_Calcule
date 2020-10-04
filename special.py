suma=int(float(input("Dati suma in lei:")))
bancnote_1000=0
bancnote_500=0
bancnote_200=0
bancnote_100=0
bancnote_50=0
bancnote_20=0
bancnote_10=0
bancnote_5=0
bancnote_2=0
bancnote_1=0
while(suma>=1000):
    suma-=1000
    bancnote_1000+=1
else:
    while(suma>=500):
        suma=suma-500
        bancnote_500+=1
    else: 
        while(suma>=200):
            suma-=200
            bancnote_200+=1
        else: 
            while(suma>=100):
                suma-=100
                bancnote_100+=1
            else: 
                while(suma>=50):
                    suma-=50
                    bancnote_50+=1
                else: 
                    while(suma>=20):
                        suma-=20
                        bancnote_20+=1
                    else: 
                        while(suma>=10):
                            suma-=10
                            bancnote_10+=1
                        else: 
                            while(suma>=5):
                                suma-=5
                                bancnote_5+=1
                            else: 
                                while(suma>=2):
                                    suma-=2
                                    bancnote_2+=1
                                else: 
                                    if(suma==1):
                                        bancnote_1=1
print("sunt",bancnote_1000,"bancnote de 1000")
print("sunt",bancnote_500,"bancnote de 500")
print("sunt",bancnote_200,"bancnote de 200")
print("sunt",bancnote_100,"bancnote de 100")
print("sunt",bancnote_50,"bancnote de 50")
print("sunt",bancnote_20,"bancnote de 20")
print("sunt",bancnote_10,"bancnote de 10")
print("sunt",bancnote_5,"bancnote de 5")
print("sunt",bancnote_2,"bancnote de 2")
print("sunt",bancnote_1,"bancnote de 1")

print("[+] Aceasta linie a fost adaugata recent")
