import numpy as np
import math
#der er nogle tilfælde hvor s og t skal flippes, dette nævnes senere tho.
#evt test om s*a+t*b =sfd(a,b)
#hvis det er lig hinanden, så er det rigtigt, ellers så flip dem.

def gcdamount(a, b): #dette er gcd, MEN vi returner slet ikke gcd, vi returner hvor mange gange der kræver at lave operationen,
    nOfIter = 2 #starter på 2 fordi vi i tabellen først sætter a og b ind.
    while b:
        nOfIter += 1
        a, b = b, a % b
    return nOfIter


def NormalEucl(a, b):
    r0 = a
    r1 = b
    listforRk = []
    while r1 != 0:
        tmp = r0 % r1
        r0 = r1
        r1 = tmp
        listforRk.append(tmp)  # appender a mob b resultatet

    listforRk.insert(0, a)  # indeks 0 skal være lig a jf. euklids udvidet algori
    listforRk.insert(1, b)  # indeks 1 skal være lig b jf. eulids. udvidet
    global x #dårlig ide, men lige hvad jeg kunne finde på
    x = np.asarray(listforRk)  # converter til numpy, jeg har brug for denne liste både på s_k og t_k så laver den global.
    return x


def sK(k):
    if k == 0:
        return 1
    if k == 1:
        return 0
    else:
        return sK(k - 2) - math.floor(x[k - 2] / x[k - 1]) * sK(
            k - 1)  # faktisk er der lidt fejl her, da vi kan ikke calle 'x' som er r_k værdierne, men det virker
                    # eftersom jeg har sat x til global... dårlig ide, men det var lige hvad jeg kunne finde på


def tK(k): #samme præcis som før, det er bare den matematiske definition af hvordan t_k værdierne udregnes, rekursivt.
    if k == 0:
        return 0
    if k == 1:
        return 1
    else:
        return tK(k - 2) - math.floor(x[k - 2] / x[k - 1]) * tK(k - 1)


def ECEATG(a, b):  # EuclideanExtendedAlgorithmTableGenerator
    a1 =a
    b1 = b
    if a1<b1:#basecase, hvis a<b, så skal de flippes jf. euklids algo.
        a =b1
        b = a1
        print("A<B ER SANDT, SÅ FLIP RESULTATERNE, DVS.  s*a+t*b bliver nu t*a+s*b, altså resultatet i næstsidste kolonnene.")

    RowN = gcdamount(a, b)
    TableGen = np.zeros(shape=(RowN, 4))  # Laver en matrix på størrelse med hvad tablet skal være
    for i in range(RowN):  # fra 0 til 5, vi indsætter bare k indeks værdierne..
        TableGen[i][0] = i

    # gør klar til euclidean algorithm
    rKs = NormalEucl(a, b)  # liste med værdier af resterne
    # print(x)
    for i in range(len(rKs)):  # looper så vi får indekserne dvs. længden af rKs
        TableGen[i][1] = rKs[i]  # vi indsætter i anden række, de ting der står på rKs'ets indekser.

    listforSk = []  # liste til at holde s_k værdierne
    for i in range(RowN):  # lopper så vi kører mængden af rækkerne
        listforSk.append(sK(i))  # vi kallder algoritmen for hver af værdierne, i indekset (se nederst for algo)

    for i in range(len(listforSk)):  # loper så vi får indekserne.
        TableGen[i][2] = listforSk[i]  # vi indsætter i tredje ræke, de ting der står på s_k'ets indekser.

    listfortk = []
    for i in range(RowN):
        listfortk.append(tK(i))

    for i in range(len(listfortk)):
        TableGen[i][3] = listfortk[i]

    expcolumn = [0]*RowN #create empty list of size of amount of rows
    expcolumn[0] = "Dette er a"
    expcolumn[1] = "Dette er b"
    #print(rKs)
    for i in range(len(rKs)-2):
        expcolumn[i+2] = "Da " + str(rKs[i]) + " = " + str(math.floor(rKs[i]/rKs[i+1])) + " * " + str(rKs[i+1]) + " + " +str(rKs[i] % rKs[i+1])


    expcolumn = np.array([expcolumn]).T #laver til numpy 2d matrix, og transposer den så vi kan sætte den på den rigtige matrix.
    TableGen= np.hstack((TableGen, expcolumn))


    #cut den næst sidste række ud og print s og t resultaterne. indeks 2 og 3 og så opstil resultatet.
    cutresult = TableGen[-2:-1,2:4] #vi får s og t
    if a1 < b1:
        t = int(float(cutresult[0,0]))
        s = int(float(cutresult[0,1]))
        print("s = " + str(s))
        print("t = " + str(t))
        print("sfd("+str(a1)+","+str(b1)+ ") = s*a+t*b = "+str(s)+"*"+str(a1)+" + "+str(b1) + "*"+str(t)+" = " +
              str(s*a1+t*b1))
        print("sfd(" + str(a1) + "," + str(b1) + ") = " +str(math.gcd(a1,b1)))
        print("Hvis ovenstående to tal IKKE er lig hinanden er der fejl i koden og derved fejl i nedenstående tabel. ")
    else:
        s = int(float(cutresult[0, 0]))
        t = int(float(cutresult[0, 1]))
        #print("hello")
        print("s = " + str(s))
        print("t = " + str(t))
        print(
            "sfd(" + str(a1) + "," + str(b1) + ") = s*a+t*b = " + str(s) + "*" + str(a1) + " + " + str(t) + "*" + str(
                b1) + " = " +
            str(s * a1 + t * b1))
        print("sfd(" + str(a1) + "," + str(b1) + ") = " + str(math.gcd(a1, b1)))
        print("Hvis ovenstående to tal IKKE er lig hinanden er der fejl i koden og derved fejl i nedenstående tabel. ")

    words = ["k", "r_k", "s_k", "t_k", "forklaring"]
    print()
    print(words)
    return TableGen


#print(ECEATG(195,85))


#TODO
"""

Fix koden lidt, da global x er shit kode, og jeg bruger rKs listen, selvom der blot kunne bruges x listen nu hvor den er global
x listen er blot r_k værdierne. dvs. resterne 

"""
