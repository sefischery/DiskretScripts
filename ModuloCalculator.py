import math
def mod(a,b):
    if a<b:
        print("a værdien er blot resultatet, da a<b.  = "+str(a))
    else:
        firstString = " a mod b = a-(b*floor(a/b))\n"
        step1str = "Indsæt værdierne i formlen:\n"
        step2str = str(a) + " mod " + str(b) + " = " + str(a) + " -(" + str(b) + "*floor(" + (
        str(a) + "/" + str(b) + "))\n")
        step3str = "Udregn floor delen:\n"
        step4str = "floor(" + (str(a) + "/" + str(b) + ") = " + str(math.floor(a / b))) + "\n"
        step5str = "Udregn da hele udtrykket\n"
        step6str = str(a) + " mod " + str(b) + " = " + str(a) + "-(" + str(b) + "*(" + str(
        math.floor(a / b)) + ")) = " + str(a - (b * math.floor(a / b))) + "\n"

        print(firstString, step1str, step2str, step3str, step4str, step5str, step6str)


mod(2,3)