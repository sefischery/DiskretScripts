from ExtendedEUCLAlgorithmGeneratorTabel import *
import math
def KGRSolver(b1,b2,n1,n2):  #jf. afsnit 5.3 i diskret bogen (del 2)
#Dette er kun for sætning Den kinsesiske restklassesætning
#DET ER ANTAGET AT LIGNING 1 (N1) ER STØRRE END LIGNING 2 (N2)
#ELLERS SÅ FLIP DEM, DVS BARE SÆT LIGNING TIL AT VÆRE LIGNING 2...
#DETTE ER DEN KINESISKE REST KLASSE SÆTNING.
#hvor sfd(n1,n2) =1
#DETTE ER IKKE FOR SÆTNING 5.4 i bogen.
    b1tmp =b1
    b2tmp = b2
    n1tmp = n1
    n2tmp =n2

    if math.gcd(n1,n2) != 1: #basistilfælde, sfd(n1,n2) skal være lig 1.
        print("sfd("+str(n1)+","+str(n2)+") er ikke lig 1, systemet kan ikke løses umiddelbart")
    else:
        if n1<n2:
            b1 = b2tmp
            b2 = b1tmp
            n1 = n2tmp
            n2 = n1tmp

        TableGen = ECEATG(n1, n2) #euklids udvidede, tabel halløj


        print(TableGen)
        cutresult = TableGen[-2:-1, 2:4]
        s = int(float(cutresult[0, 0]))
        t = int(float(cutresult[0, 1]))
        u1 = s
        u2 = t
        xp = u1 * n1 * b2 + u2 * n2 * b1 #formel
        k = n1 * n2 #formel
        stringText = "Vi tjekker først om sfd(n1,n2) = 1, som vi kan se af tabellen er rigtigt. Da dette er sandt" \
                 ", kan vi anvende den kinesiske restklassesætning.\nFølges eksempel 5.7s metodik, kan vi anvende" \
                 " Euklids Udvidede Algoritme og få tabellen som ovenstående.\nDet ses af tabellen at " \
                 "sfd(" + str(n1) + "," + str(n2) + ")=1=" + str(s) + "*" + str(n1) + "+" + str(t) + "*" + str(
        n2) + "\n" \
              "Derfor er x_p = u1*n1*b2+u2*n2*b1" \
              "=" + str(s) + "*" + str(n1) + "*" + str(b2) + "+" + str(t) + "*" + str(n2) + "*" + str(
        b1) + " = " + str(xp) + "\n" \
                                "De to kongruenser er da jf. den Kinesiske Restklassesætning, ækvivalent med den ene kongruens dvs:\n" \
                                "x ≡ " + str(xp) + "(mod " + str(n1) + "*" + str(n2) + ")" + "\n" \
                                                                                             "Da " + str(
        n1) + "*" + str(n2) + " =" + str(n1 * n2) + " kan vi konkludere at løsningsmængden er lig:"
        print(stringText)
        print(str(xp) + " + " + str(k) + "Z")

        return "Vi tager modulus og simplificere:\n" + str(xp % (n1*n2)) + " + " + str(k) + "Z"# xp%*n1,n2 ER FUCKING VIGTIGT. IKKE ORDENTLIGT FORKLARET I BOGEN


print(KGRSolver(2,1,101,17))


# # # DER ER ET PROBLEM NÅR DEN CALLER, DEN ANDEN FUNKTION ****** WATCH THE FUCK OUT *****