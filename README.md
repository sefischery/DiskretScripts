# DiskretScripts

####UPDATE#####
MyGUI.exe indeholder nu ONLYTABLERETURN.py hvilket stortset er fuldstændig ligesom den originale ExtendedEUCLAlgorithmGeneratorTabel.py fil gør. Her er det meget mere smooth i det at der er et GUI og man ikke skal kigge i consolen. (Imo, meget bedre). 

MyGUI.py er MyGUI.exe scriptet, det er blot blevet compilet til en exe, via Pyinstaller. I MyGUI.py er alt PyQT5 koden og så koden fra tablereturn da det var nødsaget at copypaste koden over i ét script da pyinstaller ikke kan tage flere .py filer og compile :( 
########

ExtendedEUCLAlgorithmGeneratorTabel:
Tager 2 tal som input, og printer tabellen af euklids algoritme. 

ModulCalculator:
Tager to tal og printer en udførlig gennemregning for at tage modulus.

ONLYTABLERETURN:
Printer hvad ExtendedEUCLAlgorithmGeneratorTabel gør, men uden nogen form for 
melleregninger og lignende.

SignleKongruensligning:
Tager en kongruensligning af form (a*x=b mod n) hvor den skal skrives som (a,b,n)
Og printer da melleregninger

Kongruengsligninger:
Tager input (b1,b2,n1,n2) i form af ligning (x = b1 mod n1, x = b2 mod n2)
og printer mellem regninger ift. xp udrengningen osv.
