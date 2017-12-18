import math
from ONLYTABLERETURN import ECEATG
def solvekongruens(a,b,n):
    if b==1:
        print("Dette er et specialtilfælde hvor b=1,jf. def 5.3 ")
        if math.gcd(n,a) != 1:
            print("Der er ingen løsning da sfd(n,a) ikke er lig 1, dvs a ikke har en multiplikativ invers (mod n)")
        else:
            TableGen = ECEATG(n,a)
            #print(TableGen)
            cutresult = TableGen[-2:-1, 2:4]  # vi får s og t
            #s = int(float(cutresult[0, 0]))
            t = int(float(cutresult[0, 1]))
            print("Vi bruger Euklids Udvidede algoritme")
            print(TableGen)
            print("Dit svar er t (eller c,x.etc) = "+str(t))
            print("Da "+str(t) +"*"+str(a)+" ≡ 1 (mod "+str(n)+")")
            print("Husk på at der er flere løsninger, dette er blot én. En anden løsning vil være hvor vi tager "+str(t)+" mod "+str(n)+"= "+str(t % n))

    else:
        print("Dette er tilfældet hvor b>1 ")
        d = math.gcd(n,a)
        print("d = "+str(d))
        if (b % d) != 0:
            print("Da d ikke går op i b, har kongruensligningen ingen løsninger")
        else:
            print("Da d går op i b, anvendes sætning 5.2 og vi får en ny kongruensligning. ")
            a = int(a/d)
            b = int(b/d)
            n = int(n/d)
            print("Den nye ligning a'x≡ b' (mod n') er da:")
            print(str(a)+"x≡"+str(b)+" (mod "+str(n)+")")
            print("Denne er ækvivalent med x≡cb (mod n) jf. sætning 5.3")
            TableGen = ECEATG(n,a)
            cutresult = TableGen[-2:-1, 2:4]  # vi får s og t
            t = int(float(cutresult[0, 1]))
            s = int(float(cutresult[0,0]))
            print("Ved at køre Euklids algoritme fås:")
            print(TableGen)
            c = t
            print("s*n+t*a = "+str(s*n+t*a))
            print("S = " + str(s))
            print("n = "+ str(n))
            print("t = c =  "+ str(t))
            print("a = " +str(a))
            print("b = " +str(b))
            print("Da kan vi se at "+str(c)+"*"+str(a)+"≡ 1 mod "+str(n))#dette er da
            print("HVIS "+str(c)+"*"+str(a)+" mod " + str(n)+" IKKE ER LIG 1. SÅ SKAL MAN VÆLGE KOLONNE S VÆRDIEN dvs." +str(s))
            print("Check: "+str(c)+"*"+str(a)+" mod " + str(n) +" = " +str((c*a)% n))
            print("Derfor er ligningen ækvivalent med\n x ≡ "+str(c*b)+" (mod "+str(n)+")")
            print("Hvoraf vi ser løsningsmængden er "+str(c*b)+"+"+str(n)+"Z  eller "+ str((c*b)%n)+"+"+str(n)+"Z , hvis man tager modulus")
            print("Den nye ligning, hvis den skal anvendes videre vil være x ≡ "+str((c*b)%n)+" (mod "+str(n)+")")
solvekongruens(9,1,30) #HVIS B TALLET ER STØRRE END A TALLET VIL DEN REGNE FORKERT... B'TALLET SKAL ALTSÅ VÆRE DET MINDSTE...

#B TALLET SKAL VÆRE DET MINDSTE TAL.
#VIRKER DOG HVIS B>A OG B<C