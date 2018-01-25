import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton,QLineEdit, QTextEdit, QLabel
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
import numpy as np
import math


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
        #print("A<B ER SANDT, SÅ FLIP RESULTATERNE, DVS.  s*a+t*b bliver nu t*a+s*b, altså resultatet i næstsidste kolonnene.")

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

    else:
        s = int(float(cutresult[0, 0]))
        t = int(float(cutresult[0, 1]))

    return TableGen
"""""""""""""""""""""""""""""""""""""""""""""""""""""BELOW IS GUI, ABOVE IS ONLY COPY-PASTED CODE FROM THE ONLYTABLERETURN script!"""""""""""""""""""""
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Euclidean Table Generator'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(50,50,600,600)

        # Create textbox for value a
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText('ENTER a VALUE HERE')
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create textbox for value b

        self.textbox2 = QLineEdit(self)
        self.textbox2.setPlaceholderText('ENTER b VALUE here')
        self.textbox2.move(20,100)
        self.textbox2.resize(280,40)


        # Create a button in the window
        self.button = QPushButton('Calculate Euclidean Table', self)
        self.button.resize(200,50)
        self.button.move(20, 150) #x,y (right,highrvalue = lower down)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click) # den siger .connect er en error, men lortet virker ikke uden, no idea why

        # Create a button for restart scenario
        self.restartbutton = QPushButton('Restart',self)
        self.restartbutton.resize(200,50)
        self.restartbutton.move(230,150)
        #connect restart button to function restart_click

        self.restartbutton.clicked.connect(self.restart_click)


        # Create textbox for the results

        self.outputbox = QTextEdit(self)
        self.outputbox.setFontPointSize(14)
        self.outputbox.setText('Your output will be shown here')
        self.outputbox.setFontPointSize(10)
        self.outputbox.setReadOnly(True) #brugeren skal ikke kunne slette noget, så setreadonly = TRUE
        self.outputbox.move(30, 220)
        self.outputbox.resize(530, 355)

        #info label
        self.infolabel = QLabel('Input information',self)
        self.infolabel.setFont(QtGui.QFont("Times",weight=QtGui.QFont.Bold))
        self.infolabel.move(400,10)
        #info text
        self.infotext = QLabel('Input should be that of sfd(a,b) where the first box\nis the a value, and then next box is the b value.\nOutput will be in the white box.\n '+
                               '\nNumbers in the matrix will be flipped if a<b,\nas described in the Euclidean Algorithm\nIn the output, the matrix is in floats, however they\nshould be interpreted as integers',self)
        self.infotext.resize(270,100)
        self.infotext.move(320,40)


        self.show()

    global words
    words = ["k  ", "  r_k", "   s_k", "  t_k", "  forklaring"]
    @pyqtSlot()
    def on_click(self):
        a = self.textbox.text()
        b = self.textbox2.text()
        if (a.isdigit() or (a.startswith('-') and a[1:].isdigit())) and (b.isdigit()  or (b.startswith('-') and b[1:].isdigit())): #tjekker om input er integer
            #print("you entered an integer")
            a = int(a)
            b = int(b)
            self.outputbox.setText("You entered sfd(a,b) = sfd("+str(a)+","+str(b)+")\n"
                                    +"Your output is the following table\n\n"
                                   +str(words)+"\n"+str(ECEATG(a,b)) #kalder rent faktisk metoden der udregner her

                                   )
        else:
            self.outputbox.setFontPointSize(20)
            self.outputbox.setText("Enter a valid integer!\n"*4)
            self.outputbox.setFontPointSize(12) #vi skifter tilbage efter vi har råbt lidt af dem


    @pyqtSlot()
    def restart_click(self):
        a = ''
        b = ''
        self.textbox.clear() #vi fjerner inputtet på begge
        self.textbox2.clear()
        self.outputbox.setText("Your output will be displayed here: ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
