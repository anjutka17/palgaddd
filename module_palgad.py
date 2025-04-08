p=[]
i=[]
#ülesanne1
def lisa_andmed(p:list,i:list):
    """Funktsioon leiab nende palgad ja mitu inimesed
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :rtype:Määremata tüüp (str või float)
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                    palk=float(input("Palk: "))
                except:
                    print("Palk on arv")
                break
                print("Andmed on lisatud")
            else:
                print("Kirjuta ainult tähed")
        except:
            print("Kirjuta ainult tähtede kasutades")
    p.append(palk)
    i.append(nimi)
#ülesanne2
def kustuta_andmed(p:list,i:list):
    """Funktsioon kustuta palgad ja inimesed,kui i ja p>0
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :param nimi: Sisend str
    :rtype:Määremata tüüp (str või float)
    """
    try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                k=i.count(nimi)
                if k>0:
                    for j in range(k):
                        ind=i.index(nimi)
                        i.pop(ind)
                        p.pop(ind)
                        print("Andmed on lisatud")
            else:
                print("Andmed puuduvad!")
    except:
            print("Kirjuta ainult tähtede kasutades")
#ülesanne3
def suurim_palk(p:list,i:list):
    """Funktsioon leiab suurim palgad inimestel
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :rtype:Määremata tüüp (str või float)
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    ind=p.index(suurim)
    for j in range(k):
        ind=p.index(suurim,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1
#ülesanne4
def väiksem_palk(p:list,i:list):
    """Funktsioon leiab väiksem palgad inimestel
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :rtype:Määremata tüüp (str või float)
    """
    väiksem=min(p)
    print(f"Väiksem palk on {väiksem}")
    k=p.count(väiksem)
    ind=p.index(väiksem)
    for j in range(k):
        ind=p.index(väiksem,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1
#ülesanne5
def kas_kah_palk(p:list,i:list)->any:
    """Funktsioon järjesab palgad kasvavas ja kahanevas järjekorras koos nimedega
    :param inimesed: Inimeste nimekiri
    :param palgad: Palkade nimekiri
    :rtype: any
    """
    while True:
        try:
            v=input("Vali märk: >(kasvav) või < (kahanev)")
            if v in('>','<'):
                break
            else:
                print("Ainult "<" ja ">"")
        except:
            print("Viga! Proovi uuesti!")
            for n in range(0,len(i)):
                for m in range(n,len(i)):
                    if eval(str(p[n])+v+str+(p[m])):
                        p[n],p[m]=p[m],p[n]
                        i[n],i[m]=i[m],i[n]

       
#ülesanne6
def võrdsed_palk(p:list,i:list):
    """Funktsioon leiab kes saavad võrdset palka, ja kui palju neid on ja kuvada nende andmed ekraanile
    :param inimesed: Inimeste nimekiri
    :param palgad: Palkade nimekiri
    :rtype:none
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1

#ülesanne7
def palgaotsing(i: list, p: list):
    """
    Funktsioon otsib inimese palga nime järgi.
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
    nimi=input("Sisesta nimi mida sa sooviks: ")
    leitud=False
    for j in range(len(i)):
       if i[j]==nimi:
           print(f"{nimi} palk: {p[j]}")
           leitud=True
    else:
        print(f"{nimi} kohta andmeid ei leitud.")
#ülesanne8
def rohkem_vahem(i: list, p: list):
    """
    Funktsioon leiab inimesed, kes saavad rohkem või vähem kui määratud summa.
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
while True:
    summa = float(input("Sisesta summa: "))
    break
try:    
    valik = input("Kas soovid rohkem (r) või vähem? (v)?: ").lower()
    if valik == "r":
       for j in range(len(p)):
           if p[j] > summa:
                   print(f"{i[j]} saab {p[j]}")
           elif valik == "v":
                  for j in range(len(p)):
                         if p[j] < summa:
                            print(f"{i[j]} saab {p[j]}")
    else:
         print("Vale valik!")
except:
       print("Vigane sisend!")
#ülesanne9 
def top_inimesed(i: list, p: list):
    """
    Funktsioon leiab inimesed suurima ja väikseima palgaga.
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
    suurim_palk = max(p)
    print(f"Suurim palk: {suurim_palk} ")
    for j in range(len(p)):
        if p[j]==suurim_palk:
            print(f"{i[j]}")
    väiksem_palk = min(p)
    print(f"Väiksem palk: {väiksem_palk} ")
    for j in range(len(p)):
        if p[j]==väiksem_palk:
            print(f"{i[j]}")

#ülesanne10
def keskmine_palk(i: list, p: list):
    """
    Funktsioon arvutab keskmise palga ja otsib inimesed, kes seda saavad.
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
    if len(p) > 0:
        avg=sum(p)/len(p)
        print(f"Keskmine palk: {avg:.0f}")
        for j in range(len(p)):
            if p[j] ==avg:
                print(f"{i[j]} saab keskmist palka.")
    else:
        print("Palkade nimekiri on tühi.")














### EMILIA DARK (theme)