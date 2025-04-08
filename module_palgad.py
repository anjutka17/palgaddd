p=[]
i=[]
#�lesanne1
def lisa_andmed(p:list,i:list):
    """Funktsioon leiab nende palgad ja mitu inimesed
    :param i: Sisend t�hed
    :param p: Sisend numbrid
    :rtype:M��remata t��p (str v�i float)
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
                print("Kirjuta ainult t�hed")
        except:
            print("Kirjuta ainult t�htede kasutades")
    p.append(palk)
    i.append(nimi)
#�lesanne2
def kustuta_andmed(p:list,i:list):
    """Funktsioon kustuta palgad ja inimesed,kui i ja p>0
    :param i: Sisend t�hed
    :param p: Sisend numbrid
    :param nimi: Sisend str
    :rtype:M��remata t��p (str v�i float)
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
            print("Kirjuta ainult t�htede kasutades")
#�lesanne3
def suurim_palk(p:list,i:list):
    """Funktsioon leiab suurim palgad inimestel
    :param i: Sisend t�hed
    :param p: Sisend numbrid
    :rtype:M��remata t��p (str v�i float)
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    ind=p.index(suurim)
    for j in range(k):
        ind=p.index(suurim,ind)
        print(f"Saab k�tte {i[ind]}")
        ind+=1
#�lesanne4
def v�iksem_palk(p:list,i:list):
    """Funktsioon leiab v�iksem palgad inimestel
    :param i: Sisend t�hed
    :param p: Sisend numbrid
    :rtype:M��remata t��p (str v�i float)
    """
    v�iksem=min(p)
    print(f"V�iksem palk on {v�iksem}")
    k=p.count(v�iksem)
    ind=p.index(v�iksem)
    for j in range(k):
        ind=p.index(v�iksem,ind)
        print(f"Saab k�tte {i[ind]}")
        ind+=1
#�lesanne5
def kas_kah_palk(p:list,i:list)->any:
    """Funktsioon j�rjesab palgad kasvavas ja kahanevas j�rjekorras koos nimedega
    :param inimesed: Inimeste nimekiri
    :param palgad: Palkade nimekiri
    :rtype: any
    """
    while True:
        try:
            v=input("Vali m�rk: >(kasvav) v�i < (kahanev)")
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

       
#�lesanne6
def v�rdsed_palk(p:list,i:list):
    """Funktsioon leiab kes saavad v�rdset palka, ja kui palju neid on ja kuvada nende andmed ekraanile
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
                print(f"Saab k�tte {i[ind]}")
                ind+=1

#�lesanne7
def palgaotsing(i: list, p: list):
    """
    Funktsioon otsib inimese palga nime j�rgi.
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
#�lesanne8
def rohkem_vahem(i: list, p: list):
    """
    Funktsioon leiab inimesed, kes saavad rohkem v�i v�hem kui m��ratud summa.
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
while True:
    summa = float(input("Sisesta summa: "))
    break
try:    
    valik = input("Kas soovid rohkem (r) v�i v�hem? (v)?: ").lower()
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
#�lesanne9 
def top_inimesed(i: list, p: list):
    """
    Funktsioon leiab inimesed suurima ja v�ikseima palgaga.
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
    suurim_palk = max(p)
    print(f"Suurim palk: {suurim_palk} ")
    for j in range(len(p)):
        if p[j]==suurim_palk:
            print(f"{i[j]}")
    v�iksem_palk = min(p)
    print(f"V�iksem palk: {v�iksem_palk} ")
    for j in range(len(p)):
        if p[j]==v�iksem_palk:
            print(f"{i[j]}")

#�lesanne10
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
        print("Palkade nimekiri on t�hi.")














### EMILIA DARK (theme)